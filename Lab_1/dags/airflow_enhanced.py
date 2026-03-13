import pendulum
from airflow.decorators import dag, task
from src_lab1.lab import load_data, data_preprocessing, build_save_model, load_model_elbow

@dag(
    dag_id='Airflow_Lab1_Enhanced',
    schedule=None,
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=['mlops', 'lab1', 'enhanced'],
    description='Enhanced Lab 1 using TaskFlow API',
)
def lab_1_enhanced():
    
    @task
    def load():
        return load_data()

    @task
    def preprocess(data):
        return data_preprocessing(data)

    @task
    def train(data):
        return build_save_model(data, "model.sav")

    @task
    def evaluate(sse):
        return load_model_elbow("model.sav", sse)

    # Define the workflow
    raw_data = load()
    clean_data = preprocess(raw_data)
    sse_list = train(clean_data)
    prediction = evaluate(sse_list)

lab_1_enhanced_dag = lab_1_enhanced()
