# EC2 Inventory Tool

A Python-based Infrastructure Automation project that simulates retrieving EC2 instance information from the AWS EC2 `describe_instances()` API response.

## Features

✅ Connect to AWS using boto3
✅ Retrieve live EC2 inventory
✅ Display instance Name, ID, Type, and State
✅ Filter by state
✅ Filter by instance type
✅ Filter by AWS tags
✅ Sort inventory
✅ Export inventory to CSV
✅ Display inventory summary


## Technologies Used

- Python 3
- AWS EC2
- boto3
- AWS CLI
- CSV Module

## Project Structure

```
EC2_Inventory_Tool/
├── ec2_inventory.py
├── ec2_inventory.csv
└── README.md
```

## Prerequisites
```
Before running the project, ensure you have:

Python 3 installed
AWS CLI configured
boto3 installed
IAM user with permissions to describe EC2 instances

Install boto3:

pip install boto3

Verify AWS credentials:

aws configure

```

## How to Run

Clone the repository:

git clone https://github.com/Jeevitha-MC/python-ec2-inventory-tool.git
cd python-ec2-inventory-tool

Run the application:

python ec2_inventory.py

## Author

Jeevitha MC

Aspiring Infrastructure Engineer with experience in Linux, AWS, Python, Terraform, Docker, and Kubernetes.

GitHub: https://github.com/Jeevitha-MC