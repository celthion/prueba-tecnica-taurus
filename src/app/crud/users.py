# app/crud/users.py

from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas

def get_user(db: Session, user_id: int) -> Optional[models.TbUsers]:
    return db.query(models.TbUsers).filter(models.TbUsers.Admin_ID == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.TbUsers]:
    return db.query(models.TbUsers).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.TbUsersCreate) -> models.TbUsers:
    db_user = models.TbUsers(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.TbUsersUpdate) -> Optional[models.TbUsers]:
    db_user = get_user(db, user_id)
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def delete_user(db: Session, user_id: int) -> Optional[models.TbUsers]:
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None
