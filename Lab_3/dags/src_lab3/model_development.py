import pandas as pd
import os
import pickle
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Define directories relative to the source file
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")
DATA_DIR = os.path.join(BASE_DIR, "data") # Assumed data dir

os.makedirs(MODEL_DIR, exist_ok=True)

def load_data():
    """
    Loads data from a CSV file.
    """
    # Note: Original had a hardcoded /home path, we'll try to find advertising.csv in data_dir
    csv_path = os.path.join(DATA_DIR, "advertising.csv")
    if not os.path.exists(csv_path):
        # Fallback if lab 3 data is shared with lab 2 or elsewhere
        csv_path = os.path.join(os.path.dirname(BASE_DIR), "Lab_2", "data", "advertising.csv")
    
    data = pd.read_csv(csv_path)
    return data

def data_preprocessing(data):
    """
    Preprocess the data.
    """
    X = data.drop(['Timestamp', 'Clicked on Ad', 'Ad Topic Line', 'Country', 'City'], axis=1)
    y = data['Clicked on Ad']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    num_columns = ['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']

    ct = make_column_transformer(
        (MinMaxScaler(), num_columns),
        (StandardScaler(), num_columns),
        remainder='passthrough'
    )

    X_train_tr = ct.fit_transform(X_train)
    X_test_tr = ct.transform(X_test)

    return X_train_tr, X_test_tr, y_train.values, y_test.values

def build_model(data, filename):
    """
    Build and save a logistic regression model.
    """
    X_train, _, y_train, _ = data

    lr_clf = LogisticRegression()
    lr_clf.fit(X_train, y_train)

    output_path = os.path.join(MODEL_DIR, filename)
    with open(output_path, 'wb') as f:
        pickle.dump(lr_clf, f)
    
    return output_path

def load_model(data, filename):
    """
    Load a saved model and evaluate it.
    """
    _, X_test, _, y_test = data
    output_path = os.path.join(MODEL_DIR, filename)
    
    with open(output_path, 'rb') as f:
        loaded_model = pickle.load(f)

    predictions = loaded_model.predict(X_test)
    score = loaded_model.score(X_test, y_test)
    print(f"Model score on test data: {score}")

    return int(predictions[0])

