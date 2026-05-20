## How to install
Following set-up [documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html)

Install uv:
`curl -LsSf https://astral.sh/uv/install.sh | sh`

Install airflow:
```
uv venv
source .venv/bin/activate
bash airflow_install.sh
```

Run airflow standalone:
`airflow standalone > airflow_service.log 2>&1`

Check password for user:
`less /home/damian/airflow/simple_auth_manager_passwords.json.generated`

Airflow home directory:
`AIRFLOW_HOME=/home/damian/airflow`

Set up the db:
https://airflow.apache.org/docs/apache-airflow/stable/installation/setting-up-the-database.html

The Newcomer's Guide to Airflow's Architecture:
https://www.youtube.com/watch?v=oLTMN-4Rvj8

Tutorials
 - Airflow [101](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html)