The data is not stored in the workspace. All the data is stored in Datastores which are refence to the Azure Data services. The connection info to a data service is stored in the azure key vault.

- `workspaceartifactstore` : Connects to `azureml` container of the Azure storage account created with the workspace.
- `workspaceworkingdirectory`: Connects to the file share of the Azure storage account created with the workspace used by the *notebook* section of the studio. Any upload is uploaded to this file share.
- `workspaceblobstore`: Connects to Blob storage of the account created with the workspace. `Azureml-blobstore` set as the default datastore.
- `workspacefilestore`: Connects to the file share of the Azure storage account created with the workspace. `azureml-filestore`



