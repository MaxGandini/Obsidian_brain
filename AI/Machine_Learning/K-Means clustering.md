Example of [[Unsupervised-Learning]] . It takes *K* as a hyper parameter.

Optimization P: Minimization of the sum of square distances with respect to a group center.
![[Flow-chartflow_chart.jpg]]

Graphical representation of clusters and their optimized centroids. The center is first positioned randomly and then through a metric (generally euclidian), the distance squared is minimized in every iteration. 

![[Cluster_graph.png]]

The algorithm that [[Sci-Kit Learn]] uses by default is called [[k-means++]] in a variant called "greedy k-means++" which is supposed to accelerate the convergence of the model.
It also takes a parameter "n_clusters" it has to be an integer and defines de amount of centroids.
[[k-means-example]].