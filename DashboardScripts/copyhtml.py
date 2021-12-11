pairs = {
    "MKR": 1,
    "COMP" : 1,
    "FIL": 1,
    "NMR": 1,
    "LUNA": 1,
    "AUCTION": 1,
    "UNI": 1,
    "PSG": 1,
    "PROM": [],
    "JUV": 1,
    "INJ": 1,
    "MASK": 1,
    "SNX": 1,
    "NEAR": 1,
    "SBD": [],
    "CELO": 1,
    "RLC": 1,
    "CRV": 1,
    "BNT": True,
    "ALGO": 1,
    "FX": [],
    "USDP": 1,
    "OGN": 1,
    "DAI": 1, # REVERSED
    "TUSD": 1,
    "GRT": 1,
    "HBD": [],
    "PCI": [],
    "CTSI": 1,
    "GXC": 1, # GXC -> GXS
    "LRC": 1,
    "NKN": 1,
    "CHR": 1,
    "OXT": 1,
    "AERGO": [],
    "BFC": [],
    "DAD": [],
    "RVN": 1,
    "ONIT": [],
    "SOLVE": [],
    "MARO": [],
    "FOR": 1,
    "IOTX": 1,
    "DGB": 1,
    "LINA": 1,
    "RSR": 1,
    "GO": ["BINANCE:GOUSD"],
    "SUN": 1,
    "OBSR": [],
    "BASIC": [],
    "DENT": 1,
    "QTCON": [],
}

default_html_lines = []

with open("./htmls/ZILBTC.html", "r") as handle:
    default_html_lines = [line.rstrip() for line in handle.readlines()]

for ticker in pairs.keys():
    default_pair = [f"UPBIT:{ticker}BTC"]

    if pairs[ticker] == 1:
        default_pair += [f"BINANCE:{ticker}USDT"]
    else:
        default_pair += pairs[ticker]

    for market in default_pair:
        html_lines = default_html_lines.copy()

        html_lines[19] = html_lines[19].replace("BINANCE:ZILBTC", market)

        if market.endswith("BTC"):
            with open(f"./aaaa/{ticker}BTC.html", "w") as handle:
                for line in html_lines:
                    handle.writelines(line + "\n")

        elif market.endswith("USDT"):
            with open(f"./aaaa/{ticker}USDT.html", "w") as handle:
                for line in html_lines:
                    handle.writelines(line + "\n")

        elif market.endswith("USD"):
            with open(f"./aaaa/{ticker}USD.html", "w") as handle:
                for line in html_lines:
                    handle.writelines(line + "\n")
