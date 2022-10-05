
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from projects.project2.scripts.p2script1 import project2_script1
from projects.project2.scripts.p2script2 import project2_script2

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def project2_task3():
    return "Tüm tasklar yapıldı."

main_dag = DAG(
    default_args=default_args,
    dag_id='project2',
    description='project 2 description',
    start_date=datetime(2021, 10, 6),
    schedule_interval='@daily'
)
task1 = PythonOperator(
    task_id='project2_script1',
    python_callable=project2_script1,
    dag = main_dag
)
task2= PythonOperator(
    task_id='project2_script2',
    python_callable=project2_script2,
    dag = main_dag
)
task3= PythonOperator(
    task_id='project2_script3',
    python_callable=project2_task3,
    dag = main_dag
)
[task1,task2] >> task3
DAGS = [ main_dag ]
