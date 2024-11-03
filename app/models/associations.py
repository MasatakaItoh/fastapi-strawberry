from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

user_projects = Table(
    "user_projects",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("project_id", Integer, ForeignKey("projects.id")),
)