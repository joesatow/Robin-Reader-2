from helper_funcs.handle_file import getData
from helper_funcs.filter import filterData

# Get account activity list
accountActivityList = getData()

# Filter data
accountActivityList = filterData(accountActivityList)

print()
