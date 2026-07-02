#Import response variable from sample_data.py
from sample_data import response

def get_running_instances(response):
    #Store running instances in a list
    ec2_instances = []

    #Loop through all reservations
    for reservation in response["Reservations"]:
        #Loop through all instances in the reservation
        for instance in reservation["Instances"]:
            if instance["State"]["Name"] == "running":
                ec2_instances.append(
                    {
                        "InstanceId": instance["InstanceId"],
                        "InstanceType": instance["InstanceType"]
                    }

                )
    return ec2_instances

running_instances = get_running_instances(response)
print("Running EC2 Instances:", len(running_instances))
print("-" * 40)

for ec2_instance in running_instances:
    print(f"Instance ID: {ec2_instance['InstanceId']}, Instance Type: {ec2_instance['InstanceType']}")
    print ()