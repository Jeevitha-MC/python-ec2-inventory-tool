# EC2 Inventory Tool

A Python-based Infrastructure Automation project that simulates retrieving EC2 instance information from the AWS EC2 `describe_instances()` API response.

## Features

- List running EC2 instances
- Display Instance ID and Instance Type
- Parse nested AWS API responses
- Demonstrates Python automation concepts used in Infrastructure Engineering

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