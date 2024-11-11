Unsupervised learning is a great approach to soft problems. It goes beyond the diagram below, as one has an intuitive previous understanding of the vegetable categories and knows what the output should be. In reality, one can obtain clusters or categories that correlate many different variables, and don't conform to an intuitive understanding of the problem.

![[unsupervised.png]]

### Models:
- [[K-Means clustering]] is a good approach for spherical clusters. In advance, one cannot know how the cluster will be, so it's trial-error.
- For **non-spherical clusters**, [[DBSCAN]] and [[GMM]] are often the go-to methods.
  - **DBSCAN** excels when you have noise and varying densities.
  - **GMM** is great for capturing elliptical shapes.
- **Agglomerative Hierarchical Clustering** and **Mean Shift** (pending)
- [[Spectral Clustering]] is useful for complex, connected clusters that are not linearly separable.

Each of these algorithms has its own strengths and can be chosen based on the nature of your dataset and the type of clusters you are looking for.





