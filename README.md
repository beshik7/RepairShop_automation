# Acuity to RepairShopr Integration Script

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![requests](https://img.shields.io/badge/requests-2.25.1-blue)
![Environment Variables](https://img.shields.io/badge/-Environment%20Variables-green)

This script integrates Acuity Scheduling with RepairShopr by automatically creating service tickets in RepairShopr based on the appointments scheduled in Acuity. It's designed to automate the workflow between scheduling appointments and managing service tickets.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- [requests](https://docs.python-requests.org/en/master/) library
- An Acuity Scheduling account with API access
- A RepairShopr account with API access

### Installation

1. Clone this repository or download the script to your local machine.

    ```sh
    git clone https://github.com/beshik7/g4mScripts.git
    ```

2. Navigate to the script directory.

    ```sh
    cd your-repository-name
    ```

3. Install the required Python packages.

    ```sh
    pip install -r requirements.txt
    ```

### Setting Up Environment Variables

Before running the script, you need to set up the following environment variables with your API credentials:

- `ACUITY_USER_ID`: Your Acuity Scheduling User ID
- `ACUITY_API_KEY`: Your Acuity Scheduling API Key
- `REPAIRSHOPR_API_KEY`: Your RepairShopr API Key
- `REPAIRSHOPR_SUBDOMAIN`: Your RepairShopr subdomain


On macOS or Linux:

```sh
export ACUITY_USER_ID='your_acuity_user_id'
export ACUITY_API_KEY='your_acuity_api_key'
export REPAIRSHOPR_API_KEY='your_repairshopr_api_key'
export REPAIRSHOPR_SUBDOMAIN='your_repairshopr_subdomain'

```
On Windows (using Command Prompt):
```
set ACUITY_USER_ID=your_acuity_user_id
set ACUITY_API_KEY=your_acuity_api_key
set REPAIRSHOPR_API_KEY=your_repairshopr_api_key
set REPAIRSHOPR_SUBDOMAIN=your_repairshopr_subdomain
```
### Running the Script

After setting up the environment variables, you can run the script with:
```
python main.py
```

### How It Works

The script fetches the latest appointments from Acuity Scheduling and creates corresponding service tickets in RepairShopr. It uses the Acuity API to retrieve appointment details and the RepairShopr API to create tickets.

### Contributing

Contributions are welcome! If you have ideas for improvements or new features, please feel free to fork the repository and submit a pull request.

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.
