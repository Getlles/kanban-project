from pydantic import BaseModel

class Columns(BaseModel):
    project_id: int
    name: str