import pandas as pd
df = pd.read_csv(r"../datasets/SalesTransactions.txt",sep="\t", encoding="utf-8")
print(df.head())

import pandas as pd
df = pd.read_csv(r"../datasets/SalesTransactions.csv", encoding="utf-8", dtype='unicode', lowmemory=False)
print(df.head())

import pandas as pd
df = pd.read_csv(r"../datasets/SalesTransactions.json", encoding="utf-8", dtype='unicode')
print(df.head())

from bs4 import BeautifulSoup
with open("../datasets/SalesTransactions.xml", "r", encoding="utf-8") as f:
    data=f.read()
bs_data=BeautifulSoup(data,'xml')
Uelsample=bs_data.find_all('Uelsample')
print(Uelsample)

import pandas_read_xml as pdx

df = pdx.read_xml("../datasets/SalesTransactions.xml", ['UelSample', 'SalesItem'])
print(df)
print(df.iloc[0])
data = df.iloc[0]

print(data[0])
print(data[1])
print(data["OrderID"])

import pandas as pd
datafame=pd.read_excel("../datasets/SalesTransactions.xlsx")
print(datafame)