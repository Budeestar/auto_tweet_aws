from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from twitter_etl import post_tweet

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 6, 18),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'tweet_scheduler',
    default_args=default_args,
    description='A simple DAG to tweet daily',
    schedule_interval=timedelta(days=1),
)

tweet_task = PythonOperator(
    task_id='post_daily_tweet',
    python_callable=post_tweet,
    op_kwargs={'message': 'Hello Twitter! This is a scheduled tweet from Airflow.'},
    dag=dag,
)
