import sys
import requests

try:
    quantidade = float(sys.argv[1])
except ValueError:
    sys.exit("The element is not a float")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Something is wrong")

arquivo = response.json()
bpi = arquivo["bpi"]
usd = bpi["USD"]
rate = float(usd["rate_float"])

total = rate*quantidade

print(f"${total:,.4f}")
