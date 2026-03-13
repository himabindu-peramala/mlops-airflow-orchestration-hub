import pytest
from airflow.models import DagBag

def test_dag_integrity():
    """
    Test that all DAGs in the repository can be loaded by Airflow without errors.
    """
    dag_bag = DagBag(dag_folder=".", include_examples=False)
    assert not dag_bag.import_errors, f"DAG import errors: {dag_bag.import_errors}"

def test_dag_enhanced_exists():
    """
    Verify that our enhanced DAGs are correctly indexed.
    """
    dag_bag = DagBag(dag_folder=".", include_examples=False)
    expected_dags = ["Airflow_Lab1_Enhanced", "Airflow_Lab2_Enhanced", "Airflow_Lab3_Enhanced"]
    for dag_id in expected_dags:
        assert dag_id in dag_bag.dags, f"DAG {dag_id} not found in DagBag"
