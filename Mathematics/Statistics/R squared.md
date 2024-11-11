### R² (R-squared) Explanation

**R-squared** is a statistical metric that represents the proportion of the variance in the dependent variable that is explained by the independent variables in a regression model.

Mathematically, R² is defined as:

$$
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
$$

Where:
- $SS_{res}$ is the **residual sum of squares** (the sum of squared differences between the observed and predicted values):
  
  $$
  SS_{res} = \sum_{i=1}^n (y_i - \hat{y}_i)^2
  $$

- $SS_{tot}$ is the **total sum of squares** (the sum of squared differences between the observed values and their mean):
  
  $$
  SS_{tot} = \sum_{i=1}^n (y_i - \bar{y})^2
  $$

Where:
- $y_i$ are the observed values.
- $\hat{y}_i$ are the predicted values.
- $\bar{y}$ is the mean of the observed values.

### Interpretation of R²:
- **R² = 1**: Perfect model fit (all data points lie on the regression line).
- **R² = 0**: The model does not explain any of the variance in the dependent variable.
- **R² < 0**: The model performs worse than simply predicting the mean of the dependent variable.

### Adjusted R²:
When working with multiple regression models, **Adjusted R²** is often used to account for the number of predictors in the model. It adjusts the R² value to prevent overfitting:

$$
R^2_{adj} = 1 - \left(1 - R^2\right) \frac{n - 1}{n - p - 1}
$$

Where:
- $n$ is the number of observations.
- $p$ is the number of predictors in the model.