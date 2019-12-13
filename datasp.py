import boto3
from datetime import datetime
import re
import os
import pandas as pd
import csv
import psycopg2
import pandas_datareader as pdr
from datetime import datetime
from pathlib import Path


def dwdata():
    dfObj = pd.DataFrame(columns=['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close','Ticker','Date'])
    # get list of all s&p 500 companies
    data1 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    table = data1[0]
    tickers = table['Symbol'].tolist()

    for i in tickers:

        try:
            pdticker = pdr.get_data_yahoo(symbols=i, end=datetime.now())
            #ibm = pdticker.insert(6, "Company", i)
            pdticker['Ticker'] = i
            pdticker['Date'] = pdticker.index

            print(i)
        #ibm = pdr.get_data_yahoo(symbols='IBM', end=datetime.now())
            dfObj = dfObj.append(pdticker, sort=False)
            #print(dfObj)
        except KeyError:
            pass
        #except ChunkedEncodingError:
         #   pass
        #except:
         #   pass


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

    dfObj.to_csv(addr4, header=True, encoding="utf-8",index=False)

dwdata()

