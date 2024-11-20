From the doc:

```
XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way. The same code runs on major distributed environment (Hadoop, SGE, MPI) and can solve problems beyond billions of examples.
```

An advantage it has, is that the algorithms introduce new [[Hyper-parameter optimization]] options. [[Sci-Kit Learn]], feeds off XGBoost, by having optimized loops in it's calculations.

XGBoost has many interesting concepts to enhance [[GBM]] (gradient boosting machines). 

Some of it's main features:
- [[Random Forest Regressor]] [[Pruning]] .
- [[Feature Interaction]] .

An example of it's usage can be found in :
- https://colab.research.google.com/drive/1yQNilgqWXe-MkWu_QfYD5RFWfrar_QWU?usp=sharing
- [[xgboost_random_forest.py]]. 

