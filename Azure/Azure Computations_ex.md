Extra note for examples an additional concepts in the wide [[Azure Computations]] concept.

How to create a compute instance with the python SDK:
#### Compute instance:

```python
from azure.ai.ml.entities import ComputeInstance

ci_basic_name = "basic-ci-12345"
ci_basic = ComputeInstance(
    name=ci_basic_name, 
    size="STANDARD_DS3_v2"
)
ml_client.begin_create_or_update(ci_basic).result()
```

Some actions that can be done while in a computing instance:

- Assign to user
- Minimize compute time
- Run. (You need an application that can host notebooks) The easiest way is through the integrated notebooks experience in the Azure ML Studio.

#### Compute cluster: 

```python
from azure.ai.ml.entities import AmlCompute 

cluster_basic = AmlCompute( name="cpu-cluster", type="amlcompute", size="STANDARD_DS3_v2", location="westus", min_instances=0, max_instances=2, idle_time_before_scale_down=120, tier="low_priority", ) ml_client.begin_create_or_update(cluster_basic).result()
```

Link to docs: (https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.entities.amlcompute)

There are scenarios in which you can use this:

- Running a pipeline job you built in the designer.
- Running automated ML job. 
- Running a script as a job.

You can use the API to feed commands with the syntax:

```python
from azure.ai.ml import command

# configure job
job = command(
    code="./src",
    command="python diabetes-training.py",
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
    compute="cpu-cluster",
    display_name="train-with-cluster",
    experiment_name="diabetes-training"
    )

# submit job
returned_job = ml_client.create_or_update(job)
aml_url = returned_job.studio_url
print("Monitor your job at", aml_url)
```

The abstractions are pretty self-explanatory.


