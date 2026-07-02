# EC2 Inventory Tool

A Python-based Infrastructure Automation project that simulates retrieving EC2 instance information from the AWS EC2 `describe_instances()` API response.

## Features

- Retrieve EC2 inventory from a sample AWS `describe_instances()` response
- List all EC2 instances
- Display Instance ID, Instance Type, and State
- Display total number of EC2 instances
- Parse nested AWS API responses using Python
- Modular Python functions for infrastructure automation

## Technologies Used

- Python 3
- Dictionaries
- Lists
- Functions
- Loops
- AWS EC2 API response structure (sample data)

## Project Structure

```
EC2_Inventory_Tool/
├── ec2_inventory.py
├── sample_data.py
└── README.md
```

## Future Enhancements

- List all EC2 instances
- Count running and stopped instances
- Export inventory to CSV
- Integrate with boto3
- Accept AWS Region as input