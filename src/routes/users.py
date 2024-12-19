from fastapi import APIRouter, Depends, HTTPException
from src.models.users.createUsers import CreateUsers
from src.models.users.users import Users
from typing import List, Annotated
from src.crud.users import create_user, get_users, delete_user

router = APIRouter()

@router.post("/users/")
async def add_user(user: Annotated[CreateUsers, Depends()]) -> dict:
    create_user(user)
    return user

@router.get("/users/", response_model=List[Users])
async def get_all_users() -> List[Users]:
    users = get_users()
    return users

@router.delete("/users/{id}", status_code=204)
async def remove_user(id: int):
    try:
        existing_user = get_users()
        if not any(user.id == id for user in existing_user):
            raise HTTPException(status_code=404, detail="User not found")
        delete_user(id)
        return
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))