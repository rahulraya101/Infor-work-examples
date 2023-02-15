import boto3
from pprint import PrettyPrinter
import sys


#create session: In python we call the environment (stage, ade,dde etc) in create session code. 
#with this we login to aws console browser
session = boto3.Session(profile_name="dde", region_name="us-east-1")
#sys.exit()
#create service client: with this we login to the ec2 client.
#label the client 
ec2_client = session.client("ec2")

#how do we list those buckets on python code?
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client
#in describe_instances cmd takes the args

response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Product',
            'Values': [
                'hms',          #this describes the instances that are tag:product with a value of hms
            ]
        },
    ]   #this pics all the owner tags.
#        InstanceIds=[
#           'i-03cb8d6c6f0c91fff',
#           ' i-064e163a87f10665a'
#
#       ]
)
   
pp = PrettyPrinter()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        for Tag in instance['Tags']:
            if Tag["Key"] == "Owner":
                #True when the current tag being looped through is "Owner"
                owner_val = Tag["Value"] #Set value to variable
            if Tag["Key"] == "Name":
                #True when the current tag being looped through is "Name"
                name_val = Tag["Value"] #Set value to variable
        state_val = instance["State"]["Name"] #Retrieve state value from instance dictionary

        #ATTEMPT TO PRINT TO TXT FILE  https://realpython.com/read-write-files-python/
        with open('owner-report.txt', 'a') as file:
            file.write("Name: " + name_val + ", Owner: " + owner_val + ", State: " + state_val)
        
#sys.exit()
            #if Tag['Key'] == "Owner":
                #print(Tag['Value'])    #need to filter the value if it is the correct email format.
# upload to s3
#create service client: with this we login to the s3 client.
#label the client 
s3_client = session.client("s3")

#how do we list those buckets on python code?
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#client
#in list_objects cmd takes the args

response = s3_client.put_object(
    Bucket='infor-dde-dev-appdata-us-east-1',
    Key = 'hms/ops/rahul'
    )

print(response)
