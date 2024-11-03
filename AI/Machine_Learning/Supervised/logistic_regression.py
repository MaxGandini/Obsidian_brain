import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler
#Very simple model for classifying fruits
df = pd.DataFrame(
    {
        "weight": [150, 160, 170, 180, 190],  
        "color": [1, 1, 0, 0, 0], 
        "fruit": [0, 0, 1, 1, 1],  
        "core": ["no","no","yes","yes","yes"]    
    }
)
from sklearn.compose import ColumnTransformer

X = df.drop('fruit',axis=1)
y = df['fruit']
transformer = ColumnTransformer(
    [
        (
            "category", 
            OrdinalEncoder(),
            ["core"],  
        ),
        (
            "number",
            MinMaxScaler(),
            ["weight"],
        )
    ],
    remainder="passthrough",
    #verbose_feature_names_out=True,
)

data_= pd.DataFrame(transformer.fit_transform(X), columns=transformer.get_feature_names_out())
apple_ = pd.DataFrame(np.array([[140,1,"yes"]]),columns=['weight','color','core']) 
apple =pd.DataFrame(transformer.fit_transform(apple_), columns=transformer.get_feature_names_out()) 
#Things are getting pretty verbose
model = LogisticRegression()
model_fit = model.fit(data_,y)
data = pd.concat([data_, apple], ignore_index=True)
data['predictions'] = np.concatenate((model_fit.predict(data_), model_fit.predict(apple)))
data['target'] = y
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="number__weight", y="target", label="target")
sns.lineplot(data=data, x="number__weight", y="predictions", label="model")
plt.title("Logistic Regression Predictions")
plt.xlabel("Weight")
plt.ylabel("Predictions")
plt.legend()
plt.show()
