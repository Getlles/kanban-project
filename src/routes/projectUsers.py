from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated, Dict
from src.models.project_users.projectUsers import Project_users
from src.crud.projectUsers import create_project_user, get_project_users, delete_project_user

router = APIRouter()

@router.post("/projectusers/")
async def add_user(projectuser: Annotated[Project_users, Depends()]) -> dict:
    create_project_user(projectuser)
    return projectuser

@router.get("/projectusers/", response_model=List[Project_users])
async def get_all_projectusers() -> List[Project_users]:
    users = get_project_users()
    return users

@router.delete("/projectusers/", status_code=204)
async def remove_user(project_id: int, user_id: int):
    try:
        delete_project_user(project_id, user_id)
        return
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))