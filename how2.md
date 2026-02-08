## How to install
Following set-up [documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html)

```
export AIRFLOW_HOME=~/airflow

AIRFLOW_VERSION=3.0.0
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
pip3 install -r requirements.txt --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.10.txt"
```

Start-up the service:
`airflow standalone > airflow_service.log 2>&1`

Check password for user:
`less /home/damian/airflow/simple_auth_manager_passwords.json.generated`

Airflow home directory:
`AIRFLOW_HOME=/home/damian/airflow`