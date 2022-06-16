import mlflow

def get_power(x,n):
    return x**n

if __name__ == '__main__':
    with mlflow.start_run():
        # exp_list = [(2,4), (5,7), (8,12)]
        # for (x,n) in exp_list:
        x,n = 3,12
        y = get_power(x, n)

        mlflow.log_param("x",x)
        mlflow.log_param("n", n)
        mlflow.log_metric("y", n)

