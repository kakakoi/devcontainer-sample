from copy import deepcopy
from typing import Any

from app.domain.tasks.models import Task


class InMemoryRepository:
    _store: dict[str, Any] = {}

    @classmethod
    def find_by_id(cls, id_: str) -> Task:
        task = cls._store.get(id_)
        if task is None:
            raise Exception("Not Found")

        return task

    @classmethod
    def find_all(cls) -> list[Task]:
        tasks = list(cls._store.values())

        return tasks

    @classmethod
    def save(cls, task: Task) -> None:
        cls._store[str(task.id)] = deepcopy(task)

    @classmethod
    def delete(cls, task: Task) -> None:
        del cls._store[str(task.id)]
