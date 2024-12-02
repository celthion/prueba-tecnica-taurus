# app/routers/claim_checklist_tasks.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/claim-checklist-tasks",
    tags=["claim_checklist_tasks"],
)

@router.get("/", response_model=List[schemas.TbClaimChecklistTasks])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.claim_checklist_tasks.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.get("/{task_id}", response_model=schemas.TbClaimChecklistTasks)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.claim_checklist_tasks.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.post("/", response_model=schemas.TbClaimChecklistTasks)
def create_task(task: schemas.TbClaimChecklistTasksCreate, db: Session = Depends(get_db)):
    return crud.claim_checklist_tasks.create_task(db=db, task=task)

@router.put("/{task_id}", response_model=schemas.TbClaimChecklistTasks)
def update_task(task_id: int, task: schemas.TbClaimChecklistTasksUpdate, db: Session = Depends(get_db)):
    db_task = crud.claim_checklist_tasks.update_task(db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/{task_id}", response_model=schemas.TbClaimChecklistTasks)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.claim_checklist_tasks.delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
