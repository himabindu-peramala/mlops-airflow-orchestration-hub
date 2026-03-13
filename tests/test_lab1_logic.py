import pytest
import pandas as pd
import numpy as np
import os
from Lab_1.dags.src_lab1.lab import data_preprocessing

def test_lab1_preprocessing():
    # Create sample data
    data = {
        "BALANCE": [1000, 2000, np.nan, 4000],
        "PURCHASES": [100, 200, 300, 400],
        "CREDIT_LIMIT": [500, 1000, 1500, 2000],
        "OTHER": [1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    
    # Run preprocessing
    processed = data_preprocessing(df)
    
    # Assertions
    # 1. Dropped NaN
    assert processed.shape[0] == 3
    # 2. Only 3 columns used for clustering
    assert processed.shape[1] == 3
    # 3. Scaled between 0 and 1
    assert processed.min() >= 0
    assert processed.max() <= 1
