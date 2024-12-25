from fastapi import APIRouter, Depends, HTTPException
from src.models.tasks import Tasks, CreateTasks, UpdTasks
from typing import List, Annotated
from src.crud.tasks import create_task, get_tasks, update_task, delete_task
from src.crud.users import get_user_by_username
from src.crud.projectUsers import get_projects_by_user
from src.crud.columns import get_columns
from src.crud.logs import create_log
from datetime import datetime

router = APIRouter()

@router.post("/{username}/{project_id}/{column_id}/new-task/")
async def add_task(username, project_id, column_id, task: Annotated[CreateTasks, Depends()]) -> dict:
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    projects = get_projects_by_user(user.id)
    for project in projects:
        if project.id == int(project_id):
            columns = get_columns(int(project_id))
            for column in columns:
                if column.id == int(column_id):
                    task_id = create_task(task)
                    create_log(username, project_id, column_id, task_id, 'create', f'Task "{task.title}" created by {username} at {datetime.now()}.')
                    return task

@router.get("/{username}/{project_id}/{column_id}/tasks/", response_model=List[Tasks])
async def get_all_tasks(username, project_id, column_id) -> List[Tasks]:
    user = get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404)
    projects = get_projects_by_user(user.id)
    for project in projects:
        if project.id == int(project_id):
            columns = get_columns(int(project_id))
            for column in columns:
                if column.id == int(column_id):
                    tasks = get_tasks(column_id)
                    return tasks

@router.put("/{username}/{project_id}/{column_id}/tasks/{task_id}")
async def modify_task(username, project_id, column_id, task_id, task: Annotated[UpdTasks, Depends()]) -> dict:
    try:
        user = get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404)
        projects = get_projects_by_user(user.id)
        for project in projects:
            if project.id == int(project_id):
                columns = get_columns(int(project_id))
                for column in columns:
                    if column.id == int(column_id):
                        new_data = {
                            'new_column_id': task.new_column_id,
                            'title': task.title,
                            'description': task.description
                        }
                        update_task(task_id, new_data)
                        create_log(username, project_id, column_id, task_id, 'update', f'Task "{task.title}" updated by {username} at {datetime.now()}.')
                        return task
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/{username}/{project_id}/{column_id}/tasks/{task_id}", status_code=204)
async def remove_task(username, project_id, column_id, task_id):
    try:
        user = get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404)
        projects = get_projects_by_user(user.id)
        for project in projects:
            if project.id == int(project_id):
                columns = get_columns(int(project_id))
                for column in columns:
                    if column.id == int(column_id):
                        existing_tasks = get_tasks(column_id)
                        if not any(task.id == int(task_id) for task in existing_tasks):
                            raise HTTPException(status_code=404, detail="Task not found")
                        delete_task(task_id)
                        create_log(username, project_id, column_id, task_id, 'delete', f'Task "{task_id}" deleted by {username} at {datetime.now()}.')
                        return
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))