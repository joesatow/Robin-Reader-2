def createNewDictEntry(line):
    return {
            'ticker': line['Instrument'],
            'currentQuantity': 0,
            'cons': 0,
            'buySum': 0,
            'sellSum': 0,
            'net': 0,
            'startDate': '',
            'endDate': line['Process Date'],
            'letExpire': False
        }