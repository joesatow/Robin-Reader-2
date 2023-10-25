# fileFunctions.py
#   return data dictionary list without slicing 

# filter.py
#   change names of variables/fucntions to actually make sense
#   filter by security type instead of buy/sell/journal - since those could be equity purchases

# main.py
#    add comments above description variable
#   Line 35: can use line['Post Date'] 

# dataFunctions.py
#   lots of stuff
#   line 24 and 31: can both just return line['Ticker'] as this provides the option description were looking for
#   line 26: no S to replace, no need to make negative as chase does it already.
#   Line 33: change transCode to 'Buy'
#   Line 29: comment 
#   getCurrentValue -> else clause -> if value==1 - can change to one line since numbers are already correct in chase


# contractDictFunctions.py
#   change 'ticker' to the 'ticker' field and split it by space (" ") and use first element
#   change 'sellDate' to "Post Date" field

# contractDictUpdate.py
#  line 4: transaction code change to "Type"
#  All if-statements - change to journal/buy/sell

## Next: contractDictUpdates - amount for buys