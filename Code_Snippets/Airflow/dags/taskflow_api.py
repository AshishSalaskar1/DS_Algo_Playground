from datetime import datetime, timedelta

from airflow.decorators import dag, task


default_args = {
    "owner" : "ashish",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=2)

}

'''
TaskFlow automatically deduces the relationships and also the Xcom vars needed for the functions
You just need to make the function calls in steps n the API will do rest of the things
'''

@dag(
    default_args = default_args,
    dag_id = "taskflow_api_dag_v1",
    description = "My first dag which Im trying out",
    start_date = datetime(2022, 9, 15, 2),
    schedule_interval = "@daily"
)
def taskflow_dag():
    @task(multiple_outputs=True)
    def get_name():
        return {
            "fname": "Ashish",
            "lname" : "Salaskar"
        }

    @task()
    def get_age():
        return 24

    @task()
    def greet(name, age):
        print(f"Hello from {name} who is {age} years old")

    name = get_name()
    age = get_age()
    greet(name["fname"], age)
    

my_dag = taskflow_dag()