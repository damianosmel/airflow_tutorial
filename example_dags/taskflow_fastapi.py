import pendulum
from airflow.sdk import task, DAG, get_current_context

with DAG(
    dag_id ="taskflow_fastapi",
    schedule=None,
    start_date = pendulum.datetime(2021,1,1,tz="UTC"),
    params={"data": {"1001":301.77, "1002":433.21, "1003": 502.22}},
    catchup=False,
    tags=["example"],
) as dag:

    def taskflow_fastapi():
        @task()
        def extract(**kwargs):
            params = kwargs["params"]
            input_data = {}
            if "data" in params:
                input_data = params["data"]
            print(f'input data: {input_data}')
            return input_data
        
        @task(multiple_outputs=True)
        def transform(order_data_dict: dict):
            total_order_value = sum(order_data_dict.values())
            return {"total_order_value": total_order_value}
        
        @task()
        def load(total_order_value: float):
            print(f"Total order value is {total_order_value:.2f}")
            return total_order_value
        
        order_data = extract()
        order_summary = transform(order_data)
        load(order_summary["total_order_value"])

    taskflow_fastapi()