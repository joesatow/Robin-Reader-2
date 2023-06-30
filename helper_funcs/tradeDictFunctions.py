from .dataFunctions import getAverages

def getTradeDictUpdate(currentContract):
    averageBuy, averageSell, pctChange = getAverages(currentContract).values() # get averages of final trade info
    buyDate = currentContract['Process Date'] # get buy date here, since we work backward in time for transactions
    
    return {

    }