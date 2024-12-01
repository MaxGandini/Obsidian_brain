import os
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

sub_id = os.getenv("subscription_id")
resource_group = os.getenv("resource_group")
workspace_name = os.getenv("workspace_name")

ml_client = MLClient(
DefaultAzureCredential(),sub_id,resource_group,workspace_name
)

from azure.ai.ml import command

# This is how you configure a job through the SDK:

job = command(
        code="/.src",
        command="python train.py",
        environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
        compute="aml-cluster",
        experiment_name="train-model"
)

returned_job = ml_client.create_or_update(job)
