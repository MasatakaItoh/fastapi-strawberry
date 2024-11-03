from typing import Optional, List

import strawberry

from app.graphql.schemas.tasks import Task
from app.graphql.schemas.users import User


@strawberry.type
class Project:
    id: int
    name: str
    description: Optional[str] = None
    owner = Optional[User]
    members = List[User] = []
    tasks = List[Task] = []
