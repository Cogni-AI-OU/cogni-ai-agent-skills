from __future__ import annotations

import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, Asset, AssetOrTimeSchedule, CronTriggerTimetable

dag1_asset = Asset("s3://dag1/output_1.txt", extra={"hi": "bye"})
dag2_asset = Asset("s3://dag2/output_1.txt", extra={"hi": "bye"})
dag3_asset = Asset("s3://dag3/output_3.txt", extra={"hi": "bye"})

with DAG(
    dag_id="asset_produces_1",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule="@daily",
    tags=["produces", "asset-scheduled"],
) as dag1:
    # [START task_outlet]
    BashOperator(outlets=[dag1_asset], task_id="producing_task_1", bash_command="sleep 5")
    # [END task_outlet]

with DAG(
    dag_id="asset_produces_2",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=None,
    tags=["produces", "asset-scheduled"],
) as dag2:
    BashOperator(outlets=[dag2_asset], task_id="producing_task_2", bash_command="sleep 5")

# [START dag_dep]
with DAG(
    dag_id="asset_consumes_1",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=[dag1_asset],
    tags=["consumes", "asset-scheduled"],
) as dag3:
    # [END dag_dep]
    BashOperator(
        outlets=[Asset("s3://consuming_1_task/asset_other.txt")],
        task_id="consuming_1",
        bash_command="sleep 5",
    )

with DAG(
    dag_id="asset_consumes_1_and_2",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=[dag1_asset, dag2_asset],
    tags=["consumes", "asset-scheduled"],
) as dag4:
    BashOperator(
        outlets=[Asset("s3://consuming_2_task/asset_other_unknown.txt")],
        task_id="consuming_2",
        bash_command="sleep 5",
    )

with DAG(
    dag_id="asset_consumes_1_never_scheduled",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=[
        dag1_asset,
        Asset("s3://unrelated/this-asset-doesnt-get-triggered"),
    ],
    tags=["consumes", "asset-scheduled"],
) as dag5:
    BashOperator(
        outlets=[Asset("s3://consuming_2_task/asset_other_unknown.txt")],
        task_id="consuming_3",
        bash_command="sleep 5",
    )

with DAG(
    dag_id="asset_consumes_unknown_never_scheduled",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=[
        Asset("s3://unrelated/asset3.txt"),
        Asset("s3://unrelated/asset_other_unknown.txt"),
    ],
    tags=["asset-scheduled"],
) as dag6:
    BashOperator(
        task_id="unrelated_task",
        outlets=[Asset("s3://unrelated_task/asset_other_unknown.txt")],
        bash_command="sleep 5",
    )

with DAG(
    dag_id="consume_1_and_2_with_asset_expressions",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=(dag1_asset & dag2_asset),
) as dag5:
    BashOperator(
        outlets=[Asset("s3://consuming_2_task/asset_other_unknown.txt")],
        task_id="consume_1_and_2_with_asset_expressions",
        bash_command="sleep 5",
    )
with DAG(
    dag_id="consume_1_or_2_with_asset_expressions",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=(dag1_asset | dag2_asset),
) as dag6:
    BashOperator(
        outlets=[Asset("s3://consuming_2_task/asset_other_unknown.txt")],
        task_id="consume_1_or_2_with_asset_expressions",
        bash_command="sleep 5",
    )
with DAG(
    dag_id="consume_1_or_both_2_and_3_with_asset_expressions",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=(dag1_asset | (dag2_asset & dag3_asset)),
) as dag7:
    BashOperator(
        outlets=[Asset("s3://consuming_2_task/asset_other_unknown.txt")],
        task_id="consume_1_or_both_2_and_3_with_asset_expressions",
        bash_command="sleep 5",
    )
with DAG(
    dag_id="conditional_asset_and_time_based_timetable",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=AssetOrTimeSchedule(
        timetable=CronTriggerTimetable("0 1 * * 3", timezone="UTC"),
        assets=(dag1_asset & dag2_asset),
    ),
    tags=["asset-time-based-timetable"],
) as dag8:
    BashOperator(
        outlets=[Asset("s3://asset_time_based/asset_other_unknown.txt")],
        task_id="conditional_asset_and_time_based_timetable",
        bash_command="sleep 5",
    )
