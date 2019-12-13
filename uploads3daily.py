import boto3
from datetime import datetime
import re
import os
import pandas as pd
import csv
import psycopg2
import pandas_datareader as pdr
from datetime import datetime
from datetime import timedelta
from pathlib import Path

#---------------------------------------------------------------------------------
#variable definitions
#var1 -> contains file name
#listoffiles -> conatin list of files
#dir_path -> contains file path

#dfObj -> dataframe which contains stock details for all the tickers
#tickers -> contains all S&P500 companies name
#addr4 -> complete name of file. addr1, addr2, addr3 contains partial name
#----------------------------------------------------------------------------------
def searchfile():
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = 'C:\\Users\\tmehrotra'
    s3name = 'uploadprac'
    st = 'stock_data'

    listoffiles = os.listdir(dir_path)
    #print(listoffiles)
    # quit()
    # search for filename of same date

    listToStrlocal = ' '.join(listoffiles)  #convert file list to string to avoid looping

    str = st + (datetime.today().date().strftime("%d%m%Y"))   #generating file name dynamically
#    fl = re.search(^str, file)
#    fll = re.search((datetime.today().date().strftime("%d%m%Y")),fl)
    var1 = st + datetime.today().date().strftime("%d%m%Y") + '.csv'
    if var1 in listToStrlocal:

        addr1 = dir_path

        upl(var1, dir_path, s3name)
    else:
        dwdata()
        upl(var1, dir_path, s3name)

# download file for current data from yahoo finance

def dwdata():
    dfObj = pd.DataFrame(columns=['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close','Ticker','Date'])
    # get list of all s&p 500 companies
    data1 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    table = data1[0]
    tickers = table['Symbol'].tolist()

    for i in tickers:

        try:
            #print(i)
            pdticker = pdr.get_data_yahoo(symbols=i, start=datetime.today().date())
            #ibm = pdticker.insert(6, "Company", i)
            pdticker['Ticker'] = i
            pdticker['Date'] = pdticker.index
            print(i)
            print('dfObj',dfObj)
        #ibm = pdr.get_data_yahoo(symbols='IBM', end=datetime.now())
            dfObj = dfObj.append(pdticker, sort=False)
            print(dfObj)
        except KeyError:
            pass
        #except ChunkedEncodingError:
         #  pass
        #except:
         #   pass
#    dfObj.reset_index(drop=True)

    # print(amz['Adj Close'])

    addr1 = 'C:\\Users\\tmehrotra\\stock_data'
    addr2 = datetime.today().date().strftime("%d%m%Y")
    addr3 = '.csv'
    addr4 = addr1 + addr2 + addr3

    dfObj.to_csv(addr4, header=True, encoding="utf-8",index=False)
    print('Downloaded file:')


#below function use to update data in database
def upldb(key2):
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=admin")
    cur = conn.cursor()
    with open(key2, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
        for row in reader:
            cur.execute(
                "INSERT INTO COMPANY(High,Low,Open,Close,Volume,Adj_Close,Company_Name,Date_Inserted) VALUES (%s,%s, %s, %s, %s,%s,%s,%s )",
                row
            )
            conn.commit()
    print('File value uploaded in database')

def upl(ky, ad1, s3name):
    #    bucketName = "Your S3 BucketName"
    #    Key = "Original Name and type of the file you want to upload into s3"
    #    outPutname = "Output file name(The name you want to give to the file after we upload to s3)"
    #key2= variable store address with file name
    #ky filename
    #ad1 directory path
    key2 = ad1 + '\\' + ky

    # verify if file already exist on S3
    s3 = boto3.client('s3')
    # searching the file in S3 by converting the list into string
    listToStr = ' '.join([str(elem) for elem in s3.list_objects(Bucket=s3name)['Contents']])

#        for obj in s3.list_objects(Bucket=s3name)['Contents']:

    if re.search(ky, listToStr):
        print("File already exist in S3")
#                s3.upload_file(key2, s3name, ky)
#                print('upload', key2)

    else:
        upldb(key2)
        s3.upload_file(key2, s3name, ky)
        print('Uploaded file:')



# call search file function for today's file
searchfile()