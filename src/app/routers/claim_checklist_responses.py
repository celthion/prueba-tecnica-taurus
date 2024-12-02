# app/routers/claim_checklist_responses.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/claim-checklist-responses",
    tags=["claim_checklist_responses"],
)

@router.get("/", response_model=List[schemas.TbClaimChecklistResponses])
def read_responses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    responses = crud.claim_checklist_responses.get_responses(db, skip=skip, limit=limit)
    return responses

@router.get("/{response_id}", response_model=schemas.TbClaimChecklistResponses)
def read_response(response_id: int, db: Session = Depends(get_db)):
    db_response = crud.claim_checklist_responses.get_response(db, response_id=response_id)
    if db_response is None:
        raise HTTPException(status_code=404, detail="Response not found")
    return db_response

@router.post("/", response_model=schemas.TbClaimChecklistResponses)
def create_response(response: schemas.TbClaimChecklistResponsesCreate, db: Session = Depends(get_db)):
    return crud.claim_checklist_responses.create_response(db=db, response=response)

@router.put("/{response_id}", response_model=schemas.TbClaimChecklistResponses)
def update_response(response_id: int, response: schemas.TbClaimChecklistResponsesUpdate, db: Session = Depends(get_db)):
    db_response = crud.claim_checklist_responses.update_response(db, response_id=response_id, response=response)
    if db_response is None:
        raise HTTPException(status_code=404, detail="Response not found")
    return db_response

@router.delete("/{response_id}", response_model=schemas.TbClaimChecklistResponses)
def delete_response(response_id: int, db: Session = Depends(get_db)):
    db_response = crud.claim_checklist_responses.delete_response(db, response_id=response_id)
    if db_response is None:
        raise HTTPException(status_code=404, detail="Response not found")
    return db_response
