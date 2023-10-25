def createNewDictEntry(line):
    return {
            'ticker': line['Description'].split(" ")[1], # get ticker from here as 'Ticker' field in csv is inconsistent
            'currentQuantity': 0,
            'cons': 0,
            'buySum': 0,
            'sellSum': 0,
            'net': 0,
            'sellDate': line['Post Date'],
            'letExpire': False
        }