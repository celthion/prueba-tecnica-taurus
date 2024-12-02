# app/routers/policies.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/policies",
    tags=["policies"],
)

@router.get("/", response_model=List[schemas.TbPolicies])
def read_policies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    policies = crud.policies.get_policies(db, skip=skip, limit=limit)
    return policies

@router.get("/{policy_id}", response_model=schemas.TbPolicies)
def read_policy(policy_id: int, db: Session = Depends(get_db)):
    db_policy = crud.policies.get_policy(db, policy_id=policy_id)
    if db_policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return db_policy

@router.post("/", response_model=schemas.TbPolicies)
def create_policy(policy: schemas.TbPoliciesCreate, db: Session = Depends(get_db)):
    return crud.policies.create_policy(db=db, policy=policy)

@router.put("/{policy_id}", response_model=schemas.TbPolicies)
def update_policy(policy_id: int, policy: schemas.TbPoliciesUpdate, db: Session = Depends(get_db)):
    db_policy = crud.policies.update_policy(db, policy_id=policy_id, policy=policy)
    if db_policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return db_policy

@router.delete("/{policy_id}", response_model=schemas.TbPolicies)
def delete_policy(policy_id: int, db: Session = Depends(get_db)):
    db_policy = crud.policies.delete_policy(db, policy_id=policy_id)
    if db_policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return db_policy
