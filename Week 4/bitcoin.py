import sys
import json
import requests

try:

    bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    site = bitcoin.json()
    usd_rate_float = site["bpi"]["USD"]["rate_float"]
    print(f"${usd_rate_float * float(sys.argv[1]):,.4f}")


except requests.RequestException:
    sys.exit()

except ValueError:
    sys.exit("Command-line argument is not a number")

except IndexError:
    sys.exit("Missing command-line argument")

