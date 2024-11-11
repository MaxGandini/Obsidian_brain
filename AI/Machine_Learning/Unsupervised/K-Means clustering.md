Example of [[Unsupervised-Learning]] . It takes *K* as a hyper
parameter, which is an integer. It is used to classify unknown categories in data.
IE:
- [[k-means-example]].
- [[k_means1.py]]
## How K-Means Works

![[Flow-chartflow_chart.jpg]]

1. **Initialization**: 
   Choose **K** initial cluster centers (centroids) randomly or using some other heuristic, like [[k-means++]] .

2. **Assignment Step**:
   Assign each data point to the nearest centroid. The distance is typically measured using **Euclidean distance**.

   $$d(x,c_k) = \sqrt{\sum_{i=1}^{n} (x_i - c_{k_i})^2}$$

   Where:
   - $x$ is a data point.
   - $c_k$ is the centroid of the $k^{th}$ cluster.
   - $x_i$ and $c_{k_i}$ are the $i^{th}$ feature of the point and centroid, respectively.

3. **Update Step**:
   Recalculate the centroids of each cluster by taking the **mean** of all the points assigned to it.

   $$c_k = \frac{1}{|C_k|} \sum_{x_i \in C_k} x_i$$

   Where:
   - $c_k$ is the new centroid of the $k^{th}$ cluster.
   - $C_k$ is the set of points in the $k^{th}$ cluster.
   - $x_i$ are the points in the $k^{th}$ cluster.

4. **Repeat**:
   Repeat steps 2 and 3 until the centroids no longer change significantly or a predetermined number of iterations is reached.

### Consider:
- **Fixed K**: You must specify the number of clusters $K$ in advance.
- **Sensitive to Initialization**: Random initialization of centroids can result in suboptimal clustering. Using K-Means++ helps mitigate this problem.
- **Not Ideal for Non-Spherical Clusters**: K-Means assumes that clusters are spherical and equally sized, so it may struggle with non-globular shapes or clusters with varying sizes and densities.

## Applications

K-Means clustering is widely used in many fields, such as:
- **Customer Segmentation**: Grouping customers based on purchasing behavior.
- **Image Compression**: Reducing the number of colors in an image.
- **Document Clustering**: Grouping similar documents based on their content.
- **Anomaly Detection**: Identifying outliers by clustering normal data points.



Graphical representation of clusters and their optimized centroids. The center is first positioned randomly and then through a metric (generally euclidian), the distance squared is minimized in every iteration. 

![[Cluster_graph.png]]

The algorithm that [[Sci-Kit Learn]] uses by default is called [[k-means++]] in a variant called "greedy k-means++" which is supposed to accelerate the convergence of the model.
It also takes a parameter "n_clusters" it has to be an integer and defines de amount of centroids.
[[k-means-example]].