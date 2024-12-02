# app/crud/claim_checklist_responses.py

from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas

def get_response(db: Session, response_id: int) -> Optional[models.TbClaimChecklistResponses]:
    return db.query(models.TbClaimChecklistResponses).filter(models.TbClaimChecklistResponses.id == response_id).first()

def get_responses(db: Session, skip: int = 0, limit: int = 100) -> List[models.TbClaimChecklistResponses]:
    return db.query(models.TbClaimChecklistResponses).offset(skip).limit(limit).all()

def create_response(db: Session, response: schemas.TbClaimChecklistResponsesCreate) -> models.TbClaimChecklistResponses:
    db_response = models.TbClaimChecklistResponses(**response.dict())
    db.add(db_response)
    db.commit()
    db.refresh(db_response)
    return db_response

def update_response(db: Session, response_id: int, response: schemas.TbClaimChecklistResponsesUpdate) -> Optional[models.TbClaimChecklistResponses]:
    db_response = get_response(db, response_id)
    if db_response:
        for key, value in response.dict(exclude_unset=True).items():
            setattr(db_response, key, value)
        db.commit()
        db.refresh(db_response)
        return db_response
    return None

def delete_response(db: Session, response_id: int) -> Optional[models.TbClaimChecklistResponses]:
    db_response = get_response(db, response_id)
    if db_response:
        db.delete(db_response)
        db.commit()
        return db_response
    return None
