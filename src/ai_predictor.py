import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import requests
import io

class AIPredictor:
    """
    AI Predictor for time-series or tabular data.
    Supports internal datasets and external data sources (CSV/API).
    """
    def __init__(self, model=None):
        self.model = model if model else RandomForestRegressor(
            n_estimators=100, max_depth=None, random_state=42
        )
        self.feature_columns = None
    
    def load_internal_data(self, filepath):
        """
        Load internal dataset (CSV/Excel)
        """
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filepath.endswith('.xlsx'):
            df = pd.read_excel(filepath)
        else:
            raise ValueError("Unsupported file type. Use CSV or Excel.")
        return df
    
    def load_external_csv(self, url):
        """
        Load external dataset from a public CSV URL
        """
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"Failed to fetch data: {response.status_code}")
        df = pd.read_csv(io.StringIO(response.text))
        return df
    
    def preprocess(self, df, target_column):
        """
        Basic preprocessing: handle missing values, separate features/target
        """
        df = df.copy()
        df = df.dropna()
        self.feature_columns = [col for col in df.columns if col != target_column]
        X = df[self.feature_columns].values
        y = df[target_column].values
        return X, y
    
    def train(self, X, y, test_size=0.2):
        """
        Train model and split data
        """
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"Model trained. MSE: {mse:.4f}, R2: {r2:.4f}")
        return mse, r2
    
    def predict(self, df=None):
        """
        Make predictions on new data
        """
        if df is not None:
            if self.feature_columns is None:
                raise ValueError("Feature columns not set. Train the model first.")
            X = df[self.feature_columns].values
        else:
            raise ValueError("No data provided for prediction.")
        return self.model.predict(X)
    
    def integrate_external_sources(self, internal_df, external_urls, target_column):
        """
        Combine internal data with multiple external datasets
        """
        combined_df = internal_df.copy()
        for url in external_urls:
            ext_df = self.load_external_csv(url)
            combined_df = pd.concat([combined_df, ext_df], ignore_index=True, sort=False)
        # Optional: fill missing target values with mean
        combined_df[target_column] = combined_df[target_column].fillna(combined_df[target_column].mean())
        return combined_df
