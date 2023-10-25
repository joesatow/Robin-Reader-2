from .dataFunctions import getCurrentValue

def getContractDictUpdate(currentContract, line):
    transactionCode = line['Type']

    # Get quantity by adding current quantity thats in the dictionary + the quantity from the new line of data
    newQuantity = currentContract['currentQuantity'] + getCurrentValue(1, line) # add quantity.  since there's both positive (buys) and negative (sells) values, it'll eventually zero out (trade is done).
    
    # Get contract count
    newContractCount = max(currentContract['cons'], abs(currentContract['currentQuantity']))

    # get amount, which is the total dollars of the transaction
    amount = getCurrentValue(2, line)

    # calculate net by adding the amount to the current contract's net
    newNet = currentContract['net'] + amount

    updateObject = {
        'currentQuantity': newQuantity,
        'cons': newContractCount,
        'net': newNet
    }

    if transactionCode == 'Journal':
        updateObject.update({
            'letExpire': True
        })

    if transactionCode == 'Buy':
        newBuySum = currentContract['buySum'] + amount
        updateObject.update({
            'buySum': newBuySum
        })
    elif transactionCode == 'Sell':
        newSellSum = currentContract['sellSum'] + amount
        updateObject.update({
            'sellSum': newSellSum
        })

    return updateObject