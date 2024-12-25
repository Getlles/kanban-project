from pydantic import BaseModel

class ProjectUser (BaseModel):
    project_id: int
    user_id: int