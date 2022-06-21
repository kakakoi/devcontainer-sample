import strawberry
from strawberry.fastapi import GraphQLRouter

from app.domain.tasks.resolvers import add_task, delete_task, get_task, get_tasks, update_task
from app.domain.tasks.types import TaskType


@strawberry.type
class Query:
    task: TaskType = strawberry.field(resolver=get_task)
    tasks: list[TaskType] = strawberry.field(resolver=get_tasks)


@strawberry.type
class Mutation:
    task_add: TaskType = strawberry.field(resolver=add_task)
    task_update: TaskType = strawberry.field(resolver=update_task)
    task_delete: TaskType = strawberry.field(resolver=delete_task)


schema = strawberry.Schema(query=Query, mutation=Mutation)


graphql_router = GraphQLRouter(schema)
