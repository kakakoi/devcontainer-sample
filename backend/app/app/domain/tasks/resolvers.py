import strawberry

from app.domain.tasks.inputs import AddTaskInput, UpdateTaskInput
from app.domain.tasks.repositories import InMemoryRepository
from app.domain.tasks.services import TaskService
from app.domain.tasks.types import TaskType


def get_task(id: strawberry.ID) -> TaskType:
    db = InMemoryRepository
    service = TaskService(db)
    task = service.find(id)

    return TaskType.from_instance(task)


def get_tasks() -> list[TaskType]:
    db = InMemoryRepository
    service = TaskService(db)
    tasks = service.find_all()

    return [TaskType.from_instance(task) for task in tasks]


def add_task(task_input: AddTaskInput) -> TaskType:
    db = InMemoryRepository
    service = TaskService(db)
    task = service.create(**task_input.__dict__)

    return TaskType.from_instance(task)


def update_task(task_input: UpdateTaskInput) -> TaskType:
    db = InMemoryRepository
    service = TaskService(db)
    task = service.update(**task_input.__dict__)

    return TaskType.from_instance(task)


def delete_task(id: strawberry.ID) -> TaskType:
    db = InMemoryRepository
    service = TaskService(db)
    task = service.delete(id)

    return TaskType.from_instance(task)
