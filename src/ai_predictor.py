import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_next_pass(passes_csv='results/passes.csv'):
    """
    Hybrid prediction: uses previous passes to predict next pass start
    """
    df = pd.read_csv(passes_csv)
    # Simple regression on pass start times
    X = np.arange(len(df)).reshape(-1,1)
    y = df['start_time'].values
    model = LinearRegression()
    model.fit(X, y)
    next_pass_start = model.predict(np.array([[len(df)]]))[0]
    return next_pass_start
