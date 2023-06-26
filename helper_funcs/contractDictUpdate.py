from dataFunctions import getCurrentValue

def getContractDictUpdate(currentContract, line):
    currentContract = contractDict[description]
    transactionCode = line['Trans Code']

    newQuantity = currentContract['currentQuantity'] + getCurrentValue(1, line) # add quantity.  since there's both positive (buys) and negative (sells) values, it'll eventually zero out (trade is done).
    newContractCount = max(currentContract['cons'], abs(currentContract['currentQuantity']))

    amount = getCurrentValue(2, line)
    newNet = currentContract['net'] + amount
    
    if transactionCode == 'OEXP':
        currentContract['letExpire'] = True
    if transactionCode == 'BTO':
        currentContract['buySum'] += amount  ###### Fix all these to go in the update object
    elif transactionCode == 'STC': # STC or OEXP
        currentContract['sellSum'] += amount
    
    updateObject = {
        description: {
            'currentQuantity': newQuantity,
            'cons': newContractCount,
            'net': newNet
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