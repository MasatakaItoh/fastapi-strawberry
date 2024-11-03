from typing import Optional

import strawberry


@strawberry.type
class Task:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    project_id: int
