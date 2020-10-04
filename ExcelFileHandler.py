import pandas as pd
file = pd.ExcelFile('/Users/mrskumar/Downloads/sales.xlsx')
print(file.sheet_names)
sheet = file.parse('sales')
print(sheet)
print(sheet.Amount.sum())
print(sheet.loc[sheet['Amount'] > 2000])
