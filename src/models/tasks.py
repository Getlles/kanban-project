from pydantic import BaseModel
from datetime import datetime

class Tasks(BaseModel):
    id: int
    column_id: int
    title: str
    description: str | None
    created_at: datetime
    updated_at: datetime


class CreateTasks(BaseModel):
    column_id: int
    title: str
    description: str | None


class UpdTasks(BaseModel):
    new_column_id: int | None
    title: str | None
    description: str | None