from fastapi import APIRouter, HTTPException
from src.crud.logs import get_logs_by_project
from typing import List
from src.models.logs import Logs
from src.crud.users import get_user_by_username
from src.crud.projectUsers import get_projects_by_user

router = APIRouter()

@router.get("/{username}/{project_id}/messages/", response_model=List[str])
async def get_messages_by_project(username, project_id):
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    projects = get_projects_by_user(user.id)
    for project in projects:
        if project.id == int(project_id):
            logs = get_logs_by_project(project_id)
            if not logs:
                raise HTTPException(status_code=404, detail="No logs found for this project.")
            return logs