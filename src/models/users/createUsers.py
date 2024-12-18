from pydantic import BaseModel


class CreateUsers(BaseModel):
    username: str
    email: str
    password_hash: str