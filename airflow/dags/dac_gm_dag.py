from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datasets.guarda_municipal_dataset import GuardaMunicipalDataset


def get_dataset():
    dataset = GuardaMunicipalDataset()
    dataset.load_clean_data()
    dataset.save_dataset()


def save_on_db():
    print('saving on db...')


dag_dac_gm = DAG('etl_dac_gm', description='ETL for DAC_GM', start_date=datetime(2024, 2, 24), catchup=False)

get_dataset_operator = PythonOperator(task_id='get_dataset', python_callable=get_dataset, dag=dag_dac_gm)
save_on_db_operator = PythonOperator(task_id='save_on_db', python_callable=save_on_db, dag=dag_dac_gm)

get_dataset_operator >> save_on_db_operator
