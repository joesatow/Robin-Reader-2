from .fileFunctions import getData
from .filter import filterData
from .dataFunctions import getCurrentValue
from .contractDictFunctions import createNewDictEntry
from .contractDictUpdate import getContractDictUpdate
from .tradeListFunctions import getTradeDictUpdate
from .outputFunctions import writeCSV
     
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
  description = getCurrentValue(0, line)

  if description not in contractDict:
    contractDict[description] = createNewDictEntry(line)

  currentContract = contractDict[description]

  contractDict[description].update(getContractDictUpdate(currentContract, line))

  if currentContract['currentQuantity'] == 0:
    tradeList.append(getTradeDictUpdate(currentContract, description, line['Process Date'])) # use process date to get buy date
    del contractDict[description]

writeCSV(tradeList)