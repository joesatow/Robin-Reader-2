def filterData(list):
    filteredAccountActivityList = [x for x in list if isCorrectSecurityType(x)]
    return filteredAccountActivityList

# function for use in filtering accountActivityList.
# get rid of anything that isnt an option
def isCorrectSecurityType(str):
    securityType = str['Security Type']
    if securityType == 'Option':
        return True

