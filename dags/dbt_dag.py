import os
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={"database": "dbt_db", "schema": "dbt_schema"},
    )
)

# Ensure AIRFLOW_HOME is set, fallback to a default
dbt_executable = os.getenv("AIRFLOW_HOME", "/usr/local/airflow") + "/dbt_venv/bin/dbt"

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig(
        "/usr/local/airflow/dags/dbt/data_pipeline"
    ),
    operator_args={"install_deps": True},  # Corrected syntax
    profile_config=profile_config,  # Corrected arg
    execution_config=ExecutionConfig(dbt_executable_path=dbt_executable),
    schedule_interval="@daily",
    start_date=datetime(2025, 2, 22),
    catchup=False,
    dag_id="dbt_dag",
)
