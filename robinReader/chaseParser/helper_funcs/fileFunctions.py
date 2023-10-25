import csv
import os
import glob

def getData():
    path = os.getcwd()
    extension = 'csv'
    os.chdir(path)
    result = glob.glob('*.{}'.format(extension))
    activityFile = result[0]

    with open(activityFile) as f:
        reader = csv.DictReader(f)
        data = list(reader)

    return data 