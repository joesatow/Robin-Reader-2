from helper_funcs.fileFunctions import getData
from helper_funcs.filter import filterData
from helper_funcs.dataFunctions import getUniqueVals, getAverages
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

  description, quantity, amount = getUniqueVals(transactionCode, line).values()

  if description not in contractDict:
    contractDict[description] = createNewDictEntry(line)

  currentContract = contractDict[description]
  currentContract['currentQuantity'] += quantity # add quantity.  since there's both positive (buys) and negative (sells) values, it'll eventually zero out (trade is done).
  currentContract['cons'] = max(currentContract['cons'], abs(currentContract['currentQuantity']))
  currentContract['net'] += amount
  
  if transactionCode == 'OEXP':
      currentContract['letExpire'] = True
  if transactionCode == 'BTO':
      currentContract['buySum'] += amount
  elif transactionCode == 'STC': # STC or OEXP
      currentContract['sellSum'] += amount

  if currentContract['currentQuantity'] == 0:
    averageBuy, averageSell, pctChange = getAverages(currentContract['buySum'], currentContract['sellSum'], currentContract['cons']).values()
    print()

print()