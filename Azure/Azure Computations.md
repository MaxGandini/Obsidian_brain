Below is a diagram of a typical ML workflow and computations in each step of the pipeline:

![[azure_computin.png]]

Compute instance: It's like a virtual machine that is used to run notebooks in the exploration phase

Compute clusters: It's a multi noded cluster of virtual machines that automatically scale up or down to meet demands.
These allow for parallel processing to distribute the workload.

Kubernetes clusters: These are based on the [[Kubernetes]] technology. It gives additional control on the paralellization processing. 

Attached compute: It allows you to attach existing computations like the Azure Virtual machines or the databricks clusters to your workspace

Serverless: Fully managed, on demand compute for training.

### General concepts: 

You would want a different type of computing for different phases:

- For experimentation : Spark - compute instance . A jupyter notebook can be used.
- For production (training) : Using python scripts is recommended, and it will be easier to automate an schedule. You can run scripts as pipeline jobs with a **compute cluster** .
	If it's important that the computation is ready fast *serverless compute* can be used
- For deployment: It depends on if you want batch of real-time predictions.
	Batch: Pipeline job in Azure Machine Learning. It has target computation with clusters and serverless.
	
	Real-time: A benefit is to be gained from a lightweight and more cost efficient compute. Containers ([[Kubernetes]]) are ideal for real time deployments. Azure creates and manages containers to run a model, and kubernetes clusters can be attached to manage the necessary computing.
