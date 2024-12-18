from pydantic import BaseModel


class UpdTasks(BaseModel):
    id: int
    column_id: int | None
    title: str | None
    description: str | None