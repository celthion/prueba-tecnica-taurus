# app/routers/holdingcompanies.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/holdingcompanies",
    tags=["holdingcompanies"],
)

@router.get("/", response_model=List[schemas.TbHoldingCompanies])
def read_holdingcompanies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = crud.holdingcompanies.get_holdingcompanies(db, skip=skip, limit=limit)
    return companies

@router.get("/{company_id}", response_model=schemas.TbHoldingCompanies)
def read_holdingcompany(company_id: int, db: Session = Depends(get_db)):
    db_company = crud.holdingcompanies.get_holdingcompany(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Holding company not found")
    return db_company

@router.post("/", response_model=schemas.TbHoldingCompanies)
def create_holdingcompany(company: schemas.TbHoldingCompaniesCreate, db: Session = Depends(get_db)):
    return crud.holdingcompanies.create_holdingcompany(db=db, company=company)

@router.put("/{company_id}", response_model=schemas.TbHoldingCompanies)
def update_holdingcompany(company_id: int, company: schemas.TbHoldingCompaniesUpdate, db: Session = Depends(get_db)):
    db_company = crud.holdingcompanies.update_holdingcompany(db, company_id=company_id, company=company)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Holding company not found")
    return db_company

@router.delete("/{company_id}", response_model=schemas.TbHoldingCompanies)
def delete_holdingcompany(company_id: int, db: Session = Depends(get_db)):
    db_company = crud.holdingcompanies.delete_holdingcompany(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Holding company not found")
    return db_company
