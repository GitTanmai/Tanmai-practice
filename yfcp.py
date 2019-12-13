import pandas as pd
import pandas_datareader as pdr
from datetime import datetime
from pathlib import Path

ibm = pdr.data.get_data_yahoo(symbols='IBM', start=datetime(2019, 10, 10), end=datetime.now())

# amz= pdr.data.get_data_yahoo(symbols='AMZN', start=datetime(2000, 1, 1), end=datetime(2012, 1, 1))
#    print(ibm['Adj Close'])
print('Downloaded file:')
# print(amz['Adj Close'])
# join dataframe
# frames =[ibm,amz]
# res = pd.concat(frames)
addr1 = 'C:\\Users\\tmehrotra\\stock_data'
addr2 = datetime.today().date().strftime("%d%m%Y")
addr3 = '.csv'
addr4 = addr1 + addr2 + addr3

ibm.to_csv(addr4, header=True, index=False, encoding="utf-8", date_format='%Y%m%d')

data = pd.read_csv(addr4)

# inserting column with static value in data frame
data.insert(6, "Company", "IBM")
data.insert(7, "Date", datetime.today().date())

# displaying data frame again - Output 2
data.head()

data.to_csv(addr4, header=True, index=False, encoding="utf-8", date_format='%Y%m%d')