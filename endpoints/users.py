from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from repositories.users import UserRepository
from models.user import User, UserIn
from .depends import get_user_repository, get_current_user

router = APIRouter()

@router.get("/", response_model=List[User])
async def read_users(
    users: UserRepository = Depends(get_user_repository),
    limits: int =100, 
    skip: int = 100):
    return await users.get_all(limit=limits, skip=0)

@router.post("/", response_model=User)
async def user_create(
    user: UserIn, 
    users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)

@router.put("/", response_model=User)
async def user_update(
    id: int,
    user: UserIn, 
    users: UserRepository = Depends(get_user_repository), 
    current_user: User = Depends(get_current_user)):
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.email != current_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return await users.update(id=id, u=user)