from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated
from src.models.columns import Columns, CreateColumns, UpdColumns
from src.crud.columns import create_column, get_columns, update_column, delete_column
from src.crud.users import get_user_by_username
from src.crud.projectUsers import get_projects_by_user
from src.crud.logs import create_log
from datetime import datetime

router = APIRouter()

@router.post("/{username}/{project_id}/new-column/")
async def add_column(username, project_id, column: Annotated[CreateColumns, Depends()]) -> dict:
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    projects = get_projects_by_user(user.id)
    for project in projects:
        if project.id == int(project_id):
            column_id = create_column(column)
            create_log(username, project_id, column_id, None, 'create', f'Column "{column.name}" created by {username} at {datetime.now()}.')
    return column

@router.get("/{username}/{project_id}/columns/", response_model=List[Columns])
async def get_all_columns(username, project_id) -> List[Columns]:
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    projects = get_projects_by_user(user.id)
    for project in projects:
        if project.id == int(project_id):
            columns = get_columns(int(project_id))
    return columns

@router.put("/{username}/{project_id}/columns/{column_id}")
async def modify_column(username, project_id,column_id, column: Annotated[UpdColumns, Depends()]) -> dict:
    try:
        user = get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404)
        projects = get_projects_by_user(user.id)
        for project in projects:
            if project.id == int(project_id):
                new_data = {
                    'name': column.name,
                    'position': column.position
                }
                update_column(column_id, new_data)
                create_log(username, project_id, column_id, None, 'update', f'Column "{column.name}" updated by {username} at {datetime.now()}.')
                return column
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{username}/{project_id}/columns/{column_id}", status_code=204)
def remove_column(username, project_id, column_id):
    try:
        user = get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404)
        projects = get_projects_by_user(user.id)
        for project in projects:
            if project.id == int(project_id):
                delete_column(column_id)
                create_log(username, project_id, column_id, None, 'delete', f'Column "{column_id}" deleted by {username} at {datetime.now()}.')
                return
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))