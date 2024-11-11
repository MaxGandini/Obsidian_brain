
![[ttsl.png]]

[[Machine Learning]] models always return an output. We need tools to evaluate the validity of the model to what we are trying to apply.

There's a fundamental distinction between the score calculated with the test_data and the actual score with data you never saw.

- [[Cross Validation]]
- [[Hyper-parameter optimization]] 

Self-made examples:
- [[model_validation_overfit.py]] 
- [[model_validation.py]] 

Where I use [[Scikit-Pipeline]] and [[Cross Validation]]

We can divide the model validation again in [[Regression]] and [[Classification]] scores:
#### **[[Regression]] Metrics**

1. **R² (R-squared)**
   R² measures the proportion of variance in the dependent variable explained by the independent variables.

   $$
   R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
   $$

   Where:
   - $SS_{res}$ is the residual sum of squares:
     $$
     SS_{res} = \sum_{i=1}^n (y_i - \hat{y}_i)^2
     $$ 
   - $SS_{tot}$ is the total sum of squares:
     $$
     SS_{tot} = \sum_{i=1}^n (y_i - \bar{y})^2
     $$

   **Interpretation**:
   - $R^2 = 1$: Perfect model fit.
   - $R^2 = 0$: Model explains no variance.
   - $R^2 < 0$: Model performs worse than predicting the mean.

2. **Mean Absolute Error (MAE)**
   MAE is the average of the absolute errors between the observed and predicted values.

   $$
   MAE = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
   $$

   **Interpretation**:
   - Lower values indicate better model performance.

3. **Mean Squared Error (MSE)**
   MSE is the average of the squared differences between the observed and predicted values.

   $$
   MSE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
   $$

   **Interpretation**:
   - Lower values indicate better model performance.

4. **Root Mean Squared Error (RMSE)**
   RMSE is the square root of MSE, bringing the error back to the same unit as the dependent variable.

   $$
   RMSE = \sqrt{MSE}
   $$

   **Interpretation**:
   - Lower values indicate better model performance.


---

#### **[[Classification]] Metrics**

Another way of thinking this can be found in [[Evaluation methods]] inside [[Supervised-Learning]].

1. **Accuracy**
   Accuracy is the proportion of correct predictions out of all predictions.

   $$
   Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
   $$

   Where:
   - $TP$: True Positives
   - $TN$: True Negatives
   - $FP$: False Positives
   - $FN$: False Negatives

   **Interpretation**:
   - Higher accuracy indicates better model performance, but can be misleading with imbalanced datasets.

2. **Precision**
   Precision is the proportion of true positive predictions among all positive predictions.

   $$
   Precision = \frac{TP}{TP + FP}
   $$

   **Interpretation**:
   - Higher precision means fewer false positives.

3. **Recall (Sensitivity or True Positive Rate)**
   Recall is the proportion of actual positives that are correctly identified.

   $$
   Recall = \frac{TP}{TP + FN}
   $$

   **Interpretation**:
   - Higher recall means fewer false negatives.

4. **F1-Score**
   The F1-Score is the harmonic mean of precision and recall.

   $$
   F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
   $$

   **Interpretation**:
   - Balances precision and recall, useful for imbalanced datasets.

5. **Area Under the Receiver Operating Characteristic Curve (AUC-ROC)**
   AUC-ROC measures the ability of the model to distinguish between classes.

   $$
   AUC = \int_{0}^{1} \text{ROC Curve}
   $$

   Where ROC is a plot of the true positive rate vs. false positive rate at various thresholds.

   **Interpretation**:
   - AUC of 0.5: Model is no better than random guessing.
   - AUC of 1: Perfect model.

6. **Confusion Matrix**
   A confusion matrix shows the true positives, true negatives, false positives, and false negatives.

   $$
   \begin{matrix}
   & Predicted\ Positives & Predicted\ Negatives \\
   Actual\ Positives & TP & FN \\
   Actual\ Negatives & FP & TN \\
   \end{matrix}
   $$

   **Interpretation**:
   - Provides insight into the types of errors made by the classifier.

---

### Conclusion
- **Regression** metrics focus on how well the model predicts continuous values, with R², MAE, MSE, and RMSE being commonly used.
- **Classification** metrics focus on how well the model categorizes discrete labels, with accuracy, precision, recall, F1-score, and AUC being important metrics.