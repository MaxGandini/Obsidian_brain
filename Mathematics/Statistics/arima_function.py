import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

def arima_model(data, order=(1, 1, 1), train_size=0.8):
    """
    Fits an ARIMA model to the time series data and returns the fitted model, predictions, and residuals.
    
    Parameters:
        data (list or pd.Series): The time series data to model.
        order (tuple): The (p, d, q) order of the ARIMA model.
        train_size (float): Proportion of data to use for training (rest is used for testing).
        
    Returns:
        model_fit: Fitted ARIMA model.
        predictions: Predictions on the test set.
        residuals: Residuals from the model.
    """
    data = pd.Series(data)
    
    train_len = int(len(data) * train_size)
    train, test = data[:train_len], data[train_len:]
    
    # Fit ARIMA model
    model = ARIMA(train, order=order)
    model_fit = model.fit()
    
    # Forecasting on test data
    predictions = model_fit.forecast(steps=len(test))
    
    residuals = test - predictions[:len(test)]
    
    return model_fit, predictions, residuals,test

if __name__ == "__main__":
    np.random.seed(42)
    
    n = 4000
    trend = np.linspace(1, 8, n)  # Linear trend
    seasonality = 2 * np.sin(np.linspace(0, 4 * np.pi, n))  # Seasonal component
    noise = np.random.normal(0, 0.1, n)  # Random noise
    time_series = trend + seasonality + noise

    fitted_model, preds, resids, test = arima_model(time_series, order=(1, 1, 2))
    
    plt.plot(range(len(preds)),preds)
    plt.plot(range(len(time_series)),time_series)
    plt.show()
    print("Model Summary:")
    print(fitted_model.summary())
    print("\nPredictions:", preds)
    print("\nResiduals:", resids)
