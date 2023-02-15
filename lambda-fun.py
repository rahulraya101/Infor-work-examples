import boto3
session = boto3.Session(profile_name="dde", region_name="us-east-1")

ec2_client = session.client("ec2")
stoppedInstances = ec2_client.describe_instances(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': ['stopped']
                }
            ]
        )

with open("instance-list.txt", "w") as f:
    for instance in stoppedInstances['Reservations']:
        for instance_id in instance['Instances']:
            print(instance_id['InstanceId'])
            f.write(f"{instance_id['InstanceId']}\n")

    print("done")
