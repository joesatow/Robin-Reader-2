from robinReader.chaseParser.helper_funcs.fileFunctions import getData
from robinReader.chaseParser.helper_funcs.filter import filterData
from robinReader.chaseParser.helper_funcs.dataFunctions import getCurrentValue
from robinReader.chaseParser.helper_funcs.contractDictFunctions import createNewDictEntry
from robinReader.chaseParser.helper_funcs.contractDictUpdate import getContractDictUpdate
from robinReader.chaseParser.helper_funcs.tradeListFunctions import getTradeDictUpdate
from robinReader.chaseParser.helper_funcs.outputFunctions import writeCSV
      
# Get account activity list
accountActivityList = getData()

# Filter data
accountActivityList = filterData(accountActivityList)

# contract dictionary to track positions until closed
# using a dictionary is a good way to track because sometimes you open multiple options at once.
contractDict = {}

# trade List to keep track of closed trades
tradeList = []

for line in accountActivityList:
  # description is important because it is used as the key for our dictionary of contracts.  
  # we need to grab it with getCurrentValue() because broker reports have different descriptions for expiration/buy/sell
  description = getCurrentValue(0, line)

  if description not in contractDict:
    contractDict[description] = createNewDictEntry(line)

  currentContract = contractDict[description]

  contractDict[description].update(getContractDictUpdate(currentContract, line))

  if currentContract['currentQuantity'] == 0:
    tradeList.append(getTradeDictUpdate(currentContract, description, line['Post Date'])) # use process date to get buy date
    del contractDict[description]

writeCSV(tradeList)