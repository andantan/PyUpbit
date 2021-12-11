import cryptocompare
import requests
import threading
import sys

price = {}

MARKET_URL= "https://api.upbit.com/v1/candles/days"

headers = {
    "Accept": "application/json"
}

upbit_symbol = sys.argv[1].replace('-', '')

querystring = {
    "market": f"KRW-{upbit_symbol}",
    "count": "0"
}

CYCE_KEY = "737ffc78c4cf7f5c325e811461ffe0e8ba794e6b1f5db7c9657d1473150be809"

cryptocompare.cryptocompare._set_api_key_parameter(CYCE_KEY)

def get_price(symbol):
    tickers1 = ["BTC", "ETH"]
    tickers2 = ["XRP", "ADA", symbol]
    

    try:
        ticker = cryptocompare.get_price(tickers1 + tickers2, currency="USDT", full=True)

        for element in tickers1:
            price[element] = round(ticker["RAW"][element]["USDT"]["PRICE"], 1)
            price[element + "OPEN"] = round(ticker["RAW"][element]["USDT"]["OPEN24HOUR"], 1)

        for element in tickers2:
            price[element] = ticker["RAW"][element]["USDT"]["PRICE"]
            price[element + "OPEN"] = ticker["RAW"][element]["USDT"]["OPEN24HOUR"]
    except:
        pass

def get_price_by_upbit():
    try:
        response = requests.request("GET", MARKET_URL, headers=headers, params=querystring).json()

        price[upbit_symbol + "U"] = response[0]["trade_price"]
    except:
        pass

def get_btc_price_by_upbit():
    try:
        QSNG = {
            "market": "KRW-BTC",
            "count": "0"
        }

        response = requests.request("GET", MARKET_URL, headers=headers, params=QSNG).json()

        price["BTCF"] = int(response[0]["trade_price"])
    except:
        pass

def upbit_get_usd_krw():
    try:
        url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
        exchange = requests.get(url, headers=headers).json()
        
        price["exchange"] = exchange[0]['basePrice']
    except:
        pass

upbit_thread = threading.Thread(target=get_price_by_upbit)
upbit_thread_btc = threading.Thread(target=get_btc_price_by_upbit)
exchange_thread = threading.Thread(target=upbit_get_usd_krw)
adorable_thread = threading.Thread(target=get_price, args=(upbit_symbol, ))

upbit_thread.start()
upbit_thread_btc.start()
exchange_thread.start()
adorable_thread.start()

upbit_thread.join()
upbit_thread_btc.join()
exchange_thread.join()
adorable_thread.join()

output = ""

for k, v in price.items():
    output += f"{k}={v} "

print(output)