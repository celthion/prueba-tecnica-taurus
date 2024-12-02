# app/crud/holdingcompanies.py

from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas

def get_holdingcompany(db: Session, company_id: int) -> Optional[models.TbHoldingCompanies]:
    return db.query(models.TbHoldingCompanies).filter(models.TbHoldingCompanies.n_HoldingCompanyId_PK == company_id).first()

def get_holdingcompanies(db: Session, skip: int = 0, limit: int = 100) -> List[models.TbHoldingCompanies]:
    return db.query(models.TbHoldingCompanies).offset(skip).limit(limit).all()

def create_holdingcompany(db: Session, company: schemas.TbHoldingCompaniesCreate) -> models.TbHoldingCompanies:
    db_company = models.TbHoldingCompanies(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def update_holdingcompany(db: Session, company_id: int, company: schemas.TbHoldingCompaniesUpdate) -> Optional[models.TbHoldingCompanies]:
    db_company = get_holdingcompany(db, company_id)
    if db_company:
        for key, value in company.dict(exclude_unset=True).items():
            setattr(db_company, key, value)
        db.commit()
        db.refresh(db_company)
        return db_company
    return None

def delete_holdingcompany(db: Session, company_id: int) -> Optional[models.TbHoldingCompanies]:
    db_company = get_holdingcompany(db, company_id)
    if db_company:
        db.delete(db_company)
        db.commit()
        return db_company
    return None
