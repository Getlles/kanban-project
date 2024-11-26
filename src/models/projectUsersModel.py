from pydantic import BaseModel

class Project_users(BaseModel):
    project_id: int
    user_id: int