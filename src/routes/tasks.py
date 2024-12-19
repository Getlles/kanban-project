from fastapi import APIRouter, Depends, HTTPException
from src.models.tasks.tasks import Tasks
from src.models.tasks.createTasks import CreateTasks
from src.models.tasks.updateTasks import UpdTasks
from typing import List, Annotated
from src.crud.tasks import create_task, get_tasks, update_task, delete_task

router = APIRouter()

@router.post("/tasks/")
async def add_task(task: Annotated[CreateTasks, Depends()]) -> dict:
    create_task(task)
    return task

@router.get("/tasks/", response_model=List[Tasks])
async def get_all_tasks() -> List[Tasks]:
    tasks = get_tasks()
    return tasks

@router.put("/tasks/{id}")
async def modify_task(id: int, task: Annotated[UpdTasks, Depends()]) -> dict:
    try:
        new_data = {
            'column_id': task.column_id,
            'title': task.title,
            'description': task.description
        }
        update_task(id, new_data)
        return task
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/tasks/{id}", status_code=204)
async def remove_task(id: int):
    try:
        existing_tasks = get_tasks()
        if not any(task.id == id for task in existing_tasks):
            raise HTTPException(status_code=404, detail="Task not found")
        delete_task(id)
        return
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))