import boto3
#Create an EC2 client
ec2 = boto3.client("ec2")

aws_response = ec2.describe_instances()
