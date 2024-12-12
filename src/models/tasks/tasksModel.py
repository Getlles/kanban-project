from pydantic import BaseModel
from datetime import datetime

class Tasks(BaseModel):
    id: int
    column_id: int
    title: str
    description: str | None
    created_at: datetime
    updated_at: datetime