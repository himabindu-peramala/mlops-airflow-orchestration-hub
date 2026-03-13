# KMeans Clustering Pipeline (Lab 1)

## Overview
This laboratory implements an automated unsupervised learning pipeline designed to cluster consumer data. The workflow identifies natural groupings within the dataset and determines the optimal cluster count using the Elbow Method.

## Machine Learning Logic
The pipeline executes the following high-level operations:
1.  **Data Ingestion**: Loads raw consumer data from CSV format.
2.  **Preprocessing**: Performs dimensionality reduction by selecting relevant clustering features (Balance, Purchases, Credit Limit) and handles missing values.
3.  **Feature Scaling**: Utilizes `MinMaxScaler` to normalize features between 0 and 1, ensuring equal weight during distance calculations.
4.  **Cluster Optimization**: Iteratively builds KMeans models across a range of cluster counts to compute the Sum of Squared Errors (SSE).
5.  **Elbow Identification**: Uses the `KneeLocator` algorithm to programmatically identify the "elbow" point, indicating the optimal number of clusters.

## Orchestration Enhancements
This lab has been refactored from a traditional `PythonOperator` implementation to a modern **TaskFlow API** architecture:
*   **Modular Tasks**: Each ML step is encapsulated within a `@task` decorated function, promoting isolation and reusability.
*   **Automatic Data Passing**: Leveraging Airflow's native XCom backend, DataFrames and SSE values are passed between tasks implicitly without manual serialization.
*   **Clean DAG Topology**: The workflow is defined using the `@dag` decorator, providing a clear, Pythonic representation of the pipeline's logic and dependencies.