def createNewDictEntry(line):
    return {
            'ticker': '',
            'currentQuantity': 0,
            'cons': 0,
            'buySum': 0,
            'buyCons': 0,
            'sellSum': 0,
            'sellCons': 0,
            'net': 0,
            'startDate': '',
            'endDate': line['Process Date'],
            'letExpire': False
        }