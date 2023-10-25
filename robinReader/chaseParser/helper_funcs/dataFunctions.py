# OEXP = option expiration
# we'll need to get description, ticker, and quantity values differently if we're reading from a OEXP transaction code, because this is just the way Robinhood provided the line.
# these transactions will act the same as a 'sell'.  example: 10 contracts expired acts as 10 contracts sold for 0 dollars. 
# this is necessary for netting out quantity, since there's no STC transactions for some trades if you let them expire worthless.
# 0 = description
# 1 = quantity
# 2 = amount
def getCurrentValue(value, line):
    transCode = line['Type']

    if transCode == 'Journal':
        if value == 0:
            ticker = line["Ticker"]
            if ticker.split(" ")[0] != "":
                return ticker
            else:
                return reconstructDescription(ticker, line['Description'])
        if value == 1:
            return int(line['Quantity']) # quantity here is how many contracts expired.
        if value == 2:
            return  0 # 0 because the option expired worthless, equivalent to selling for 0 dollars.
    else: # standard Buy or Sell line
        if value == 0:
            ticker = line["Ticker"]
            if ticker.split(" ")[0] != "":
                return ticker
            else:
                return reconstructDescription(ticker, line['Description'])
        if value == 1:
            return int(line['Quantity'])
        if value == 2:
            price = float(line['Price USD'])
            quantity = int(line['Quantity'])
            total = price * quantity * 100
            if line['Type'] == "Buy":
                return -total
            else:
                return -total

def reconstructDescription(ticker, desc):
    ticker_from_description_field = desc.split(" ")[1]
    reconstructed_description = f"{ticker_from_description_field}{ticker}"
    return reconstructed_description
 
def getAverages(currentContract):
    buySum = currentContract['buySum']
    sellSum = currentContract['sellSum']
    cons = currentContract['cons']
    
    averageBuy = abs(round((buySum / cons)/100, 3))
    averageSell = abs(round((sellSum / cons)/100, 3))
    if averageSell == 0:
        pctChange = -1
    else:
        pctChange = -round(((averageBuy - averageSell) / averageBuy), 4)
    return {
        "averageBuy": averageBuy,
        "averageSell": averageSell,
        "pctChange": pctChange
    }