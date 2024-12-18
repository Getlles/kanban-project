from pydantic import BaseModel


class UpdColumns(BaseModel):
    id: int
    name: str | None
    position: int | None