from typing import List
from models.jobs import Jobs, JobIn
from models.user import User
from repositories.jobs import JobRepository
from fastapi import APIRouter, Depends, HTTPException, status
from .depends import get_job_repository, get_current_user

router = APIRouter()

@router.get("/", response_model=List[Jobs])
async def read_jobs(
    limit: int=100,
    skip: int=0,
    jobs: JobRepository = Depends(get_job_repository)):
    return await jobs.get_all(limit=limit, skip=skip)
    
@router.post("/", response_model=Jobs)
async def create_job(
    j: JobIn,
    jobs: JobRepository = Depends(get_job_repository),
    curent_user: User = Depends(get_current_user)):
    return await jobs.create(user_id=curent_user.id, j=j)

@router.put("/", response_model=Jobs)
async def update_job(
    id: int,
    j: JobIn, 
    jobs: JobRepository = Depends(get_job_repository),
    current_user: User = Depends(get_current_user)):
    job = await jobs.get_by_id(id=id)
    if job is None or jobs.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return await jobs.update(id=id, user_id=current_user.id, j=j)

@router.delete("/")
async def delete_job(
    id: int,
    jobs: JobRepository = Depends(get_job_repository),
    current_user: User = Depends(get_current_user)):
    job = await jobs.get_by_id(id=id)
    if job is None or jobs.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    await jobs.delete(id=id)
    return {"status": True}