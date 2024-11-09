from google.cloud import bigquery
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the GOOGLE_APPLICATION_CREDENTIALS variable
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Use the credentials in your BigQuery client
client = bigquery.Client.from_service_account_json(credentials_path)

# Now you can interact with BigQuery
