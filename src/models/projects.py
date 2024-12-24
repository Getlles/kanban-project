from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from src.models.columns import Columns


class Project(BaseModel):
    id: int
    name: str
    description: str | None
    created_at: datetime
    updated_at: datetime
    columns: Optional[List[Columns]]

    
class CreateProject(BaseModel):
    name: str
    description: str | None


class UpdProject(BaseModel):
    id: int
    name: str | None
    description: str | None