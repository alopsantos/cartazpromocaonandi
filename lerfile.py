import pandas as pd 

produtos = pd.read_excel('produtos.xlsx', engine='openpyxl')

for i, row in produtos.iterrows():
  print(row.MARCA)