from fastapi import APIRouter, Depends, HTTPException, status
from src.models.users import Users, SignUsers
from typing import List, Annotated
from src.crud.users import create_user, get_users, delete_user, get_user_by_email, get_user_by_username, check_user

router = APIRouter()

@router.get("/users/", response_model=List[Users])
async def get_all_users() -> List[Users]:
    users = get_users()
    return users

@router.post("/signup")
async def sign_new_user(data: Annotated[SignUsers, Depends()]) -> dict:
    existing_user_by_email = get_user_by_email(data.email)
    if existing_user_by_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    existing_user_by_username = get_user_by_username(data.username)
    if existing_user_by_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    create_user(data)
    return data

@router.post("/signin", status_code=202)
async def sign_user_in(user: Annotated[SignUsers, Depends()]) -> dict: 
    existing_user = check_user(user.username, user.email)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if user.password != existing_user.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return existing_user

@router.delete("/users/{id}", status_code=204)
async def remove_user(id):
    try:
        existing_user = get_users()
        if not any(user.id == id for user in existing_user):
            raise HTTPException(status_code=404)
        delete_user(id)
        return
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))