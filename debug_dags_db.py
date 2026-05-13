from airflow.models import DagBag
db = DagBag('/home/dmelidis/projects/airflow_tutorial/example_dags')
print(db.import_errors)