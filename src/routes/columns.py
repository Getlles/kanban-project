from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated
from src.models.columns.columns import Columns
from src.models.columns.createColumns import CreateColumns
from src.models.columns.updateColumns import UpdColumns
from src.crud.columns import create_column, get_columns, update_column, delete_column


router = APIRouter()

@router.post("/columns/")
async def add_column(column: Annotated[CreateColumns, Depends()]) -> dict:
    create_column(column)
    return column

@router.get("/columns/", response_model=List[Columns])
async def get_all_columns() -> List[Columns]:
    columns = get_columns()
    return columns

@router.put("/columns/{id}")
async def modify_column(id: int, column: Annotated[UpdColumns, Depends()]) -> dict:
    try:
        new_data = {
            'name': column.name,
            'position': column.position
        }
        update_column(id, new_data)
        return column
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/columns/{column_id}", status_code=204)
def remove_column(column_id: int):
    try:
        delete_column(column_id)
        return
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))