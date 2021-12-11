from numpy.core.defchararray import index
import requests
import jwt
import uuid

from pprint import pprint
import numpy as np
import pandas as pd

ONLY_BTC_MARKET_SYMBOL = [
    "AUCTION", "BFC", "BASIC",  "LRC",   "SOLVE",   "FIL",
    "MASK",    "RVN",   "PCI",  "LUNA",    "FOR",    "GO",
    "CHR",    "ONIT",  "MARK",  "GXC",     "SNX",    "FX",
    "VAL",    "CTSI",  "IOTX",  "NEAR",    "JUV",   "RSR",
    "OGN",    "ARGO",   "CRV",  "DGB",    "CELO",   "INJ",
    "SUN",    "PROM",   "OXT",  "DNT",    "COMP", "QTCON",
    "DENT",    "UNI",  "LINA",  "HBD",     "GRT",   "DAD",
    "LRC",     "PSG",   "NKN",  "BNT",    "TUSD",   "NMR",
    "MKR",    "USDP",
]

key = {
    "ACCESS_KEY": "WVSh6xWB1UwrZmf3Q30f2hxHGnEyhN8nWXGtXRyx",
    "SECRET_KEY": "l2zsmJaagsd2qLIY8I8xw3bDzfcgrFsHpxQx6bMX"
}

url = {
    "ACCOUNT_URL": "https://api.upbit.com/v1/accounts",
    "CANDLE_URL": "https://api.upbit.com/v1/candles/days",
}

query_payload = {
    "access_key": key["ACCESS_KEY"],
    "nonce": str(uuid.uuid4())
}

query_headers = {
    "Authorization": f"Bearer {jwt.encode(query_payload, key['SECRET_KEY'])}"
}

market_headers = {
    "Accept": "application/json"
}

market_querystring = {
    "market": "",
    "count": "0"
}

stocked_symbol = []

accounts_response = requests.get(url["ACCOUNT_URL"], headers=query_headers).json()

for element in accounts_response:
    if element["currency"] == "KRW":
        cash = element["balance"]

    if not element["avg_buy_price"] == '0':
        stocked_symbol.append([element["currency"], element["avg_buy_price"], element["balance"]])

market_querystring["market"] = "KRW-BTC"

btc_trade_price = requests.request("GET", url["CANDLE_URL"], headers=market_headers, params=market_querystring).json()[0]["trade_price"]

for symbol in stocked_symbol:
    if symbol[0] in ONLY_BTC_MARKET_SYMBOL:
        market_querystring["market"] = f"BTC-{symbol[0]}"

        candle_response = requests.request("GET", url["CANDLE_URL"], headers=market_headers, params=market_querystring).json()

        symbol.append(round(float(candle_response[0]["trade_price"]) * float(btc_trade_price), 3))
    else:
        market_querystring["market"] = f"KRW-{symbol[0]}"

        candle_response = requests.request("GET", url["CANDLE_URL"], headers=market_headers, params=market_querystring).json()

        symbol.append(candle_response[0]["trade_price"])

    symbol.append(int((float(symbol[1]) * float(symbol[2])))) # 매수금액
    symbol.append(int((float(symbol[2]) * symbol[3]))) # 평가금액
    symbol.append(symbol[5] - symbol[4])
    symbol.append(round(symbol[6] / symbol[4] * 100, 2))

cash = int(float(cash))

total = cash
amount_total = 0
eval_amount_total = 0

for symbol in stocked_symbol:
    total += symbol[4]
    amount_total += symbol[4]
    eval_amount_total += symbol[5]

for symbol in stocked_symbol:
    symbol.append(round(symbol[4] / total * 100, 1))

if (eval_amount_total < 0):
    return_total = abs(eval_amount_total) - amount_total
else:
    return_total = eval_amount_total - amount_total

margin_total = round(return_total / amount_total * 100, 2)
weight_total = round(amount_total / total * 100, 2)

stocked_symbol.append(["KRW", "0", cash, "0", "0", "0", "0", "0", round(cash / total * 100, 1)])
stocked_symbol.append(["TOTAL", "0", eval_amount_total + cash, "0", amount_total, eval_amount_total, return_total, margin_total, weight_total])

data_info = ["SYMBOL", "BID", "BALANCE", "QUOTE", "AMOUNT", "EVAL_AMOUNT", "RETURN", "MARGIN", "WEIGHT"]

for symbol in stocked_symbol:
    for k, v in dict(zip(data_info, symbol)).items():
        print(f"{k}={v},", end="")
    
    print(" ", end="")

# data = { symbol[0]: symbol[1:] for symbol in stocked_symbol }

# frame = pd.DataFrame(data, index=data_info[1:])

# print(frame.T)
