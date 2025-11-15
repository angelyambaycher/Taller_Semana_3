import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_scale(df):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    return X_scaled
