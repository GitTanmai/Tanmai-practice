import boto3

# Let's use Amazon S3
s3 = boto3.client('s3')
#for bucket in s3.buckets.all():
#    print(bucket.name)
list=s3.list_objects(Bucket='prac-1')['Contents']
for key in list:
    s3.download_file('prac-1', key['Key'], key['Key'])