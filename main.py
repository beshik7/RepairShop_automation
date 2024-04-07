import requests
from requests.auth import HTTPBasicAuth
import json
import logging
import os


# Setup logging
logging.basicConfig(level=logging.INFO, filename='script.log',
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Acuity API credentials
ACUITY_USER_ID = os.getenv('ACUITY_USER_ID')
ACUITY_API_KEY = os.getenv('ACUITY_API_KEY')

# RepairShopr API credentials
REPAIRSHOPR_API_KEY = os.getenv('REPAIRSHOPR_API_KEY')
REPAIRSHOPR_SUBDOMAIN = 'geeks4mac'

def fetch_acuity_appointments():
    """Fetches appointments from Acuity Scheduling"""
    acuity_url = "https://acuityscheduling.com/api/v1/appointments"
    try:
        response = requests.get(acuity_url, auth=HTTPBasicAuth(ACUITY_USER_ID, ACUITY_API_KEY))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching appointments from Acuity: {e}")
        raise

def create_repairshopr_ticket(appointment):
    """Create a ticket for RepairShopr from an appointment"""
    repairshopr_url = f"https://{REPAIRSHOPR_SUBDOMAIN}.repairshopr.com/api/v1/tickets"
    repairshopr_headers = {
        "X-Api-Key": REPAIRSHOPR_API_KEY,
        "Content-Type": "application/json"
    }

    # Construct the payload with appointment data
    repairshopr_payload = {
        "subject": "New Service Ticket from Acuity",
        "customer_id": appointment.get("client", {}).get("id", ""),
        "issue": appointment.get("notes", ""),
        "appointment_date": appointment.get("datetime", ""),
    }

    try:
        response = requests.post(repairshopr_url, headers=repairshopr_headers, data=json.dumps(repairshopr_payload))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error creating ticket in RepairShopr: {e}")
        raise

def main():
    try:
        appointments = fetch_acuity_appointments()
        for appointment in appointments:
            ticket = create_repairshopr_ticket(appointment)
            logging.info(f"Created ticket: {ticket['id']}")
    except Exception as e:
        logging.exception("An unexpected error occurred during the script execution")

if __name__ == "__main__":
    main()