from sqlalchemy.orm import Session
from strawberry import Info

from app.graphql.schemas import UserPayload, UserCreateInput
from app.graphql.types import User

from app.models import User as UserModel

# User


def get_user(info: Info, user_id: int) -> UserPayload:
    db: Session = info.context["db"]
    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if not user:
        raise Exception("User not found")

    return User(id=user.id, username=user.username)


def create_user(info: Info, input: UserCreateInput) -> UserPayload:
    db: Session = info.context["db"]
    hashed_password = hash_password(input.password)
    user = UserModel(username=input.username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)

    return User(id=user.id, username=user.username)


# Utils


def hash_password(password: str) -> str:
    from passlib.hash import bcrypt

    return bcrypt.hash(password)
