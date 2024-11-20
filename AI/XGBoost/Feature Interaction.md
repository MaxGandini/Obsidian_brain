Feature interaction is a feature for [[Random Forest Regressor]] in the [[XGBoost]] library. 
From the docs very clearly explained:

When the tree depth is larger than one, many variables interact on the sole basis of minimizing training loss, and the resulting decision tree may capture a spurious relationship (noise) rather than a legitimate relationship that generalizes across different datasets. Feature interaction constraints allow users to decide which variables are allowed to interact and which are not.

The intuition behind interaction constraints is simple. Users may have prior knowledge about relations between different features, and encode it as constraints during model construction. But there are also some subtleties around specifying constraints. Take the constraint [1, 2], [2, 3, 4] as an example. The second feature appears in two different interaction sets, [1, 2] and [2, 3, 4]. So the union set of features allowed to interact with 2 is {1, 3, 4}. In the following diagram, the root splits at feature 2. Because all its descendants should be able to interact with it, all 4 features are legitimate split candidates at the second layer. At first sight, this might look like disregarding the specified constraint sets, but it is not.

Example: 
- https://colab.research.google.com/drive/1yQNilgqWXe-MkWu_QfYD5RFWfrar_QWU?usp=sharing
