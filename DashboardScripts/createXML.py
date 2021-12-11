import os

market = ("KRW", "BTC", "USD", "USDT")

pairs = [x.replace(".html", "") for x in os.listdir("./htmls") if x.replace(".html", "").endswith(market)]

symbols = []

for pair_element in pairs:
    if pair_element.endswith(("KRW", "BTC", "USD")):
        symbols.append(pair_element[:-3])
    elif pair_element.endswith("USDT"):
        symbols.append(pair_element[:-4])

pair = { symbol: [] for symbol in list(set(symbols)) }

for a, b in dict(zip(pairs, symbols)).items():
    pair[b].append(a.replace(b, ""))

print(pair)

# xml = "<tickers>\n"

# for k, v in pair.items():
#     for e in v:
#         xml += "\t<ticker>\n"
#         xml += f"\t\t<symbol>{k}</symbol>\n"
#         xml += f"\t\t<market>{e}</market>\n"
#         xml += "\t</ticker>\n"

# xml += "</tickers>"

# with open("./pair.xml", "w") as handle:
#     handle.write(xml)