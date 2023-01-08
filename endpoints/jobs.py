from models.jobs import Jobs
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()

@router.get("/", response_model=Jobs)
async def read_jobs():
    return

async def create_job():
    return

async def update_job():
    return

async def delete_job():
    return