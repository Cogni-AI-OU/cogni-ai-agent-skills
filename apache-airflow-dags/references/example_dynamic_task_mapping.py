from __future__ import annotations

from datetime import datetime

from airflow.sdk import DAG, task, task_group

with DAG(dag_id="example_dynamic_task_mapping", schedule=None, start_date=datetime(2022, 3, 4)):

    @task
    def add_one(x: int):
        return x + 1

    @task
    def sum_it(values):
        total = sum(values)
        print(f"Total was {total}")

    added_values = add_one.expand(x=[1, 2, 3])
    sum_it(added_values)

with DAG(
    dag_id="example_task_mapping_second_order",
    schedule=None,
    catchup=False,
    start_date=datetime(2022, 3, 4),
):

    @task
    def get_nums():
        return [1, 2, 3]

    @task
    def times_2(num):
        return num * 2

    @task
    def add_10(num):
        return num + 10

    _get_nums = get_nums()
    _times_2 = times_2.expand(num=_get_nums)
    add_10.expand(num=_times_2)

with DAG(
    dag_id="example_task_group_mapping",
    schedule=None,
    catchup=False,
    start_date=datetime(2022, 3, 4),
):

    @task_group
    def op(num):
        @task
        def add_1(num):
            return num + 1

        @task
        def mul_2(num):
            return num * 2

        return mul_2(add_1(num))

    op.expand(num=[1, 2, 3])
