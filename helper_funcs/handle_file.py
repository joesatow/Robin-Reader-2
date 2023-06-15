import csv
import os
import glob

def getData():
    path = os.getcwd()
    extension = 'csv'
    os.chdir(path)
    result = glob.glob('*.{}'.format(extension))
    activityFile = result[0]

    file = open(activityFile, "r")
    data = list(csv.reader(file, delimiter=','))
    file.close()

    # Return everything but first row and last 2 rows
    # First row is headers, last two rows are robinhood text, not data we want 
    return data[1:-2] 