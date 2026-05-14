import json
import pendulum
from airflow.sdk import dag, task
from airflow.models import Variable

@dag(
    dag_id ="taskflow_fastapi",
    schedule=None,
    start_date = pendulum.datetime(2021,1,1,tz="UTC"),
    catchup=False,
    tags=["example"],
)

def taskflow_fastapi():
    @task()
    def extract(**context):
        # read conf passed when triggering the DAG (via REST API)
        dag_run = context.get("dag_run")
        if dag_run and getattr(dag_run,"conf",None):
            order_data_dict = dag_run.conf
        else:
            # fallback to original hardcoded data
            data_string = '{"1001":301.77, "1002":433.21, "1003": 502.22}'
            order_data_dict = json.loads(data_string)
        return order_data_dict
    
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

dag = taskflow_fastapi()