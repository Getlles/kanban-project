from pydantic import BaseModel

class Columns(BaseModel):
    id: int
    project_id: int
    name: str
    position: int