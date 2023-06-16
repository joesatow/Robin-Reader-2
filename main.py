from helper_funcs.fileFunctions import getData
from helper_funcs.filter import filterData
from helper_funcs.dataFunctions import getUniqueVals
from helper_funcs.contractDictFunctions import createNewDictEntry
    
# Get account activity list
accountActivityList = getData()

# Filter data
accountActivityList = filterData(accountActivityList)

# contract dictionary to track positions until closed
# using a dictionary is a good way to track because sometimes you open multiple options at once.
contractDict = {}

for line in accountActivityList:
    transactionCode = line['Trans Code']

    description, ticker, quantity, amount = getUniqueVals(transactionCode, line).values()
    
    if description not in contractDict:
        contractDict[description] = createNewDictEntry(line)

    contractDict[description]['ticker'] = ticker
    contractDict[description]['currentQuantity'] += quantity # add quantity.  since there's both positive (buys) and negative (sells) values, it'll eventually zero out (trade is done).
    contractDict[description]['cons'] = max(contractDict[description]['cons'], abs(contractDict[description]['currentQuantity']))
    contractDict[description]['net'] += amount
    
    print()