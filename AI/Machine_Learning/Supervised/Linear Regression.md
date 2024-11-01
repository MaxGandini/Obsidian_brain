A linear regression model is a model that estimates the linear relationship between a dependent variable(y) and one or more explanatory variables which are labeled as regressors or independent variables.
[[linear_regression.py]] (Very simple example)

![[linear_reg.png]]

In the context of machine learning, the regressors can be transformed qualitative features of some particular object which are correlated with a target variable(y). IE: The amount of colors in an image can be quantified by three columns as red green and blue. And an algorithm could find a correlation between these values to predict a certain feature of a photo.

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon$$
$$\hat{Y} = \begin{bmatrix} \hat{y}_1 \\ \hat{y}_2 \\ \vdots \\ \hat{y}_m \end{bmatrix},
\quad
X = \begin{bmatrix} 
1 & x_{11} & x_{12} & \dots & x_{1n} \\ 
1 & x_{21} & x_{22} & \dots & x_{2n} \\ 
\vdots & \vdots & \vdots & \ddots & \vdots \\ 
1 & x_{m1} & x_{m2} & \dots & x_{mn} 
\end{bmatrix},
\quad
\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \\ \beta_2 \\ \vdots \\ \beta_n \end{bmatrix}
$$
