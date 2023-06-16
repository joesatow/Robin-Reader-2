from helper_funcs.handleFile import getData
from helper_funcs.filter import filterData
from helper_funcs.fixData import fixAmount

key = {
    'activityDate': '0',
    'processDate': '1',

}
    
# Get account activity list
accountActivityList = getData()

# Filter data
accountActivityList = filterData(accountActivityList)

# Fix amounts
for line in accountActivityList:
    transactionCode = line['Trans Code']

print()