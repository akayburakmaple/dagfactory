from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}
def greet():
    print(f"merhaba")
    print("project 1 done.")


main_dag= DAG(
    default_args=default_args,
    dag_id='project1',
    description='project 1 description',
    start_date=datetime(2021, 10, 6),
    schedule_interval='@daily'
)
task1 = PythonOperator(
    task_id='greet',
    python_callable=greet,
    dag=main_dag
)

task2 = BashOperator(
        task_id="p1_bash",
        bash_command='pwd',
        dag=main_dag
    )

task1 >> task2
DAGS= [main_dag]