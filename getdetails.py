from collections import defaultdict
import boto3
"""
A tool for retrieving basic information from the running EC2 instances.
"""
# Connect to EC2
print("-----------------------------------------------------------------")
print("-----------------      EC2 Details       -------------------------")
print("-----------------------------------------------------------------")
ec2 = boto3.resource('ec2')
# Get information for all running instances
running_instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running','stopped']}])
ec2info = defaultdict()
for instance in running_instances:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    # Add instance info to a dictionary         
    ec2info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        'Launch Time': instance.launch_time
        }
attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
for instance_id, instance in ec2info.items():
    for key in attributes:
        print("{0}: {1}".format(key, instance[key]))
    print("------")
# Connect to S3
s3_resource = boto3.resource('s3')
print("-----------------------------------------------------------------")
print("-----------------      S3 Details       -------------------------")
print("-----------------------------------------------------------------")
# Get information for all running instances and print
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print (bucket.name)
print("-----------------------------------------------------------------")
print("-----------------      RDS Details      -------------------------")
print("-----------------------------------------------------------------")
# Connect to RDS
client = boto3.client('rds')
response = client.describe_db_instances()
# Get information for all running instances and print
for db_instance in response['DBInstances']:
        db_instance_name = db_instance['DBInstanceIdentifier']
        db_type = db_instance['DBInstanceClass']
        db_storage = db_instance['AllocatedStorage']
        db_engine =  db_instance['Engine']
        print ("Name:",db_instance_name)
        print ("DB Type:",db_type)
        print ("AllocatedStorage:",db_storage)
        print ("DB Engine:",db_engine)
        print("------")