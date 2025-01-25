Imagine you have a 3D space with some clouds of points, and you sweep the space using a sphere of radius $\epsilon$, while writing down how many points were into the sphere for each step.

DBSCAN groups points into clusters based on two key parameters: 

- $\epsilon$ which is the maximum distance between two points to be considered neighbors.
- **min_samples** which is the minimum number of points required to form a dense region

It assigns a cluster ID to each point. Points in the same cluster have the same ID.
