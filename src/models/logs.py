from pydantic import BaseModel
from datetime import datetime

class Logs(BaseModel):
    id: int
    username: str
    project_id: int
    column_id: int | None
    task_id: int | None
    action: str
    time: datetime
    message: str