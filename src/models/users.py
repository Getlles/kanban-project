from pydantic import BaseModel, NameEmail
from typing import Optional, List
from src.models.projects import Project


class Users(BaseModel):
    id: int
    username: str
    email: NameEmail
    password: str
    projects: Optional[List[Project]]


class SignUsers(BaseModel):
    username: str
    email: str
    password: str