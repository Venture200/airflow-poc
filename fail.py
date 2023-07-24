from airflow import DAG, AirflowException
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from utils.callbacks import zabbix_dag_callback
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Teamplatform',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 0,
}

dag_fail = DAG(
    'test_fail_elnur',
    default_args=default_args,
    description='A DAG which always fails',
    schedule_interval=None,
    is_paused_upon_creation=True,
    catchup=False,
    on_success_callback=zabbix_dag_callback,
    on_failure_callback=zabbix_dag_callback,
    tags=['airflow'],
)


def raise_exception(message):
    print("Hellowrold")

with dag_fail:
    task_fail_one_email = BashOperator(
        task_id='fail_one_email',
        bash_command="curl -X GET -H 'Content-Type: application/xml' https://web-api.tp.entsoe.eu/api?securityToken=71b199bf-f53c-434c-b028-4c9cb622ee28&documentType=A24&processType=A51&area_Domain=10YCZ-CEPS-----N&TimeInterval=2019-12-16T13:00Z/2019-12-16T18:00Z"
    )