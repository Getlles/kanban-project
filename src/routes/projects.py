from fastapi import APIRouter, HTTPException, status, Depends
from src.models.projects import Project, CreateProject, UpdProject
from typing import List, Annotated
from src.crud.projects import create_project, update_project, delete_project
from src.crud.users import get_user_by_username
from src.crud.projectUsers import get_projects_by_user, add_user_to_project, delete_user_from_project

router = APIRouter()

@router.get("/{username}/projects", response_model=List[Project])
async def get_user_projects(username):
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    projects = get_projects_by_user(user.id)
    return projects

@router.get("/{username}/{id}", response_model=Project)
async def retrieve_projects(username, id) -> Project:
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    projects = get_projects_by_user(user.id)
    for project in projects:
        if project.id == int(id):
            return project
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/{username}/new-project")
async def add_project(username, project: Annotated[CreateProject, Depends()]) -> dict:
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    project_id = create_project(project)
    add_user_to_project(project_id, user.id)
    return project

@router.put("/{username}/project/{id}")
async def modify_project(username, id, project: Annotated[UpdProject, Depends()]) -> dict:
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    projects = get_projects_by_user(user.id)
    for existing_project in projects:
        if existing_project.id == int(id):
            try:
                new_data = {
                    'name': project.name,
                    'description': project.description
                }
                update_project(id, new_data)
                return project
            except Exception as e:
                raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{username}/project-delete/{id}", status_code=204)
async def remove_project(username, id):
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    projects = get_projects_by_user(user.id)
    for existing_project in projects:
        if existing_project.id == int(id):
            delete_user_from_project(user.id, existing_project.id)
            delete_project(id)
            return
        
@router.post("/{username}/project/{project_id}/add-user/{user_id}", status_code=204)
async def add_user_to_existing_project(username: str, project_id: int, user_id: int):
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User  not found.")
    projects = get_projects_by_user(user.id)
    if not any(project.id == project_id for project in projects):
        raise HTTPException(status_code=404, detail="Project not found.")
    add_user_to_project(project_id, user_id)
    return

@router.delete("/{username}/project/{project_id}/remove-user/{user_id}", status_code=204)
async def remove_user_from_existing_project(username: str, project_id: int, user_id: int):
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User  not found.")
    projects = get_projects_by_user(user.id)
    if not any(project.id == project_id for project in projects):
        raise HTTPException(status_code=404, detail="Project not found.")
    delete_user_from_project(user_id, project_id)
    return