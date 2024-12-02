# app/crud/policies.py

from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas

def get_policy(db: Session, policy_id: int) -> Optional[models.TbPolicies]:
    return db.query(models.TbPolicies).filter(models.TbPolicies.n_PolicyNoId_PK == policy_id).first()

def get_policies(db: Session, skip: int = 0, limit: int = 100) -> List[models.TbPolicies]:
    return db.query(models.TbPolicies).offset(skip).limit(limit).all()

def create_policy(db: Session, policy: schemas.TbPoliciesCreate) -> models.TbPolicies:
    db_policy = models.TbPolicies(**policy.dict())
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy

def update_policy(db: Session, policy_id: int, policy: schemas.TbPoliciesUpdate) -> Optional[models.TbPolicies]:
    db_policy = get_policy(db, policy_id)
    if db_policy:
        for key, value in policy.dict(exclude_unset=True).items():
            setattr(db_policy, key, value)
        db.commit()
        db.refresh(db_policy)
        return db_policy
    return None

def delete_policy(db: Session, policy_id: int) -> Optional[models.TbPolicies]:
    db_policy = get_policy(db, policy_id)
    if db_policy:
        db.delete(db_policy)
        db.commit()
        return db_policy
    return None
