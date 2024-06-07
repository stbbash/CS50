import requests
import json
import sys

try:
    if len(sys.argv) != 2:
        raise ValueError("Missing command-line argument")
    n = float(sys.argv[1])
    if n < 0:
        raise ValueError("Negative integer not allowed")
except ValueError:
    sys.exit("Invalid command-line argument")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    print("Invalid JSON response")
rate = response["bpi"]["USD"]["rate"]
price = '{:,.4f}'.format(float(rate.replace(',', '')) * n)
print(f"${price}")
