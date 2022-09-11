# from datetime import datetime, date
# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
#
# def get_dataset():
#     path = f"https://mid.curitiba.pr.gov.br/dadosabertos/Sigesguarda/{date.today().year}-{'0' if date.today().month < 10 else None}{date.today().month if date.today().day > 1 else date.today().month - 1}-01_sigesguarda_-_Base_de_Dados.csv"
#     print(f"Loading dataset from {path}")
# def filter_dataset():
#     print("Creating new dataset from filters")
# def transform_dataset():
#     print("Creating new dataset from transformations")
# def load_dataset_to_google():
#     print("Uploading data...")
#
# def print_firstdag():
#     return 'My First DAG from HevoData!'
#
# dag_dac_gm = DAG('etl_dac_gm', description='ETL for DAC_GM', start_date=datetime(2022, 2, 24), catchup=False)
#
# get_operator = PythonOperator(task_id='1_task', python_callable=get_dataset, dag=dag_dac_gm)
# filter_operator = PythonOperator(task_id='2_task', python_callable=filter_dataset, dag=dag_dac_gm)
# transform_operator = PythonOperator(task_id='3_task', python_callable=transform_dataset, dag=dag_dac_gm)
# upload_operator = PythonOperator(task_id='4_task', python_callable=load_dataset_to_google, dag=dag_dac_gm)
#
# get_operator >> filter_operator >> transform_operator >> upload_operator