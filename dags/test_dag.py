import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
import datetime

# Define a data atual com o fuso horário UTC
now = pendulum.now(tz="UTC")
now_to_the_hour = (now - datetime.timedelta(0, 0, 0, 0, 0, 3)).replace(minute=0, second=0, microsecond=0)

# Define a data de início e o nome do DAG
START_DATE = now_to_the_hour
DAG_NAME = "test_dag_v1"

# Define o DAG com as correções
dag = DAG(
    dag_id=DAG_NAME,  # Altere para dag_id ao invés de apenas DAG_NAME
    schedule_interval="*/10 * * * *",
    default_args={"depends_on_past": True},
    start_date=START_DATE,  # Use a variável START_DATE que você definiu
    catchup=False,
)

# Define a tarefa BashOperator
t1 = BashOperator(
    task_id="print_hello",
    bash_command='echo "Hello, World!"',
    dag=dag,
)
