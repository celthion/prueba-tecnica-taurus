# app/routers/groupings.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/groupings",
    tags=["groupings"],
)

@router.get("/by_company", response_model=List[schemas.CompanyGrouping])
def get_grouping_by_company(db: Session = Depends(get_db)):
    data = crud.groupings.get_grouping_by_company(db)
    return data

@router.get("/by_agent", response_model=List[schemas.AgentGrouping])
def get_grouping_by_agent(db: Session = Depends(get_db)):
    data = crud.groupings.get_grouping_by_agent(db)
    return data

@router.get("/by_state", response_model=List[schemas.StateGrouping])
def get_grouping_by_state(db: Session = Depends(get_db)):
    data = crud.groupings.get_grouping_by_state(db)
    return data
