import pendulum
from airflow.decorators import dag, task
from src_lab3.model_development import load_data, load_model, build_model, data_preprocessing

@dag(
    dag_id='Airflow_Lab3_Enhanced',
    schedule=None,
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=['mlops', 'lab3', 'enhanced'],
    description='Enhanced Lab 3 using TaskFlow API',
)
def lab_3_enhanced():

    @task
    def load():
        return load_data()

    @task
    def preprocess(data):
        return data_preprocessing(data)

    @task
    def train(data):
        return build_model(data, 'model.sav')

    @task
    def evaluate(data):
        # We pass both prep-data and name to load_model
        return load_model(data, 'model.sav')

    # Workflow
    raw_data = load()
    prep_data = preprocess(raw_data)
    # Note: build_model in Lab 3 original took (prep_data, filename)
    train_status = train(prep_data)
    prediction = evaluate(prep_data)

lab_3_enhanced_dag = lab_3_enhanced()
