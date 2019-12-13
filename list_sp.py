import pandas as pd

data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table = data[0]
#table.head()
#corrected_table = table.rename(columns=header)
#corrected_table
tickers = table['Symbol'].tolist()
print (tickers)