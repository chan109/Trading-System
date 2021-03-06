from __future__ import print_function
# from flask import Flask
# from flask import request
# from flask.json import jsonify
import flask
# import flask.Response
import sys
import urllib2
import json


app = flask.Flask(__name__)
global user_balance
user_balance = 10000
global portfolio
portfolio = {}
global all_stocks
all_stocks = {}

def getSymbols():
    symbols = ["ABT", "ABBV", "ACN", "ACE", "ADBE", "ADT", "AAP", "AES", "AET", "AFL", "AMG", "A", "GAS",
                            "APD", "ARG"]# "AKAM", "AA", "AGN", "ALXN", "ALLE", "ADS", "ALL", "ALTR", "MO", "AMZN", "AEE",
                            #"AAL", "AEP", "AXP", "AIG", "AMT", "AMP", "ABC", "AME", "AMGN", "APH", "APC", "ADI", "AON"]
                            # "APA", "AIV", "AMAT", "ADM", "AIZ", "T", "ADSK", "ADP", "AN", "AZO", "AVGO", "AVB", "AVY",
                            # "BHI", "BLL", "BAC", "BK", "BCR", "BXLT", "BAX", "BBT", "BDX", "BBBY", "BRK-B", "BBY", "BLX",
                            # "HRB", "BA", "BWA", "BXP", "BSK", "BMY", "BRCM", "BF-B", "CHRW", "CA", "CVC", "COG", "CAM", "CPB",
                            # "COF", "CAH", "HSIC", "KMX", "CCL", "CAT", "CBG", "CBS", "CELG", "CNP", "CTL", "CERN", "CF", "SCHW", "CHK",
                            # "CVX", "CMG", "CB", "CI", "XEC", "CINF", "CTAS", "CSCO", "C", "CTXS", "CLX", "CME", "CMS", "COH", "KO", "CCE",
                            # "CTSH", "CL", "CMCSA", "CMA", "CSC", "CAG", "COP", "CNX", "ED", "STZ", "GLW", "COST", "CCI", "CSX", "CMI", "CVS",
                            # "DHI", "DHR", "DRI", "DVA", "DE", "DLPH", "DAL", "XRAY", "DVN", "DO", "DTV", "DFS", "DISCA", "DISCK", "DG", "DLTR",
                            # "D", "DOV", "DOW", "DPS", "DTE", "DD", "DUK", "DNB", "ETFC", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA",
                            # "EMC", "EMR", "ENDP", "ESV", "ETR", "EOG", "EQT", "EFX", "EQIX", "EQR", "ESS", "EL", "ES", "EXC", "EXPE",
                            # "EXPD", "ESRX", "XOM", "FFIV", "FB", "FAST", "FDX", "FIS", "FITB", "FSLR", "FE", "FSIV", "FLIR", "FLS",
                            # "FLR", "FMC", "FTI", "F", "FOSL", "BEN", "FCX", "FTR", "GME", "GPS", "GRMN", "GD", "GE", "GGP", "GIS",
                            # "GM", "GPC", "GNW", "GILD", "GS", "GT", "GOOGL", "GOOG", "GWW", "HAL", "HBI", "HOG", "HAR", "HRS", "HIG",
                            # "HAS", "HCA", "HCP", "HCN", "HP", "HES", "HPQ", "HD", "HON", "HRL", "HSP", "HST", "HCBK", "HUM", "HBAN",
                            # "ITW", "IR", "INTC", "ICE", "IBM", "IP", "IPG", "IFF", "INTU", "ISRG", "IVZ", "IRM", "JEC", "JBHT", "JNJ",
                            # "JCI", "JOY", "JPM", "JNPR", "KSU", "K", "KEY", "GMCR", "KMB", "KIM", "KMI", "KLAC", "KSS", "KRFT", "KR", "LB",
                            # "LLL", "LH", "LRCX", "LM", "LEG", "LEN", "LVLT", "LUK", "LLY", "LNC", "LLTC", "LMT", "L", "LOW", "LYB", "MTB",
                            # "MAC", "M", "MNK", "MRO", "MPC", "MAR", "MMC", "MLM", "MAS", "MA", "MAT", "MKC", "MCD", "MHFI", "MCK", "MJN",
                            # "MMV", "MDT", "MRK", "MET", "KORS", "MCHP", "MU", "MSFT", "MHK", "TAP", "MDLZ", "MON", "MNST", "MCO", "MS", "MOS",
                            # "MSI", "MUR", "MYL", "NDAQ", "NOV", "NAVI", "NTAP", "NFLX", "NWL", "NFX", "NEM", "NWSA", "NEE", "NLSN", "NKE", "NI",
                            # "NE", "NBL", "JWN", "NSC", "NTRS", "NOC", "NRG", "NUE", "NVDA", "ORLY", "OXY", "OMC", "OKE", "ORCL", "OI", "PCAR",
                            # "PLL", "PH", "PDCO", "PAYX", "PNR", "PBCT", "POM", "PEP", "PKI", "PRGO", "PFE", "PCG", "PM", "PSX", "PNW", "PXD",
                            # "PBI", "PCL", "PNC", "RL", "PPG", "PPL", "PX", "PCP", "PCLN", "PFG", "PG", "PGR", "PLD", "PRU", "PEG", "PSA", "PHM",
                            # "PVH", "QRVO", "PWR", "QCOM", "DGX", "RRC", "RTN", "O", "RHT", "REGN", "RF", "RSG", "RAI", "RHI", "ROK", "COL", "ROP",
                            # "ROST", "RLC", "R", "CRM", "SNDK", "SCG", "SLB", "SNI", "STX", "SEE", "SRE", "SHW", "SIAL", "SPG", "SWKS", "SLG", "SJM",
                            # "SNA", "SO", "LUV", "SWN", "SE", "STJ", "SWK", "SPLS", "SBUX", "HOT", "STT", "SRCL", "SYK", "STI", "SYMC", "SYY",
                            # "TROW", "TGT", "TEL", "TE", "TGNA", "THC", "TDC", "TSO", "TXN", "TXT", "HSY", "TRV", "TMO", "TIF", "TWX", "TWC", "TJK", "TMK", "TSS",
                            # "TSCO", "RIG", "TRIP", "FOXA", "TSN", "TYC", "UA", "UNP", "UNH", "UPS", "URI", "UTX", "UHS", "UNM", "URBN", "VFC", "VLO", "VAR", "VTR",
                            # "VRSN", "VZ", "VRTX", "VIAB", "V", "VNO", "VMC", "WMT", "WBA", "DIS", "WM", "WAT", "ANTM", "WFC", "WDC", "WU", "WY", "WHR", "WFM", "WMB",
                            # "WEC", "WYN", "WYNN", "XEL", "XRX", "XLNX", "XL", "XYL", "YHOO", "YUM", "ZBH", "ZION", "ZTS"]
    return symbols

@app.route('/stocks/all')
def allStocks():
    global all_stocks
    symbolList = getSymbols()
    query = buildQuery(symbolList)
    response = json.loads(urllib2.urlopen(query).read())
    # return jsonify(response["query"])

    #TODO: parse safely
    quotes = response["query"]["results"]["quote"]

    for quote in quotes:
        symbol = quote["Symbol"]
        price = quote["LastTradePriceOnly"]
        name = quote["Name"]
        change = quote["Change"]
        time = quote["LastTradeTime"]
        all_stocks[symbol] = {"name": name, "symbol": symbol, "price": price, "change": change, "time": time}

    return flask.jsonify(all_stocks)

def buildQuery(symbolList):
    query_prefix = "https://query.yahooapis.com/v1/public/yql?q=select%20Symbol%2CLastTradePriceOnly%2CLastTradeTime%2CLastTradeDate%2CChange%2CName%20from%20yahoo.finance.quotes%20where%20symbol%20in%20("
    query_suffix = ")&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
    query_companies = ""

    first_symbol = True
    for symbol in symbolList:
        if first_symbol:
            first_symbol = False
            query_companies = "%22{0}%22".format(symbol)
        else:
            query_companies += "%2C%22{0}%22".format(symbol)

    return query_prefix + query_companies + query_suffix

@app.route('/stocks/buy', methods=['POST'])
def buyStock():
    print('hello')
    global all_stocks
    global portfolio
    global user_balance
    symbol = flask.request.form['symbol']#.encode('ascii')
    print(all_stocks.keys())
    print(symbol)
    #quantity = flask.request.form['quantity']
    stock = all_stocks[symbol]
    price = stock["price"]

    if portfolio.has_key(symbol):
        portfolio[symbol] = {"quantity": portfolio[symbol]["quantity"] + 1, "price": all_stocks[symbol]["price"], "name": all_stocks[symbol]["name"], "change": all_stocks[symbol]["change"]}
    else:
        portfolio[symbol] = {"quantity": 1, "price": all_stocks[symbol]["price"], "name": all_stocks[symbol]["name"], "change": all_stocks[symbol]["change"]}

    user_balance -= float(price)

    print(user_balance)

    return flask.jsonify(user_balance)

@app.route('/stocks/sell', methods=['POST'])
def sellStock():
    global all_stocks
    global portfolio
    global user_balance
    symbol = flask.request.form['symbol']#.encode('ascii')
    print(all_stocks.keys())
    print(symbol)
    #quantity = flask.request.form['quantity']
    stock = all_stocks[symbol]
    price = stock["price"]

    if portfolio.has_key(symbol):
        quantity = portfolio[symbol]["quantity"]
        if quantity > 0:
            user_balance += float(price)
            portfolio[symbol] = {"quantity": quantity - 1, "price": all_stocks[symbol]["price"], "name": all_stocks[symbol]["name"], "change": all_stocks[symbol]["change"]}

    print(user_balance)

    return flask.jsonify(user_balance)

@app.route('/user/balance')
def getBalance():
    global user_balance
    return flask.jsonify(user_balance)

@app.route('/user/portfolio')
def getPortfolio():
    global portfolio
    return flask.jsonify(portfolio)

@app.after_request
def apply_caching(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = "GET, PUT, POST, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] =  "Origin, X-Requested-With, Content-Type, Accept"
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
