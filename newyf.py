import os
import pandas_datareader as pdr
from datetime import datetime

#ibm = pdr.data.get_data_yahoo(symbols='IBM', start=datetime(2019, 10, 10), end=datetime.now())
ibm=pdr.get_data_yahoo('AAPL', end=datetime.now())

print(ibm)

addr1 = 'C:\\Users\\tmehrotra\\stock_data'
addr2 = datetime.today().date().strftime("%d%m%Y")
addr3 = '.csv'
addr4 = addr1 + addr2 + addr3
ibm.to_csv(addr4, header=True, encoding="utf-8")



data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table = data[0]
table.head()

sliced_table = table[1:]
header = table.iloc[0]

corrected_table = sliced_table.rename(columns=header)
corrected_table


tickers = corrected_table['Ticker symbol'].tolist()
print (tickers)