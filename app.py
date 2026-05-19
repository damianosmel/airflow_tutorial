from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import requests
from requests.auth import HTTPBasicAuth
import os
import time
from typing import Optional

AIRFLOW_API = os.getenv("AIFLOW_API","http://localhost:8080/api/v2")
DAG_ID = "taskflow_fastapi"
CREDENTIALS_PATH = "/home/dmelidis/airflow/simple_auth_manager_passwords.json.generated"
POLL_INTERVAL = 1.0
POLL_TIMEOUT = 30.0


app = FastAPI()


def _load_credentials() -> Optional[dict[str,str]]:
    with open(CREDENTIALS_PATH) as credentials_fp:
        credentials_data = json.load(credentials_fp)
        if "admin" in credentials_data:
            admin_creds = HTTPBasicAuth("admin",credentials_data["admin"])
        else:
            admin_creds = None
    return admin_creds

class Payload(BaseModel):
    root: dict[str,float]

@app.post("/trigger/{dag_run_id}")
def trigger(dag_run_id: str, payload: dict):
    airflow_auth = _load_credentials()
    print(f'auth: {airflow_auth}')
    resp = requests.post(
        f"{AIRFLOW_API}/dags/{DAG_ID}/dagRuns",
        json={"dag_run_id": dag_run_id, "conf": payload},
        auth=airflow_auth,
    )
    if not resp.ok:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()

@app.post("/run-sum/{dag_run_id}")
def get_result(dag_run_id: str):
    deadline = time.time() + POLL_TIMEOUT
    state = None
    airflow_auth = _load_credentials()
    while time.time() < deadline:
        response = requests.get(f"{AIRFLOW_API}/dags/{DAG_ID}/dagRuns/{dag_run_id}", auth=airflow_auth)
        if not response.ok:
            raise HTTPException(status_code=response.status_code,detail=response.text)
        state = response.json().get("state")
        if state in ("success","failed"):
            break
        time.sleep(POLL_INTERVAL)

    if state != "success":
        raise HTTPException(status_code=400, detail=f"DAG run ended with state {state}.")
    
    # fetch XCom for the task that returns the total (task id: load)
    task_id = "load"
    xcom_response = requests(f"{AIRFLOW_API}/dags/{DAG_ID}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries",auth=airflow_auth)
    if not xcom_response.ok:
        raise HTTPException(status_code=xcom_response.status_code, detail=xcom_response.text)
    xcoms = xcom_response.json().get("xcom_entries",[])
    if not xcoms:
        return {"result": None}
    
    return {"result": xcoms[-1]["value"]}