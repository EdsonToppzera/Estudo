def main():
    lst = []
    produtos = ["MILK", "MANGO", "STRAWBERRY", "SWEET POTATO", "TORTILLA", "APPLE", "SUGAR", "BANANA"]

    while True:
        try:
            item = input().upper()

            if item == "":
                break  # Exit the loop if empty input is provided

            if item in produtos:
                lst.append(item)

        except EOFError:
            break  # Exit the loop if EOFError occurs

    contagem = {i: lst.count(i) for i in lst}
    contagem_letra = sorted(list(contagem.keys()))
    contagem_numero = [contagem[i] for i in contagem_letra]

    for letra, numero in zip(contagem_letra, contagem_numero):
        print(f"{numero} {letra}")

if __name__ == "__main__":
    main()
