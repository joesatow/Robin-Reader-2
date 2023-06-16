from helper_funcs.handleFile import getData
from helper_funcs.filter import filterData
from helper_funcs.fixData import fixAmount, getUniqueVals
    
# Get account activity list
accountActivityList = getData()

# Filter data
accountActivityList = filterData(accountActivityList)

# Fix amounts
for line in accountActivityList:
    transactionCode = line['Trans Code']

    uniqueValsDict = getUniqueVals(transactionCode, line)
    description = uniqueValsDict["description"]
    ticker = uniqueValsDict["ticker"]
    quantity = uniqueValsDict["quantity"]
    amount = uniqueValsDict["amount"]
print()