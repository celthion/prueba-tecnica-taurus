# app/routers/claim.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/claims",
    tags=["claims"],
)

@router.get("/", response_model=List[schemas.TbClaim])
def read_claims(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    claims = crud.claim.get_claims(db, skip=skip, limit=limit)
    return claims

@router.get("/{claim_id}", response_model=schemas.TbClaim)
def read_claim(claim_id: int, db: Session = Depends(get_db)):
    db_claim = crud.claim.get_claim(db, claim_id=claim_id)
    if db_claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return db_claim

@router.post("/", response_model=schemas.TbClaim)
def create_claim(claim: schemas.TbClaimCreate, db: Session = Depends(get_db)):
    return crud.claim.create_claim(db=db, claim=claim)

@router.put("/{claim_id}", response_model=schemas.TbClaim)
def update_claim(claim_id: int, claim: schemas.TbClaimUpdate, db: Session = Depends(get_db)):
    db_claim = crud.claim.update_claim(db, claim_id=claim_id, claim=claim)
    if db_claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return db_claim

@router.delete("/{claim_id}", response_model=schemas.TbClaim)
def delete_claim(claim_id: int, db: Session = Depends(get_db)):
    db_claim = crud.claim.delete_claim(db, claim_id=claim_id)
    if db_claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return db_claim
