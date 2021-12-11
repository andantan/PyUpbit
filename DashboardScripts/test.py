import json

tojson = {'TUSD': ['BTC', 'USDT'], 
'PSG': ['BTC', 'USDT'], 
'ONIT': ['BTC'], 
'WAVES': ['BTC', 'USDT'], 
'WAXP': ['BTC', 'KRW', 'USDT'], 
'REP': ['BTC', 'KRW', 'USDT'], 
'HBD': ['BTC'], 
'STX': ['BTC', 'KRW', 'USDT'], 
'STPT': ['BTC', 'KRW', 'USDT'], 
'JUV': ['BTC', 'USDT'], 
'CHZ': ['BTC', 'KRW', 'USDT'], 
'CHR': ['BTC', 'USDT'], 
'CTSI': ['BTC', 'USDT'], 
'CELO': ['BTC', 'USDT'], 
'LTC': ['BTC', 'KRW', 'USDT'], 
'GRS': ['BTC', 'KRW'], 
'PROM': ['BTC'], 'AERGO': ['BTC', 'KRW'], 'SNX': ['BTC', 'USDT'], 'POWR': ['BTC', 'KRW'], 'DAD': ['BTC'], 'ANKR': ['BTC', 'KRW', 'USDT'], 'IOST': ['BTC', 'KRW', 'USDT'], 'COMP': ['BTC', 'USDT'], 'GXC': ['BTC', 'USDT'], 'NEAR': ['BTC', 'USDT'], 'MKR': ['BTC', 'USDT'], 'UNI': ['BTC', 'USDT'], 'CRV': ['BTC', 'USDT'], 'MOC': ['KRW'], 'LINA': ['BTC', 'USDT'], 'LRC': ['BTC', 'USDT'], 'BCH': ['BTC', 'KRW', 'USDT'], 'BTT': ['KRW', 'USDT'], 'PLA': ['KRW'], '1INCH': ['BTC', 'KRW', 'USDT'], 'ETH': ['BTC', 'KRW', 'USDT'], 'SOLVE': ['BTC'], 'MED': ['KRW'], 'EOS': ['BTC', 'KRW', 'USDT'], 'BORA': ['KRW'], 'SOL': ['BTC', 'KRW', 'USDT'], 'OGN': ['BTC', 'USDT'], 'STMX': ['BTC', 'KRW', 'USDT'], 'THETA': ['BTC', 
'KRW', 'USDT'], 'XEM': ['BTC', 'KRW', 'USDT'], 'CRO': ['KRW'], 'MTL': ['BTC', 'KRW', 'USDT'], 'POLY': ['BTC', 'KRW', 'USDT'], 'BASIC': ['BTC'], 'NU': ['BTC', 'KRW', 'USDT'], 'CRE': ['KRW'], 'FIL': ['BTC', 'USDT'], 'SUN': ['BTC', 'USDT'], 'ONT': ['BTC', 'KRW', 'USDT'], 'STRAX': ['BTC', 'KRW', 'USDT'], 'SNT': ['BTC', 'KRW'], 'XRP': ['BTC', 'KRW', 'USDT'], 'RSR': ['BTC', 'USDT'], 'TRX': ['BTC', 'KRW', 'USDT'], 'TFUEL': ['BTC', 'KRW', 'USDT'], 'QTCON': ['BTC'], 'ADA': ['BTC', 'KRW', 'USDT'], 'INJ': ['BTC', 'USDT'], 'OMG': ['BTC', 'KRW', 'USDT'], 'TT': ['KRW'], 'DKA': ['KRW'], 'FLOW': ['BTC', 'KRW', 'USDT'], 'SAND': ['BTC', 'KRW', 'USDT'], 'ARK': ['BTC', 'KRW', 'USD'], 'AUCTION': ['BTC', 'USDT'], 'ELF': ['BTC', 'KRW', 'USDT'], 'GAS': ['BTC', 'KRW', 'USDT'], 'OBSR': ['BTC'], 'UPP': ['KRW'], 'FOR': ['BTC', 'USDT'], 'MATIC': ['BTC', 'KRW', 'USDT'], 'NMR': ['BTC', 'USDT'], 'IQ': ['KRW'], 'ICX': ['BTC', 'KRW', 'USDT'], 'BTG': ['BTC', 'KRW', 'USDT'], 'SRM': ['BTC', 'KRW', 'USDT'], 'STRK': ['KRW'], 'XLM': ['BTC', 'KRW', 'USDT'], 'XEC': ['KRW', 'USDT'], 'NKN': ['BTC', 'USDT'], 'MVL': ['KRW'], 'ADAR': ['BTC', 'KRW', 
'USDT'], 'STEEM': ['BTC', 'KRW'], 'LOOM': ['BTC', 'KRW'], 'FCT2': ['KRW'], 'DENT': ['BTC', 'USDT'], 'IOTX': ['BTC', 'USDT'], 'HUM': ['KRW'], 'DGB': ['BTC', 'USDT'], 'LSK': ['BTC', 'KRW', 'USDT'], 'XTZ': ['BTC', 'KRW', 'USDT'], 'AAVE': ['BTC', 'KRW', 'USDT'], 'PUNDIX': ['KRW', 'USDT'], 'MLK': ['KRW'], 'BTC': ['KRW', 'USD', 'USDT'], 'AQT': ['KRW'], 'BAT': ['BTC', 'KRW', 'USDT'], 'PCI': ['BTC'], 'ATOM': ['BTC', 'KRW', 'USDT'], 'FX': ['BTC'], 'KAVA': ['BTC', 'KRW', 'USDT'], 'IOTA': ['BTC', 'KRW', 'USDT'], 'ZIL': ['BTC', 'KRW', 'USDT'], 'TON': ['KRW'], 'OXT': ['BTC', 'USDT'], 'ETC': ['BTC', 'KRW', 'USDT'], 'GO': ['BTC', 'USD'], 'DOT': ['BTC', 'KRW', 'USDT'], 'VET': ['BTC', 'KRW', 'USDT'], 'GLM': ['BTC', 'KRW'], 'LUNA': ['BTC', 'USDT'], 'RLC': ['BTC', 'USDT'], 'ORBS': ['KRW'], 'HIVE': ['BTC', 'KRW', 'USDT'], 'SXP': ['BTC', 'KRW', 'USDT'], 'JST': ['BTC', 'KRW', 'USDT'], 'AHT': ['KRW'], 'MBL': ['KRW', 'USDT'], 'HUNT': ['KRW'], 'KNC': ['BTC', 'KRW', 'USDT'], 'RFR': ['KRW'], 'HBAR': ['BTC', 'KRW', 'USDT'], 'RVN': ['BTC', 'USDT'], 'ZRX': ['BTC', 'KRW', 'USDT'], 'DOGE': ['BTC', 'KRW', 'USDT'], 'MFT': ['KRW', 'USDT'], 'SSX': ['KRW'], 'NEO': ['BTC', 'KRW', 'USDT'], 'BFC': ['BTC'], 'CBK': ['KRW'], 'LINK': ['BTC', 'KRW', 'USDT'], 'MARO': ['BTC'], 'QTUM': ['BTC', 'KRW', 'USDT'], 'MANA': ['BTC', 'KRW', 'USDT'], 'MASK': ['BTC', 'USDT'], 'QKC': ['BTC', 'KRW'], 'SC': ['BTC', 'KRW', 'USDT'], 'META': ['KRW'], 'DAI': ['BTC', 'USDT'], 'BNT': ['BTC', 'USDT'], 'SBD': ['BTC', 'KRW'], 'USDP': ['BTC', 'USDT'], 'GRT': ['BTC', 'USDT'], 'ALGO': ['BTC', 'USDT'], 'DAWN': ['KRW'], 'ENJ': ['BTC', 'KRW', 'USDT'], 'BSV': ['KRW']}


with open("./Pair.json", "w") as handle:
    json.dump(tojson, handle, indent=4) 