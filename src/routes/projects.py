from fastapi import APIRouter, Depends, HTTPException
from src.models.projects.projectsModel import Project
from src.models.projects.createProjectsModel import CreateProject
from src.models.projects.updateProjectsModel import UpdProject
from typing import List, Annotated
from src.crud.projectsCRUD import create_project, get_projects, update_project, delete_project

router = APIRouter()

@router.post("/projects/", response_model=Project)
async def add_project(project: Annotated[CreateProject, Depends()]) -> dict:
    create_project(project)
    return {"ok": True}

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
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/projects/{id}", response_model=Project)
async def remove_project(id: int) -> dict:
    try:
        existing_project = get_projects()
        if not any(project.id == id for project in existing_project):
            raise HTTPException(status_code=404, detail="Project not found")
        delete_project(id)
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))