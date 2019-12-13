import boto3
from datetime import datetime
import re
import os
#get path
#dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path ='C:\\Users\\tmehrotra'
s3name ='uploadprac'


#search for filename of same date
for root, dirs,files in os.walk(dir_path,topdown=False):
#    print("dir ", dirs)
#    print("root ",root)
    for file in files:
#        print("file ",file)
        fl = re.search('\d{8}', file)

# re.search would pass null if there is no match
        if fl is None:
            pass
        else:
            if fl.group() == datetime.today().date().strftime("%d%m%Y"):
#                print(file) printing filename if file exist of same date
                var1= file
                addr1= root
#                print(dirs)
#                print(root)
