import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
import pickle
import os

# Using absolute paths relative to the project root for consistency in Docker
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model")
os.makedirs(MODEL_DIR, exist_ok=True)

def load_data():
    """
    Loads data from a CSV file.
    """
    df = pd.read_csv(os.path.join(DATA_DIR, "file.csv"))
    return df

def data_preprocessing(df):
    """
    Performs preprocessing on the input DataFrame.
    """
    df = df.dropna()
    clustering_data = df[["BALANCE", "PURCHASES", "CREDIT_LIMIT"]]

    min_max_scaler = MinMaxScaler()
    clustering_data_minmax = min_max_scaler.fit_transform(clustering_data)
    return clustering_data_minmax

def build_save_model(data, filename: str):
    """
    Builds a KMeans model on the preprocessed data and saves it.
    Returns the SSE list.
    """
    kmeans_kwargs = {"init": "random", "n_init": 10, "max_iter": 300, "random_state": 42}
    sse = []
    for k in range(1, 50):
        kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)

    output_path = os.path.join(MODEL_DIR, filename)
    with open(output_path, "wb") as f:
        pickle.dump(kmeans, f)

    return sse

def load_model_elbow(filename: str, sse: list):
    """
    Loads the saved model and uses the elbow method to report k.
    """
    output_path = os.path.join(MODEL_DIR, filename)
    with open(output_path, "rb") as f:
        loaded_model = pickle.load(f)

    kl = KneeLocator(range(1, 50), sse, curve="convex", direction="decreasing")
    print(f"Optimal no. of clusters (Elbow): {kl.elbow}")

    # predict on raw test data
    df_test = pd.read_csv(os.path.join(DATA_DIR, "test.csv"))
    pred = loaded_model.predict(df_test)[0]
    
    return int(pred)

