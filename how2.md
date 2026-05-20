## How to install
Following set-up [documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html):
 - Install uv:
`curl -LsSf https://astral.sh/uv/install.sh | sh`

 - Install airflow:
```
uv venv
source .venv/bin/activate
bash airflow_install.sh
```

## How to run
 - Run airflow standalone:
`airflow standalone > airflow_service.log 2>&1`
 - Check password for user:
`less /home/damian/airflow/simple_auth_manager_passwords.json.generated`
 - Airflow home directory:
`AIRFLOW_HOME=/home/damian/airflow`
 - Update DAG's db after creating a new DAG (example_dag.py)
```
# initialize the database tables
airflow db migrate
# print the list of active Dags
airflow dags list
# prints the list of tasks in the "example" DAG
airflow tasks list example_dag
# prints the graphviz representation of "example" DAG
airflow dags show example_dag
```
 - Set up the db:
https://airflow.apache.org/docs/apache-airflow/stable/installation/setting-up-the-database.html

## Tutorials
 - Airflow 101: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html

### Add input parameters on DAG
 - DAG-level parameters: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html 

## Understanding the basic architecture of airflow
The Newcomer's Guide to Airflow's Architecture: [video-tutorial](https://www.youtube.com/watch?v=oLTMN-4Rvj8).