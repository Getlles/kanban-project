from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated, Dict
from src.models.projectUsersModel import Project_users
from src.crud.projectUsersCRUD import create_project_user, get_project_users, delete_project_user
from src.crud.projectsCRUD import get_projects
from src.crud.usersCRUD import get_users

router = APIRouter()

@router.post("/projectusers/", response_model=Project_users)
async def add_user(projectuser: Annotated[Project_users, Depends()]) -> dict:
    create_project_user(projectuser)
    return {"ok": True}

@router.get("/projectusers/", response_model=List[Project_users])
async def get_all_projectusers() -> List[Project_users]:
    users = get_project_users()
    return users

@router.delete("/projectusers/", response_model=dict)
async def remove_user(project_name: str, username: str) -> dict:
    try:
        delete_project_user(project_name, username)
        return {"ok": True, "message": "Project user deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))