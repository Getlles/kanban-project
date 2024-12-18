from pydantic import BaseModel


class CreateTasks(BaseModel):
    column_id: int
    title: str
    description: str | None