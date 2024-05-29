import sys
import requests

try:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    current_price = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit()


try:
    n = sys.argv[1]
    n = float(n)
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
print(f"${n*current_price:,.4f}")
