import requests


def current_price(currency):
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    value = r.json()['bpi'][currency]['rate']
    return value


class Fund:

    def __init__(self):
        self.amount = 0
        self.name = ""
        self.longname = ""


trxAmount = 62151 + 931 + 39558 + 5992 + 6544
trxbtc = Fund()
trxbtc.name = "TRX"
trxbtc.longname = "TRON"
trxbtc.amount = trxAmount

current_usd = current_price('USD')
current_eur = current_price('EUR')


print("Total amount of " + trxbtc.longname + ": " + str(trxbtc.amount) + " " + trxbtc.name)
print("BTC->USD = " + current_usd)
print("BTC->EUR = " + current_eur)
