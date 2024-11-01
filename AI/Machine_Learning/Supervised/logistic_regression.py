from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import seaborn.objects as so 

from sklearn.preprocessing import OrdinalEncoder

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

transformer = ColumnTransformer(
    [
        (
            "category",  # nombre (prefijo)
            OrdinalEncoder(),  # transformación
            ["core"],  # columnas
        )
    ],
    remainder="passthrough",
    #verbose_feature_names_out=True,
)

X_transformed = transformer.fit_transform(X)  # Fit and transform the data
X_transformed_df = pd.DataFrame(X_transformed, df.columns)

# data = pd.concat([X_transformed_df,X.drop('core')],ignore_index=True)
y = df['fruit']
logreg = LogisticRegression()
trained_logreg = logreg.fit(X_transformed_df,y)

apple = np.array([[140,1,"yes"]]) # Adjust based on what 'medium' should represent
new_df = pd.DataFrame(apple, df.columns)

# Transform the new data using the same ColumnTransformer
new_df_transformed = transformer.transform(new_df)

# Make predictions
predicted_logreg = trained_logreg.predict(X_transformed_df)
predicted_apple = trained_logreg.predict(new_df_transformed)

data = pd.concat([X,new_df],ignore_index=True)
data['predictions'] = np.concatenate((predicted_apple,predicted_logreg))
print(data)
(
   so.Plot(data, x="weight")
    .add(so.Line(), y="predictions", label="predictions")
    .add(so.Dot(), y="color", label="color")
    .label(y="fruit")
    .show()
)
