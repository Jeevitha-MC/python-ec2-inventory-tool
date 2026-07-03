# EC2 Inventory Tool

A Python-based Infrastructure Automation project that simulates retrieving EC2 instance information from the AWS EC2 `describe_instances()` API response.

## Features

- Parse AWS EC2 `describe_instances()` response (using sample data)
- Display complete EC2 inventory
- Display Instance ID, Instance Type, and State
- Generate an EC2 inventory summary
  - Total Instances
  - Running Instances
  - Stopped Instances
- Refactor inventory printing into reusable function
- Filter Instances by State(Refactoring)
- Export Inventory to CSV
- Built using modular Python functions


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