from pydantic import BaseModel

class Tasks(BaseModel):
    column_id: int
    title: str
    descriprion: str | None
    status: str