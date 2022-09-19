from datetime import datetime, timedelta


from airflow import DAG
from airflow.operators .bash import BashOperator

default_args = {
    "owner" : "ashish",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=2)

}

with DAG(
    default_args = default_args,
    dag_id = "first_dag_v4",
    description = "My first dag which Im trying out",
    start_date = datetime(2022, 9, 15, 2),
    schedule_interval = "@daily"
) as dag:

    task1 = BashOperator(
        task_id = "first_task",
        bash_command = "echo hello world from first task"
    )
    
    task2 = BashOperator(
        task_id = "second_task",
        bash_command = "echo hello world from second task"
    )

    task3 = BashOperator(
        task_id = "third_task",
        bash_command = "echo hello world from third task"
    )


    # task1.set_downstream(task2) # or task.set_upstream(task1)
    # task1.set_downstream(task3)
    # task1 >> task2
    # task1 >> task3

    task1 >> [task2, task3]
