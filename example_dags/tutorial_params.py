from airflow.sdk import DAG, task, Param, get_current_context
import logging

with DAG(
    "dag_with_params",
    params={
        "x": Param(5,type="integer",minimum=3),
        "my_int_param":6
    },
) as dag:
    
    def tutorial_params():
        @task()
        def example_task():
            ctx = get_current_context()
            logger = logging.getLogger("airflow.task")
            # This will print the default value, 6:
            logger.info(ctx["dag"].params["my_int_param"])

            # This will print the manually-provided value, 42
            logger.info(ctx["params"]["my_int_param"])

            # This will print the default value, 5, since it wasn't provided manually:
            logger.info(ctx["params"]["x"])

        run_result = example_task()

    tutorial_params()