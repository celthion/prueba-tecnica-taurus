# app/routers/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", response_model=List[schemas.TbUsers])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.users.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=schemas.TbUsers)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/", response_model=schemas.TbUsers)
def create_user(user: schemas.TbUsersCreate, db: Session = Depends(get_db)):
    return crud.users.create_user(db=db, user=user)

@router.put("/{user_id}", response_model=schemas.TbUsers)
def update_user(user_id: int, user: schemas.TbUsersUpdate, db: Session = Depends(get_db)):
    db_user = crud.users.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=schemas.TbUsers)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.users.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
