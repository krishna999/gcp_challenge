import os
import datetime
import csv
import requests

from airflow import models
from airflow.operators import bash_operator
from airflow.operators import python_operator
from google.cloud import storage

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time())
default_dag_args = {
    # Setting start date as yesterday starts the DAG immediately when it is
    # detected in the Cloud Storage bucket.
    'start_date': yesterday,
    # To email on failure or retry set 'email' arg to your email and enable
    # emailing here.
    'email_on_failure': False,
    'email_on_retry': False,
    # If a task fails, retry it once after waiting at least 5 minutes
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5)
}

with models.DAG(
        'load_coinmarketcap_bq',
        # Continue to run DAG once per day
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:

    bq_load_coinmarket_cap = bash_operator.BashOperator(
        task_id='bq_load_coinmarket_cap',
        bash_command='bq --location=US load --autodetect --replace --source_format=CSV crypto.coinmarketcap gs://coinmarketcap-2018/crypto.csv')

    bq_load_coinmarket_cap
