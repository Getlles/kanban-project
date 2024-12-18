from pydantic import BaseModel
from datetime import datetime


class Project(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime