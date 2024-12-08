from pydantic import BaseModel
from datetime import datetime

class Project(BaseModel):
    id: int
    name: str
    description: str
    # created_at: str
    # update_at: str