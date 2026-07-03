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
#-------------------------------------------------------------------------

def get_all_instances(response):
    #Store all instances in a list
    ec2_instances = []

    #Loop through all reservations
    for reservation in response["Reservations"]:
        #Loop through all instances in reservation
        for instance in reservation["Instances"]:
            ec2_instances.append(
                {"InstanceId" : instance["InstanceId"],
                "InstanceType" : instance["InstanceType"],
                "State" : instance["State"]["Name"]}
            )
    return ec2_instances
all_instances = get_all_instances(response)
print("EC2 Inventory")
print(f"Total Instances: {len(all_instances)}")
print("-" * 40)
for ec2_instance in all_instances:
    print(f"Instance ID: {ec2_instance['InstanceId']}, Instance Type: {ec2_instance['InstanceType']}, State: {ec2_instance['State']}")
    print ()
#------------------------------------------------------------------------------

#Function to count number of instances running and stopped
def get_instance_summary(all_instances):
    total = len(all_instances)
    running = 0
    stopped = 0

    for instance in all_instances:
        if instance["State"] == "running":
            running += 1
        elif instance["State"] == "stopped":
            stopped += 1

    return {
        "Total": total,
        "Running": running,
        "Stopped": stopped
    }
summary = get_instance_summary(all_instances)
print("EC2 Inventory Summary")
print("-" * 40)
print(f"Total Instances   : {summary['Total']}")
print(f"Running Instances : {summary['Running']}")
print(f"Stopped Instances : {summary['Stopped']}")
print("-" * 40)
print()
#-------------------------------------------------------------------------

#Filter Instances by Type
def get_instances_by_type(all_instances, instance_type):
    filtered_instances = []
    for instance in all_instances:
        if instance["InstanceType"] == instance_type:
            filtered_instances.append(instance)#if instance matched the requested type, append the existing dictionary
    return filtered_instances

micro_instances = get_instances_by_type(all_instances, "t3.micro")
print(f"Total Micro Instances: {len(micro_instances)}")
print("-" * 40)
for instance in micro_instances:
    print(f"Instance ID  : {instance['InstanceId']}")
    print(f"Type         : {instance['InstanceType']}")
    print(f"State        : {instance['State']}")
    print()

#----------------------------------------------
#Refactor the code to print the inventory in a more structured way
def print_inventory(instances, title):
    print(title)
    print("-" * 40)
    for instance in instances:
        print(f"Instance ID  : {instance['InstanceId']}")
        print(f"Type         : {instance['InstanceType']}")
        print(f"State        : {instance['State']}")
        print()
    
print_inventory(all_instances, "EC2 Inventory")
#print_inventory(running_instances, "Running EC2 Instances")
print_inventory(micro_instances, "Micro EC2 Instances")
print()

#------------------------------------------------------

#Filter Instances by State(Refactoring)
def get_instances_by_state(all_instances, state):
    filtered_instances = []
    for instance in all_instances:
        if instance["State"] == state:
            filtered_instances.append(instance)
    return filtered_instances
running_instances = get_instances_by_state(all_instances, "running")
stopped_instances = get_instances_by_state(all_instances, "stopped")
print_inventory(running_instances, "Running EC2 Instances")
print_inventory(stopped_instances, "Stopped EC2 Instances")