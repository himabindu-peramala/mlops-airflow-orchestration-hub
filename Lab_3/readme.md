# Advanced Hyperparameter Tuning & Notification (Lab 3)

## Overview
This laboratory implements an advanced Machine Learning orchestration workflow focusing on feature engineering comparisons and automated system notifications. It highlights the integration of monitoring hooks within modern Airflow pipelines.

## Machine Learning Logic
The pipeline executes a sophisticated feature transformation logic:
1.  **Comparative Scaling**: Applies both `MinMaxScaler` and `StandardScaler` to the input features to analyze the impact of different normalization strategies on model performance.
2.  **Feature Concatenation**: Combines transformed features into a high-dimensional feature set for robust model training.
3.  **Persistent Artifacts**: Manages the lifecycle of serialized model files within dedicated storage directories.

## Orchestration Enhancements
This lab integrates advanced Airflow features with the **TaskFlow API**:
*   **Automated Monitoring**: Implements custom success and failure callbacks using native Airflow hooks to trigger email notifications upon pipeline completion.
*   **Dynamic Path Resolution**: Utilizes robust path handling logic to detect and adapt to different execution environments (Docker vs. Local VM), ensuring directory existence and data availability.
*   **Type-Safe Task Flow**: Uses Python type hinting and `@task` decorators to define clear interfaces for data exchange between preprocessing, training, and evaluation nodes.
