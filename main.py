import requests
import subprocess

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# subprocess.call('cd /', shell=True)
# subprocess.call('clear', shell=True)

print('The current price of Bitcoin is: ' + r.json()['bpi']['EUR']['rate'] + " " + r.json()['bpi']['EUR']['code'])
print('The current price of Bitcoin is: ' + r.json()['bpi']['USD']['rate'] + " " + r.json()['bpi']['USD']['code'])
print('Last Updated: ' + r.json()['time']['updated'])
# print('Bitcoin value is displayed via the Coindesk API.')
print(r.json()['disclaimer'])
# print(r.json())
