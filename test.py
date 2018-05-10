import requests
def getprice(fuck):
    coins = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=100000000000").json()
    sms = []
    for dongxu in coins:
		if dongxu["symbol"] == fuck:
			abc = "" + dongxu['symbol'] + ': '+'$ '+ dongxu['price_usd']+" ("+dongxu['percent_change_24h']+"%)"
			print abc
getprice("BCC")