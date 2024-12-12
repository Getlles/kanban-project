from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated
from src.models.columns.columnsModel import Columns
from src.models.columns.createColumnsModel import CreateColumns
from src.models.columns.updateColumnsModel import UpdColumns
from src.crud.columnsCRUD import create_column, get_columns, update_column, delete_column

router = APIRouter()

@router.post("/columns/", response_model=Columns)
async def add_column(column: Annotated[CreateColumns, Depends()]) -> dict:
    create_column(column)
    return {"ok": True}

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
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/columns/{column_id}")
def remove_column(column_id: int):
    try:
        delete_column(column_id)
        return {"message": "Column deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))