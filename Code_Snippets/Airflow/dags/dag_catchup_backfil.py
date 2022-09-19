from datetime import datetime, timedelta


from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner" : "ashish",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=2)

}


def greet(name, age):
    print(f"Hello from {name} who is {age} years old")


with DAG(
    default_args = default_args,
    dag_id = "dag_no_catchup_v1",
    description = "My first dag which Im trying out",
    start_date = datetime(2022, 9, 15, 2),
    schedule_interval = "@daily",
    catchup = False
) as dag:


    greet_task = PythonOperator(
        task_id = "greet_task",
        python_callable = greet,
        op_kwargs={'name': "Ashish", "age":24}
    )

    greet_task

