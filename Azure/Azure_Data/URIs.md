A URI (Uniform Resource Identifier) references the location of your data. For Azure Machine Learning to connect to your data, you need to prefix the URI with the appropriate protocol. There are three common protocols when working with data in the context of Azure Machine Learning.

![[uri.png]]

- http(s): Use for data stores publicly or privately in an Azure Blob Storage or publicly available http(s) location.
- abfs(s): Use for data stores in an Azure Data Lake Storage Gen 2.
- azureml: Use for data stored in a datastore.

A datastore is a reference to an existing storage account on Azure. Therefore, when you refer to data stored in a datastore, you may be referring to data being stored in an Azure Blob Storage or Azure Data Lake Storage. When you refer to the datastore however, you won't need to authenticate as the connection information stored with the datastore will be used by Azure Machine Learning.

In Azure Machine Learning, datastores are abstractions for cloud data sources. They encapsulate the information needed to connect to data sources, and securely store this connection information so that you don’t have to code it in your scripts.