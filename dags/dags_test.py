import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
# -- 분 시 
# catchup=False, 누락된 구간 따라가면서 돌린다 True
with DAG(
    dag_id="dags_test",
    schedule="0 0 * * *", 
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    bash_t1 >> bash_t2

    