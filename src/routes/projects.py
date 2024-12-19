from fastapi import APIRouter, Depends, HTTPException
from src.models.projects.projects import Project
from src.models.projects.createProjects import CreateProject
from src.models.projects.updateProjects import UpdProject
from typing import List, Annotated
from src.crud.projects import create_project, get_projects, update_project, delete_project


router = APIRouter()

@router.post("/projects/")
async def add_project(project: Annotated[CreateProject, Depends()]) -> dict:
    create_project(project)
    return project

@router.get("/projects/", response_model=List[Project])
async def get_all_projects() -> List[Project]:
    projects = get_projects()
    return projects

@router.put("/projects/{id}")
async def modify_project(id: int, project: Annotated[UpdProject, Depends()]) -> dict:
    try:
        new_data = {
            'name': project.name,
            'description': project.description
        }
        update_project(id, new_data)
        return project
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/projects/{id}", status_code=204)
async def remove_project(id: int):
    try:
        existing_project = get_projects()
        if not any(project.id == id for project in existing_project):
            raise HTTPException(status_code=404, detail="Project not found")
        delete_project(id)
        return
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))