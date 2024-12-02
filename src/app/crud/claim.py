from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas

def get_claim(db: Session, claim_id: int):
    return db.query(models.TbClaim).filter(models.TbClaim.ClaimId_PK == claim_id).first()

def get_claims(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TbClaim).offset(skip).limit(limit).all()

def create_claim(db: Session, claim: schemas.TbClaimCreate):
    db_claim = models.TbClaim(**claim.dict())
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim

def update_claim(db: Session, claim_id: int, claim: schemas.TbClaimCreate):
    db_claim = get_claim(db, claim_id)
    if db_claim:
        for key, value in claim.dict().items():
            setattr(db_claim, key, value)
        db.commit()
        db.refresh(db_claim)
    return db_claim

def delete_claim(db: Session, claim_id: int):
    db_claim = get_claim(db, claim_id)
    if db_claim:
        db.delete(db_claim)
        db.commit()
    return db_claim
