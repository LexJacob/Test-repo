import boto3

#variable = what session (profilename='your profile name')
session = boto3.Session(profile_name='ljacob') #provide us with security credential to be able to run commands

s3 = session.client('s3')

# print(s3.list_buckets())

buckets_list = s3.list_buckets()['Buckets']

print(buckets_list) # prints just the bucket list
print('-------------------------------------------------------------------------')

def display_names():
    for bucket in buckets_list()['Buckets']:
        print(bucket['Name']) # ['Name'] -- will only print names in the bucket
    print('----------------------------------------------------------------------')

def create_s3(name, region):
    if (region != "us-east-1"):
        s3.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={
                'LocationConstraint': region,
            },
        )
    else:
        s3.create_bucket(
            Bucket=name,
        )

def put_item(filename, bucketname):
    s3.put_object(
        Body='filename',
        Bucket='bucketname',
        Key='filename',
    )
    print(response)

put_item('test.txt', 'ljacob-demo')
    

# display_names()

# create_s3("ljacob-demo", "us-east-1")