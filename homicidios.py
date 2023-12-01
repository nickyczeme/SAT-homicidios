import pandas as pd

file = pd.ExcelFile('./homicidios.xlsx')
df = pd.read_excel(file, 'HECHOS')

print(df.head(5))
