from sqlalchemy.orm import Session
from strawberry import Info

from app.graphql.schemas import (
    UserPayload,
    UserCreateInput,
    ProjectCreateInput,
    ProjectPayload,
    UserInput,
    ProjectInput,
)

from app.models import User as UserModel, Project as ProjectModel

# User


def get_user(info: Info, input: UserInput) -> UserPayload:
    db: Session = info.context["db"]
    user = db.query(UserModel).filter(UserModel.id == input.id).first()

    if not user:
        raise Exception("User not found")

    return user


def create_user(info: Info, input: UserCreateInput) -> UserPayload:
    db: Session = info.context["db"]
    hashed_password = hash_password(input.password)
    user = UserModel(username=input.username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# Project


def get_project(info: Info, input: ProjectInput) -> ProjectPayload:
    db: Session = info.context["db"]
    project = db.query(ProjectModel).filter(ProjectModel.id == input.id).first()

    if not project:
        raise Exception("Project not found")

    return project


def create_project(info: Info, input: ProjectCreateInput) -> ProjectPayload:
    db: Session = info.context["db"]
    project = ProjectModel(
        name=input.name, description=input.description, owner_id=input.owner_id
    )
    db.add(project)
    db.commit()
    db.refresh(project)

    return project


# Utils


def hash_password(password: str) -> str:
    from passlib.hash import bcrypt

    return bcrypt.hash(password)
