# import csv
# import openpyxl as px
import pandas as pd
import openpyxl as px

def writeCSV(tradeList):
    df = pd.DataFrame(tradeList)
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='welcome', index=False)
    writer.close()

    wb = px.load_workbook('output.xlsx')
    ws = wb.active

    ws.auto_filter.ref = ws.dimensions

    wb.save('output.xlsx')