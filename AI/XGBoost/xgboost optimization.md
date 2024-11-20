From xgboost's docs:
# Control Overfitting

When you observe **high training accuracy**, but **low test accuracy**, it is likely that you encountered an overfitting problem.

There are, in general, two ways to control overfitting in XGBoost:

1. **Directly control model complexity:**
   - `max_depth`
   - `min_child_weight`
   - `gamma`

2. **Add randomness to make training robust to noise:**
   - `subsample`
   - `colsample_bytree`

You can also reduce the stepsize `eta`. Remember to increase `num_round` when you do so.

---

# Handle Imbalanced Dataset

For common cases, such as ads clickthrough logs, the dataset is often extremely imbalanced. This can affect the training of the XGBoost model, and there are two ways to improve it:

### If you care only about the overall performance metric (AUC) of your prediction:
- Balance the positive and negative weights via `scale_pos_weight`.
- Use **AUC** for evaluation.

### If you care about predicting the right probability:
- In such a case, do **not** re-balance the dataset.
- Set the parameter `max_delta_step` to a finite number (e.g., `1`) to help convergence.