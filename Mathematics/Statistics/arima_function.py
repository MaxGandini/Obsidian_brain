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
    # Ensure data is a pandas Series
    data = pd.Series(data)
    
    # Split the data into training and testing sets
    train_len = int(len(data) * train_size)
    train, test = data[:train_len], data[train_len:]
    
    # Fit ARIMA model
    model = ARIMA(train, order=order)
    model_fit = model.fit()
    
    # Forecasting on test data
    predictions = model_fit.forecast(steps=len(test))
    
    # Calculate residuals
    residuals = test - predictions[:len(test)]
    
    return model_fit, predictions, residuals

# Example usage
if __name__ == "__main__":
    # Create a synthetic time series
    np.random.seed(42)
    time_series_data = np.cumsum(np.random.randn(1000))  # Random walk
    
    # Process with ARIMA model
    fitted_model, preds, resids = arima_model(time_series_data, order=(49, 9, 9))
    
    plt.plot(range(200),preds)
    plt.plot(range(len(time_series_data)),time_series_data)
    plt.show()
    print("Model Summary:")
    print(fitted_model.summary())
    print("\nPredictions:", preds)
    print("\nResiduals:", resids)
