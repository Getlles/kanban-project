from pydantic import BaseModel


class UpdProject(BaseModel):
    id: int
    name: str | None
    description: str | None