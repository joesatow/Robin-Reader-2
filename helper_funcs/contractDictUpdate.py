from dataFunctions import getCurrentValue

def getContractDictUpdate(currentContract, line):
    currentContract = contractDict[description]
    transactionCode = line['Trans Code']

    currentContract['currentQuantity'] += quantity # add quantity.  since there's both positive (buys) and negative (sells) values, it'll eventually zero out (trade is done).
    currentContract['cons'] = max(currentContract['cons'], abs(currentContract['currentQuantity']))
    currentContract['net'] += amount

    currentQuantity = getCurrentValue(1, line)
    currentAmount = getCurrentValue(2, line)
    
    if transactionCode == 'OEXP':
        currentContract['letExpire'] = True
    if transactionCode == 'BTO':
        currentContract['buySum'] += amount
    elif transactionCode == 'STC': # STC or OEXP
        currentContract['sellSum'] += amount
    
    return {
        description: {
            'currentQuantity': currentQuantity,
            'cons': max(c)
        }
    }


contractDict = {
    "tsla 420c": {
        "ticker": 'test',
        'cons': 1
    }
}

description = "tsla 420c"
contractDict.update({
    description : {
        "ticker": "blue",
        "cons": 2
    }
})
print()