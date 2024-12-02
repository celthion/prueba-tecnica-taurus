# app/crud/claim_checklist_tasks.py

from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas

def get_task(db: Session, task_id: int) -> Optional[models.TbClaimChecklistTasks]:
    return db.query(models.TbClaimChecklistTasks).filter(models.TbClaimChecklistTasks.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[models.TbClaimChecklistTasks]:
    return db.query(models.TbClaimChecklistTasks).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TbClaimChecklistTasksCreate) -> models.TbClaimChecklistTasks:
    db_task = models.TbClaimChecklistTasks(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: schemas.TbClaimChecklistTasksUpdate) -> Optional[models.TbClaimChecklistTasks]:
    db_task = get_task(db, task_id)
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete_task(db: Session, task_id: int) -> Optional[models.TbClaimChecklistTasks]:
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return db_task
    return None
