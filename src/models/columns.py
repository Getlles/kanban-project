from pydantic import BaseModel
from typing import Optional, List
from src.models.tasks import Tasks

class Columns(BaseModel):
    id: int
    project_id: int
    name: str
    position: int
    tasks: Optional[List[Tasks]]


class CreateColumns(BaseModel):
    project_id: int
    name: str
    position: int


class UpdColumns(BaseModel):
    name: str | None
    position: int | None