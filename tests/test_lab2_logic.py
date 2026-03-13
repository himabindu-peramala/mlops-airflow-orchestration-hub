import pytest
import pandas as pd
import numpy as np
import os
import pickle
from Lab_2.dags.src_lab2.model_development import data_preprocessing, WORKING_DIR

def test_lab2_preprocessing():
    # Small sample data matching advertising.csv schema
    data = {
        "Daily Time Spent on Site": [68.95, 80.23],
        "Age": [35, 31],
        "Area Income": [61833.90, 68441.85],
        "Daily Internet Usage": [256.09, 193.77],
        "Male": [0, 1],
        "Timestamp": ["2016-03-27 00:53:11", "2016-04-04 01:39:02"],
        "Clicked on Ad": [0, 1],
        "Ad Topic Line": ["A", "B"],
        "City": ["C", "D"],
        "Country": ["E", "F"]
    }
    df = pd.DataFrame(data)
    
    # Save to temp pickle as the function expects a path
    test_raw_path = os.path.join(WORKING_DIR, "test_raw.pkl")
    with open(test_raw_path, "wb") as f:
        pickle.dump(df, f)
        
    # Run
    out_path = data_preprocessing(test_raw_path)
    
    # Assertions
    assert os.path.exists(out_path)
    with open(out_path, "rb") as f:
        X_train, X_test, y_train, y_test = pickle.load(f)
        
    assert X_train is not None
    assert len(y_train) + len(y_test) == 2
