import requests
import subprocess


def current_price(currency):
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    value = r.json()['bpi'][currency]['rate']
    # print('The current price of Bitcoin is: ' + r.json()['bpi']['EUR']['rate'] + " " + r.json()['bpi']['EUR']['code'])
    # print('The current price of Bitcoin is: ' + r.json()['bpi']['USD']['rate'] + " " + r.json()['bpi']['USD']['code'])
    # print('Last Updated: ' + r.json()['time']['updated'])
    # # print('Bitcoin value is displayed via the Coindesk API.')
    # print(r.json()['disclaimer'])
    # # print(r.json())
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


# XVGBTC = Fund()

# print(TRXBTC)
print("Total amount of " + trxbtc.longname + ": " + str(trxbtc.amount) + " " + trxbtc.name)
print("BTC->USD = " + current_price('USD'))
print("BTC->EUR = " + current_price('EUR'))
