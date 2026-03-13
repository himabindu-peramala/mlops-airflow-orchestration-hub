# Ad Click Prediction Pipeline (Lab 2)

## Overview
This laboratory implements a supervised learning pipeline focused on binary classification for advertising click prediction. It demonstrates a robust end-to-end workflow from raw data ingestion to model evaluation and cross-DAG triggering.

## Machine Learning Logic
The pipeline orchestrates the following technical stages:
1.  **Raw Data Ingestion**: Extracts advertising engagement data and persists the initial state.
2.  **Transformation Pipeline**: Implements data splitting (Train/Test) and feature scaling for numerical predictors.
3.  **Model Archetype**: Trains a Logistic Regression model to predict the probability of user engagement.
4.  **Serialization**: Utilizes the `pickle` protocol for model persistence and artifact management between disparate pipeline stages.
5.  **Performance Assessment**: Validates the serialized model against held-out test data to confirm predictive accuracy.

## Orchestration Enhancements
The workflow has been modernized using the **Apache Airflow TaskFlow API**:
*   **Functional Decomposition**: Replaced legacy `PythonOperator` calls with `@task` decorators, significantly reducing boilerplate.
*   **Path-Based Data Management**: Standardized directory structures ensure that data artifacts are consistently accessible across local development and containerized environments.
*   **Inter-DAG Orchestration**: Demonstrates the use of the `TriggerDagRunOperator` to chain workflows, allowing for modular architecture where training pipelines can trigger independent API serving layers.
