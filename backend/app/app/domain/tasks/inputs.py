from typing import Optional

import strawberry

from app.domain.tasks.types import StatusType


@strawberry.input
class AddTaskInput:
    title: str
    description: Optional[str] = None


@strawberry.input
class UpdateTaskInput:
    id: strawberry.ID
    status: StatusType
