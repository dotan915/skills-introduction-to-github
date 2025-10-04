from bs4 import BeautifulSoup
with open("../datasets/SalesTransactions.xml", "r", encoding="utf-8") as f:
    data=f.read()
bs_data=BeautifulSoup(data,'xml')
Uelsample=bs_data.find_all('Uelsample')
print(Uelsample)
