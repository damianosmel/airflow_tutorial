# Airflow Tutorial

Description: This is a repo to keep track of my learning in Apache Airflow workflow engine.

## Main concepts - Dictionary

### XComs
XComs (short for "cross-communications") in Airflow are a mechanism that allows tasks to communicate with each other by pushing and pulling small amounts of data. They are identified by a key, task_id, and dag_id, and are designed for lightweight data transfer between tasks within a DAG run. [(reference)](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html)