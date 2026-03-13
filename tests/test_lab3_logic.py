import pytest
import pandas as pd
import numpy as np
import os
from Lab_3.dags.src_lab3.model_development import data_preprocessing

def test_lab3_preprocessing():
    # Small sample data
    data = {
        "Daily Time Spent on Site": [68.95, 80.23, 74.15],
        "Age": [35, 31, 41],
        "Area Income": [61833.90, 68441.85, 59785.94],
        "Daily Internet Usage": [256.09, 193.77, 236.45],
        "Male": [0, 1, 1],
        "Timestamp": ["2016-03-27 00:53:11", "2016-04-04 01:39:02", "2016-01-10 02:31:19"],
        "Clicked on Ad": [0, 1, 0],
        "Ad Topic Line": ["A", "B", "C"],
        "City": ["C1", "C2", "C3"],
        "Country": ["D1", "D2", "D3"]
    }
    df = pd.DataFrame(data)
    
    # Run
    X_train, X_test, y_train, y_test = data_preprocessing(df)
    
    # Assertions
    assert X_train is not None
    assert X_test is not None
    assert len(X_train) + len(X_test) == 3
    assert X_train.shape[1] == 10 # 5 features * 2 scalers
