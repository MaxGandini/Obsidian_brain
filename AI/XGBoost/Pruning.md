[[XGBoost]] by default computes to `max_depth`. After converging, the algorithm has a pruning step API that permits the user to trim the tree using validation.

```python
prune_params = {
    "process_type": "update",
    "updater": "prune",
    "max_depth": 5,  # New maximum depth for pruning
    }

pruned_model = xgb.train(
						  params=prune_params,
						  dtrain=dtrain,
						  num_boost_round=num_boost_round, 
						  evals=[(dval, "eval")],
						  verbose_eval=10,
						  xgb_model=model  
						)

```

An example can be found: 
- https://colab.research.google.com/drive/1yQNilgqWXe-MkWu_QfYD5RFWfrar_QWU?usp=sharing
- [[xgboost_random_forest.py]]
