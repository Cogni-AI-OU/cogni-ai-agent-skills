from __future__ import annotations

import pendulum

from airflow.sdk import DAG, task, task_group


# Creating Tasks
@task
def task_start():
    """Empty Task which is First Task of Dag"""
    return "[Task_start]"


@task
def task_1(value: int) -> str:
    """Empty Task1"""
    return f"[ Task1 {value} ]"


@task
def task_2(value: str) -> str:
    """Empty Task2"""
    return f"[ Task2 {value} ]"


@task
def task_3(value: str) -> None:
    """Empty Task3"""
    print(f"[ Task3 {value} ]")


@task
def task_end() -> None:
    """Empty Task which is Last Task of Dag"""
    print("[ Task_End  ]")


# Creating TaskGroups
@task_group
def task_group_function(value: int) -> None:
    """TaskGroup for grouping related Tasks"""
    task_3(task_2(task_1(value)))


# Executing Tasks and TaskGroups
with DAG(
    dag_id="example_task_group_decorator",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    start_task = task_start()
    end_task = task_end()
    for i in range(5):
        current_task_group = task_group_function(i)
        start_task >> current_task_group >> end_task
