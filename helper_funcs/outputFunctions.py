import csv

# field names for CSV output file
fields = ['ticker', 'contractDescription', 'contracts', 'averageBuy', 'totalBuy', 'averageSell', 'totalSell', 'pctChange', 'net', 'buyDate', 'buyDateDayOfWeek', 'sellDate', 'sellDateDayOfWeek', 'daysHeld', 'letExpire'] 

# output path
path = 'output.csv'

def writeCSV(tradeList):
    with open(path, 'w', newline='') as file: 
        writer = csv.writer(file)
        writer.writerow(['Ticker', 'Description', 'Contracts', 'Average Buy', 'Total Buy', 'Average Sell', 'Total Sell', 'Percent Change', 'Net', 'Buy Date', 'Day', 'Sell Date', 'Day', 'Days Held', 'Let Expire?'])

        writer = csv.DictWriter(file, fieldnames = fields)
        writer.writerows(tradeList)