from pydantic import BaseModel


class CreateColumns(BaseModel):
    project_id: int
    name: str
    position: int