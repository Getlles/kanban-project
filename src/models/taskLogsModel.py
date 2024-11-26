from pydantic import BaseModel

class Project_users(BaseModel):
    task_id: int
    project_user_id: int
    action: str