from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_task():
    print("Exécution du DAG")

dag = DAG(
    'velib_dag', 
    description='Un DAG de test pour Velib', 
    schedule_interval='@hourly',  
    start_date=datetime(2025, 2, 7),
    catchup=False,
)

task = PythonOperator(
    task_id='run_my_task',
    python_callable=my_task,
    dag=dag,
)
