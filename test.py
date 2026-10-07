import pandas as pd

xlsx = pd.ExcelFile("Music.xlsx")

print(xlsx.sheet_names)