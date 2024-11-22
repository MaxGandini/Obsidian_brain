import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
import numpy as np 

np.random.seed(42)
n = 4000
trend = np.linspace(1, 8, n)  # Linear trend
seasonality = 2 * np.sin(np.linspace(0, 4 * np.pi, n))  # Seasonal component
noise = np.random.normal(0, 0.1, n)  # Random noise
time_series = trend + seasonality + noise

def create_lagged_features(series, lag=3):
        data = pd.DataFrame(series, columns=['y'])
        for i in range(1, lag + 1):
                data[f'lag_{i}'] = data['y'].shift(i)
        data.dropna(inplace=True)
        return data

lagged_data = create_lagged_features(time_series, lag=3)

X = lagged_data.iloc[:, 1:]  
y = lagged_data.iloc[:, 0]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = XGBRegressor(objective='reg:squarederror', n_estimators=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(12, 6))
plt.plot(range(len(time_series)), time_series, label='Original Series', color='blue')
plt.plot(range(len(X_train), len(X_train) + len(y_test)), y_test, label='True Future Values', color='green')
plt.plot(range(len(X_train), len(X_train) + len(y_pred)), y_pred, label='Predicted Values', color='red', linestyle='--')
plt.title('Time Series Forecasting with XGBoost')
plt.legend()
plt.show()
