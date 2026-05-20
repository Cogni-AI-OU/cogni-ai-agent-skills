from __future__ import annotations

import pendulum

from airflow.sdk import DAG, Asset, AssetAlias, task

with DAG(
    dag_id="asset_s3_bucket_producer",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["producer", "asset"],
):

    @task(outlets=[Asset("s3://bucket/my-task")])
    def produce_asset_events():
        pass

    produce_asset_events()

with DAG(
    dag_id="asset_alias_example_alias_producer",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["producer", "asset-alias"],
):

    @task(outlets=[AssetAlias("example-alias")])
    def produce_asset_events_through_asset_alias(*, outlet_events=None):
        bucket_name = "bucket"
        object_path = "my-task"
        outlet_events[AssetAlias("example-alias")].add(Asset(f"s3://{bucket_name}/{object_path}"))

    produce_asset_events_through_asset_alias()

with DAG(
    dag_id="asset_s3_bucket_consumer",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=[Asset("s3://bucket/my-task")],
    catchup=False,
    tags=["consumer", "asset"],
):

    @task
    def consume_asset_event():
        pass

    consume_asset_event()

with DAG(
    dag_id="asset_alias_example_alias_consumer",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=[AssetAlias("example-alias")],
    catchup=False,
    tags=["consumer", "asset-alias"],
):

    @task(inlets=[AssetAlias("example-alias")])
    def consume_asset_event_from_asset_alias(*, inlet_events=None):
        for event in inlet_events[AssetAlias("example-alias")]:
            print(event)

    consume_asset_event_from_asset_alias()
