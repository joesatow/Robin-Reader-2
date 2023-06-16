# function to fix amounts
def fixAmount(str):
    amount = str.replace('$','').replace(',','')
    if '(' in amount:
        amount = amount.replace('(','').replace(')','')
        amount = float(amount)
        amount = -amount
    amount = float(amount)
    return amount

def getUniqueVals(transCode, data):
    # OEXP = option expiration
    # we'll need to get description, ticker, and quantity values differently if we're reading from a OEXP transaction code, because this is just the way Robinhood provided the data.
    # these transactions will act the same as a 'sell'.  example: 10 contracts expired acts as 10 contracts sold for 0 dollars. 
    # this is necessary for netting out quantity, since there's no STC transactions for some trades if you let them expire worthless.
    if transCode == 'OEXP':
        description = data['Description'].replace('call','Call').replace('put','Put').replace('Option Expiration for ', '')
        ticker = description.split(' ')[0]
        quantity = -int(data['Quantity'].replace('S','')) # quantity here is how many contracts expired.  
        amount = 0 # 0 because the option expired worthless, equivalent to selling for 0 dollars.
        letExpire = True
    else: # standard BTO or STC data
        description = data['Description']
        quantity = int(data['Quantity'])
        amount = fixAmount(data['Amount'])
        ticker = data['Instrument']
        letExpire = False

    return {
        "description": description, 
        "ticker": ticker,
        "quantity": quantity, 
        "amount": amount
    }
