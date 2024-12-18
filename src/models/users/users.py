from pydantic import BaseModel


class Users(BaseModel):
    id: int
    username: str
    email: str
    password_hash: str