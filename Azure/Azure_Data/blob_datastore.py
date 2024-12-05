import os
from azure.ai.ml import MLClient
from azureml.core import Datastore
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient
from azureml.data.azure_storage_datastore import AzureBlobDatastore 
from azure.ai.ml.entities import AccountKeyConfiguration

id = os.getenv("azure_key")

# Define the datastore configuration
blob_datastore = AzureBlobDatastore(
    name="blob_example",
    account_name="mytestblobstore",
    container_name="data-container",
    credentials=AccountKeyConfiguration(
        account_key= id # Replace with your actual key
    ),
)

print(f"Datastore {blob_datastore.name} created successfully.")
connection_string = "your_connection_string"  # Replace with your connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "data-container"
container_client = blob_service_client.get_container_client(container_name)

