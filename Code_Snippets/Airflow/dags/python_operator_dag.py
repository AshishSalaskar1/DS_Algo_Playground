from datetime import datetime, timedelta


from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner" : "ashish",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=2)

}

def get_name(task_instance):
    task_instance.xcom_push(key='name', valmue="Ashish")

def get_age(task_instance):
    task_instance.xcom_push(key='age', value=24)

# the "some_dict" must be passed with same name "some_dict" in op_kwargs while defining the task
def greet(some_dict, task_instance):
    name = task_instance.xcom_pull(task_ids='get_name_task', key='name')
    age = task_instance.xcom_pull(task_ids='get_age_task', key='age')

    print(f"Hello from {name} who is {age} years old")


with DAG(
    default_args = default_args,
    dag_id = "python_dag_v5",
    description = "My first dag which Im trying out",
    start_date = datetime(2022, 9, 15, 2),
    schedule_interval = "@daily"
) as dag:

    get_name_task = PythonOperator(
        task_id = "get_name_task",
        python_callable = get_name
    )
    
    get_age_task = PythonOperator(
        task_id = "get_age_task",
        python_callable = get_age
    )

    greet_task = PythonOperator(
        task_id = "greet_task",
        python_callable = greet,
        op_kwargs={'some_dict': {'a': 1, 'b': 2}}
    )

    [get_age_task, get_name_task] >> greet_task


# This function can then be used to 
def caller_functions(val1, val2):
    arr = [val1, val2]
    set_ele = set()
    for ele in arr:
        for j in range(len(ele)):
            set_ele.append(val1.oferred)
            print(f"{set_eke}amicable") 