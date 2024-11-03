from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    owned_projects = relationship("Project", back_populates="owner")
    projects = relationship(
        "Project", secondary="user_projects", back_populates="members"
    )
