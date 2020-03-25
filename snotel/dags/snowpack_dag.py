from datetime import datetime, timedelta
import os
from airflow import DAG
from snowpack.run_scraper import extract_snowpack_data

from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'mddarr',
    'start_date': datetime(2020, 4, 1),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': False
}

dag = DAG('snowpack_dag',
          default_args=default_args,
          description='Load snowpack data in Redshift with Airflow',
          schedule_interval='* * * * *',
          catchup = False
         )


# t1, t2 and t3 are examples of tasks created by instantiating operators
# [START basic_task]
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)
# [END basic_task]

# [END documentation]

# [START jinja_template]
templated_command = """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
{% endfor %}
"""

t3 = BashOperator(
    task_id='templated',
    depends_on_past=False,
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag,
)
# [END jinja_template]

t1 >> [t2, t3]
# [END tutorial]


