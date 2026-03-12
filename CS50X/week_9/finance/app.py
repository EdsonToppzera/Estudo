import os

from cs50 import SQL
#sqlite3 finance.db
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    #passar a database pro jinja
    money = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    rows = db.execute("SELECT symbol, total_shares FROM total WHERE user_id = ?", session["user_id"])

    dados = []
    true_total = 0

    for row in rows:
        # Chama a sua função lookup para cada símbolo
        dados_lookup = lookup(row["symbol"])

        if dados_lookup:
            # Calcula o valor total (Ações que eu tenho * Preço atual)
            valor_total = row["total_shares"] * dados_lookup["price"]
            true_total=true_total+valor_total

            # Adiciona um dicionário completo na nossa lista
            dados.append({
                "symbol": row["symbol"],
                "shares": row["total_shares"],
                "price": dados_lookup["price"],
                "total_value": valor_total
            })

    return render_template("index.html",dados=dados,true_total=true_total+money,cash=money)


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

        quoted=lookup(request.form.get("symbol"))
        if quoted != None:
            return render_template("quoted.html",quoted=quoted)
        else:
            return apology("Invalid Symbol")

    else:
        return render_template("quote.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        #'lookup' devolve um dicionário, então guardamos em 'stock'
        stock = lookup(request.form.get("symbol"))

        try:
            #Convertemos para 'int' para poder fazer cálculos
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("Invalid Symbol", 400)

        if stock == None:
            return apology("Invalid Symbol", 400)

        #O preço já está no dicionário 'stock', não precisa de outro lookup
        shares_price = stock["price"]
        #Pegamos o valor numérico de dentro da lista que o banco devolve
        money = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        if shares<1 or (shares*shares_price)>money:
            return apology("Invalid Symbol/Shares", 400)

        else:
            #atualiza cash apos a compra
            money=money-(shares*shares_price)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", money, session["user_id"])

            #atualiza o index (total)
            db.execute("""
                INSERT INTO total (user_id, symbol, total_shares)
                VALUES (?, ?, ?)
                ON CONFLICT(symbol)
                DO UPDATE SET total_shares = total_shares + excluded.total_shares
            """, session["user_id"], symbol, shares)

            #atualiza o historico (transactions)
            db.execute("INSERT INTO transactions(user_id,symbol,qtd,price) VALUES (?,?,?,?)",session["user_id"],symbol,shares,shares_price)


            return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method=="POST":
        money = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        symbol = request.form.get("symbol").upper()
        shares = int(request.form.get("shares"))
        total_shares = int(db.execute("SELECT total_shares FROM total WHERE symbol = ? AND user_id= ?",symbol,session["user_id"])[0]["total_shares"])

        if not request.form.get("shares"):
            return apology("Missing shares", 400)
        if db.execute("SELECT symbol FROM total WHERE symbol = ? AND user_id= ?",symbol,session["user_id"])==None or shares<1 or shares>total_shares:
            return apology("Invalid shares/symbol", 400)

        #atualiza historico
        db.execute("INSERT INTO transactions(user_id,symbol,qtd,price) VALUES (?,?,?,?)",session["user_id"],symbol,shares*-1,lookup(request.form.get("symbol"))["price"])

        #atualiza total
        db.execute("UPDATE total SET total_shares = ? WHERE symbol = ? AND user_id= ?",total_shares-shares,symbol,session["user_id"])
        #exclui row se total_shares=0
        db.execute("DELETE FROM total WHERE total_shares = 0")

        #atualiza o cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?",money+shares*lookup(symbol)["price"],session["user_id"])

        return redirect("/")

    else:
        #passar os simbolos da database pro select
        rows = db.execute("SELECT symbol FROM total WHERE user_id = ?", session["user_id"])

        dados = []

        for row in rows:
            # Chama a sua função lookup para cada símbolo
            dados_lookup = lookup(row["symbol"])

            if dados_lookup:
                # Adiciona um dicionário completo na nossa lista
                dados.append({
                    "symbol": row["symbol"],
                })

        return render_template("sell.html",dados=dados)



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT symbol, qtd, price, date FROM transactions WHERE user_id = ?", session["user_id"])

    return render_template("history.html",transactions_table=transactions)



@app.route("/cash", methods=["GET", "POST"])
@login_required
def cash():
    if request.method=="POST":
        money = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        try:
            plus_money = float(request.form.get("plus_money"))

            if plus_money > 0:
                #atualiza o cash
                db.execute("UPDATE users SET cash = ? WHERE id = ?",money+plus_money,session["user_id"])

                return redirect("/")

            else:
                return apology("Must be more than 0", 403)


        except ValueError:
            return apology("Invalid number", 403)

    else:
        return render_template("cash.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        #check if both passwords are the same
        elif request.form.get("confirmation")!=request.form.get("password"):
            return apology("the password and confirmation must be the same", 400)


        #insert new user to table
        try:
            password_hash = generate_password_hash(request.form.get("password"), method='scrypt', salt_length=16)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",request.form.get("username"),password_hash)

            # Redirect user to login
            return redirect("/login")

        except ValueError:
            return apology("username already exists", 400)


    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



# CREATE TABLE transactions (
#     user_id INTEGER NOT NULL,
#     transaction_id INTEGER PRIMARY KEY,
#     symbol TEXT NOT NULL,
#     qtd INTEGER NOT NULL,
#     price INTEGER NOT NULL,
#     date DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY(user_id) REFERENCES users(id)
# );
# CREATE TABLE total (
#     user_id INTEGER NOT NULL,
#     symbol TEXT NOT NULL UNIQUE,
#     total_shares INTEGER,
#     FOREIGN KEY(user_id) REFERENCES users(id)
# );
