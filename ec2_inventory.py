#Import response variable from sample_data.py
import boto3
import csv

#Create an EC2 client
ec2 = boto3.client("ec2")

response = ec2.describe_instances()

print(response["Reservations"][0]["Instances"][0]["Tags"])

print(type(response))
print(response.keys())

def get_all_instances(response):
    #Store all instances in a list
    ec2_instances = []

    #Loop through all reservations
    for reservation in response["Reservations"]:
        #Loop through all instances in reservation
        for instance in reservation["Instances"]:
            name ="N/A"
            for tag in instance.get("Tags", []):
                if tag["Key"] == "Name":
                    name = tag["Value"]
            ec2_instances.append(
                {"Name" : name,
                "InstanceId" : instance["InstanceId"],
                "InstanceType" : instance["InstanceType"],
                "State" : instance["State"]["Name"],
                "Tags": instance.get("Tags", [])}
            )
    return ec2_instances
all_instances = get_all_instances(response)
print(all_instances[0])
print("EC2 Inventory")
print(f"Total Instances: {len(all_instances)}")
print("-" * 40)
for ec2_instance in all_instances:
    print(f"Name: {ec2_instance['Name']}, Instance ID: {ec2_instance['InstanceId']}, Instance Type: {ec2_instance['InstanceType']}, State: {ec2_instance['State']}")
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
    print(f"Name         : {instance['Name']}")
    print(f"Instance ID  : {instance['InstanceId']}")
    print(f"Type         : {instance['InstanceType']}")
    print(f"State        : {instance['State']}")
    print()

#----------------------------------------------
#Refactor the code to print the inventory in a more structured way
def print_inventory(instances, title):
    print(title)
    print("-" * 40)
    if len(instances) == 0:
        print("No instances found.")
        print()
        return
    for instance in instances:
        print(f"Name         : {instance['Name']}")
        print(f"Instance ID  : {instance['InstanceId']}")
        print(f"Type         : {instance['InstanceType']}")
        print(f"State        : {instance['State']}")
        print()
    
print_inventory(all_instances, "EC2 Inventory")
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

#------------------------------------------------------
#Export Inventory to CSV
def export_inventory_to_csv(instances, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file) #writes csv rows to the file
        writer.writerow(["InstanceID", "InstanceType", "State"]) #It's a list, each item becomes a seperate column
        for instance in instances:
            writer.writerow([instance["InstanceId"], instance["InstanceType"], instance["State"]]) #Each list item becomes one CSV column

export_inventory_to_csv(all_instances, "ec2_inventory.csv")
print("EC2 Inventory exported to ec2_inventory.csv")

#------------------------------------------------------
#Sorting Instances
def sort_instances(all_instances, key):
    return sorted(all_instances, key=lambda x: x[key]) #sorting whatever the caller gives as key, in this case InstanceType

sorted_by_type = sort_instances(all_instances, "InstanceType")
sorted_by_state = sort_instances(all_instances, "State")
print_inventory(sorted_by_type, "EC2 Inventory Sorted by Instance Type")
print_inventory(sorted_by_state, "EC2 Inventory Sorted by State")

#------------------------------------------------------
#Filter Instances by Tag
def get_instances_by_tag(all_instances, tag_key, tag_value):
    filtered_instances = []
    for instance in all_instances:
        for tag in instance.get("Tags", []):
            if tag["Key"] == tag_key and tag["Value"] == tag_value:
                filtered_instances.append(instance)
                break #Break the inner loop if a matching tag is found
    return filtered_instances


prod_instances = get_instances_by_tag(all_instances, "Environment", "Production")
print_inventory(prod_instances, "Production EC2 Instances")


