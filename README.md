# EC2 Inventory Tool

A Python-based Infrastructure Automation tool that connects to AWS using boto3 to retrieve live EC2 inventory, filter resources, generate summaries, and export reports.
This project demonstrates practical Infrastructure Engineering skills by interacting with AWS APIs, processing cloud resources, and automating inventory management.
## Architecture

<img width="1536" height="1024" alt="EC2_Inventory_Tool" src="https://github.com/user-attachments/assets/aa6fb05d-17a4-4a81-a98c-9e572b237355" />

## Features

• Retrieve live EC2 inventory using AWS SDK (boto3)
• Display EC2 Name, Instance ID, Instance Type, and State
• Generate an inventory summary
• Filter instances by:
	• State
	• Instance Type
	• AWS Tags
• Sort EC2 instances
• Export inventory to CSV
Handle instances without Name tags gracefully


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

## What I Learned

This project helped me gain practical experience with:

AWS EC2 APIs using boto3
Infrastructure automation with Python
Working with nested JSON responses
Processing lists and dictionaries
Building reusable Python functions
Tag-based resource filtering
CSV report generation
AWS CLI configuration and authentication

## Author

Jeevitha MC

Aspiring Infrastructure Engineer with experience in Linux, AWS, Python, Terraform, Docker, and Kubernetes.

GitHub: https://github.com/Jeevitha-MC
