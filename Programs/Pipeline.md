A pipeline is a concept in programming that systematizes the application of different operations to a certain input data.
examples:
- [[pipeline.py]]
- [[linear_regression1.py]]

![[pipe.png]]

The image above is an oversimplification, and there are many ways to conceive this loop as a straight line with the loop in the middle. 
The main takeaway here, is that one can use an [[API]] like the one defined in [[Sci-Kit Learn]] to generate pipelines in a codebase. 

This way, users can get a diagramatical representation of the transformations applied to the input data, so any problem can be easily trackable.

From [[Azure Machine Learning]] :

A pipeline is a workflow of a complete machine learning task that can include data preparation, training, testing, and deployment. Pipelines have many uses. You can make a pipeline that trains models, makes predictions in real-time, or one that only cleans data. Because each step in a pipeline is independent, multiple people can work on different steps within the same pipeline at once. Azure Machine Learning Pipelines can save you time by only rerunning steps whose inputs have changed—drastically reducing runtimes if you're simply tweaking hyperparameters or other steps. Both Azure Data Factory and Azure Pipelines provide out-of-the-box pipelines for Azure Machine Learning, so you can focus on machine learning instead of infrastructure.
