from helper_funcs.fileFunctions import getData
from helper_funcs.filter import filterData
from helper_funcs.dataFunctions import getCurrentValue, getAverages
from helper_funcs.contractDictFunctions import createNewDictEntry
from helper_funcs.contractDictUpdate import getContractDictUpdate
     
# Get account activity list
accountActivityList = getData()

# Filter data
accountActivityList = filterData(accountActivityList)

# contract dictionary to track positions until closed
# using a dictionary is a good way to track because sometimes you open multiple options at once.
contractDict = {}

for line in accountActivityList:
  description = getCurrentValue(0, line)

  if description not in contractDict:
    contractDict[description] = createNewDictEntry(line)

  currentContract = contractDict[description]
  contractDict[description].update(getContractDictUpdate(currentContract, line))

  if currentContract['currentQuantity'] == 0:
    averageBuy, averageSell, pctChange = getAverages(currentContract['buySum'], currentContract['sellSum'], currentContract['cons']).values()
    if currentContract['letExpire'] == True:
      print()
    del contractDict[description]


print()
