from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.ai.ml import MLClient

import os

sub_id = os.getenv("subscription_id")
resource_group = os.getenv("resource_group")
workspace_name = os.getenv("workspace_name")

ml_client = MLClient(
DefaultAzureCredential(),sub_id,resource_group,workspace_name
)

# import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

# load the diabetes dataset
from pathlib import Path

grandparent_dir= Path(__file__).parents[3]

# Define the path to the directory containing the dataset (not the file itself)
data_dir = grandparent_dir / "datasets"  # This should be the directory containing Housing.csv

tables=[]
names=[]
# Check if the directory exists and then list its contents

if data_dir.exists() and data_dir.is_dir():
    for archive in data_dir.iterdir():
        print(archive)
        tables.append(archive)

else:
    print(f"{data_dir} is not a valid directory.")

csv_files = list(data_dir.glob("*.csv"))

# Print out each CSV file name
for csv_file in csv_files:
    print(csv_file.name)  # This will print just the file name, not the full path
    names.append(csv_file.name.split('.')[0])

print("Loading Data...")
diabetes = pd.read_csv(csv_files[0])

# separate features and labels
X, y = diabetes[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness','SerumInsulin','BMI','DiabetesPedigree','Age']].values, diabetes['Diabetic'].values

# split data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# set regularization hyperparameter
reg = 0.01

# train a logistic regression model
print('Training a logistic regression model with regularization rate of', reg)
model = LogisticRegression(C=1/reg, solver="liblinear").fit(X_train, y_train)

# calculate accuracy
y_hat = model.predict(X_test)
acc = np.average(y_hat == y_test)
print('Accuracy:', acc)

# calculate AUC
y_scores = model.predict_proba(X_test)
auc = roc_auc_score(y_test,y_scores[:,1])
print('AUC: ' + str(auc))

from azure.ai.ml import command

# configure job
job = command(
    code=os.path.dirname(os.path.realpath(__file__)),
    command="python diabetes-training.py",
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
    compute="aml-cluster",
    display_name="diabetes-pythonv2-train",
    experiment_name="diabetes-training"
)

# submit job
returned_job = ml_client.create_or_update(job)
aml_url = returned_job.studio_url
print("Monitor your job at", aml_url)
