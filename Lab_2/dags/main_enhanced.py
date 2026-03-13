import pendulum
from airflow.decorators import dag, task
from src_lab2.model_development import (
    load_data,
    data_preprocessing,
    separate_data_outputs,
    build_model,
    load_model,
)

@dag(
    dag_id="Airflow_Lab2_Enhanced",
    schedule="@daily",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["mlops", "lab2", "enhanced"],
    description="Enhanced Lab 2 using TaskFlow API",
)
def lab_2_enhanced():

    @task
    def load():
        return load_data()

    @task
    def preprocess(file_path):
        return data_preprocessing(file_path)

    @task
    def separate(file_path):
        return separate_data_outputs(file_path)

    @task
    def train(file_path):
        return build_model(file_path, "model.sav")

    @task
    def evaluate(file_path):
        return load_model(file_path, "model.sav")

    # Workflow
    raw_path = load()
    prep_path = preprocess(raw_path)
    sep_path = separate(prep_path)
    model_path = train(sep_path)
    prediction = evaluate(sep_path)

lab_2_enhanced_dag = lab_2_enhanced()
