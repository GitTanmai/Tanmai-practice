import boto3
from datetime import datetime
import re


fl=input("Enter filename ")
print(re.search('\d{8}', fl) )
print(datetime.today().date().strftime("%d%m%Y"))
mat= re.search('\d{8}', fl)

if re.search('\d{8}', fl).group() == datetime.today().date().strftime("%d%m%Y"):
    print('inside if')
#function to download file from S3
    def dwn(key):
# Let's use Amazon S3
        s3 = boto3.client('s3')

#for bucket in s3.buckets.all():
#    print(bucket.name)

#	list=s3.list_objects(Bucket='prac-1')['Contents']
        s3.download_file('prac-1', key , key)
        print('down')

# function to upload file into s3
    def upl(key):
        bucketName = "Your S3 BucketName"

#    Key = "Original Name and type of the file you want to upload into s3"
#    outPutname = "Output file name(The name you want to give to the file after we upload to s3)"

        s3 = boto3.client('s3')
        s3.upload_file(key, 'uploadprac',key)
        print('upload')

    upl(fl)
# file name
else:
    print('inside else')

