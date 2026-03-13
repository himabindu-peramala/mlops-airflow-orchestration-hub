# Modernized MLOps Airflow Orchestration

An enterprise-grade, containerized suite of Machine Learning workflows refactored to adhere to current Apache Airflow best practices and engineering standards.

## Project Overview
This project provides a comprehensive modernization of legacy Airflow workflows, transitioning from traditional operator-based patterns to the contemporary TaskFlow API. The architecture is designed to facilitate robust model orchestration, ensuring scalability, maintainability, and ease of deployment through advanced containerization and automated verification.

## Apache Airflow Overview
Apache Airflow is an open-source platform designed to programmatically author, schedule, and monitor complex workflows. By representing workflows as Directed Acyclic Graphs (DAGs), Airflow allows for clear visualization of task dependencies, robust error handling, and scalable execution. Its extensibility through Python makes it a standard for MLOps orchestration, enabling the integration of disparate data processing and machine learning libraries into unified, automated pipelines.

## Core Engineering Enhancements

### 1. Architectural Transition to TaskFlow API
The original implementations utilized the traditional `PythonOperator`, which often leads to fragmented code and complex state management. This project completely refactored the codebase to leverage the TaskFlow API.
*   **Functional Decomposition**: Logic is now encapsulated in decorated Python functions (`@task`), promoting modularity and unit testability.
*   **Automated XCom Serialization**: By utilizing TaskFlow, the manual management of XCom (Cross-Communication) through `xcom_push` and `xcom_pull` has been eliminated. Airflow now handles the serialization and deserialization of data structures—including DataFrames and Numpy arrays—natively.
*   **DAG Definition Clarity**: The use of the `@dag` decorator allows for a more declarative and readable definition of the workflow's entry point and configuration.

### 2. Microservices Containerization Standard
To eliminate environment-related failures and streamline the developer experience, a full-stack Airflow ecosystem is provided via Docker Compose.
*   **Standardized Runtime**: The environment is built on the `apache/airflow:2.10.2` image, ensuring that all contributors use an identical set of system dependencies and Python packages.
*   **Infrastructure Components**:
    *   **Postgres Metadata Store**: Handles all persistent state for the orchestration layer.
    *   **Airflow Scheduler and Webserver**: Provides independent services for task scheduling and system monitoring.
*   **Dynamic Development Workflow**: Host-to-container volume mounting is configured to allow real-time DAG parsing, enabling developers to iteratively update code without service restarts.

### 3. Automated Verification Framework
A dedicated testing suite has been integrated to maintain high code quality and prevent regression during deployment cycles.
*   **Integrity Verification**: Automated checks ensure that every DAG is syntactically valid and complies with the Airflow scheduler's loading requirements.
*   **Unit Testing of ML Logic**: Critical components of the ML pipeline—such as data preprocessing, feature engineering, and model training routines—are verified in isolation using `pytest`.

### 4. Robust Configuration and Path Handling
Path management has been standardized to utilize absolute references relative to the project root. This ensures that utility functions and dataset loaders function consistently whether executed in a local virtual environment or within a Linux-based Docker container.

---

## Workspace Structure
```text
.
├── Lab_1/             # KMeans Clustering Workflow
│   ├── dags/          # Refactored TaskFlow DAGs
│   ├── data/          # Clustered dataset storage
│   └── model/         # Serialized model artifacts
├── Lab_2/             # Logistic Regression Implementation
├── Lab_3/             # Advanced Hyperparameter Tuning
├── tests/              # Pytest verification suite
├── docker-compose.yaml # Service orchestration configuration
└── requirements.txt    # Project dependency specification
```

## System Execution Guide

### 1. Environment Deployment
To initialize the containerized stack, execute the following command from the project root:
```bash
docker compose up -d
```

### 2. Orchestration Interface
The Airflow Web UI is accessible through the following parameters:
*   **URL**: http://localhost:8081
*   **Security Credentials**: Username: `airflow` / Password: `airflow`

### 3. Performance and Integrity Validation
Before initiating production-level runs, verify the system integrity by executing the test suite:
```bash
# Recommendation: Execute within a configured virtual environment
pip install -r requirements.txt pytest apache-airflow
pytest tests/
```

---

## Acknowledgments
The conceptual foundations for these workflows were sourced from the Ramin Mohammadi MLOps laboratory series. This implementation focuses on the technical evolution of those concepts into high-standard software engineering artifacts.
