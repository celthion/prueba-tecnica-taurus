# app/routers/poriskadditionalfloodinfos.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/poriskadditionalfloodinfos",
    tags=["poriskadditionalfloodinfos"],
)

@router.get("/", response_model=List[schemas.TbPoRiskAdditionalFloodInfos])
def read_floodinfos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    floodinfos = crud.poriskadditionalfloodinfos.get_floodinfos(db, skip=skip, limit=limit)
    return floodinfos

@router.get("/{floodinfo_id}", response_model=schemas.TbPoRiskAdditionalFloodInfos)
def read_floodinfo(floodinfo_id: int, db: Session = Depends(get_db)):
    db_floodinfo = crud.poriskadditionalfloodinfos.get_floodinfo(db, floodinfo_id=floodinfo_id)
    if db_floodinfo is None:
        raise HTTPException(status_code=404, detail="Flood info not found")
    return db_floodinfo

@router.post("/", response_model=schemas.TbPoRiskAdditionalFloodInfos)
def create_floodinfo(floodinfo: schemas.TbPoRiskAdditionalFloodInfosCreate, db: Session = Depends(get_db)):
    return crud.poriskadditionalfloodinfos.create_floodinfo(db=db, floodinfo=floodinfo)

@router.put("/{floodinfo_id}", response_model=schemas.TbPoRiskAdditionalFloodInfos)
def update_floodinfo(floodinfo_id: int, floodinfo: schemas.TbPoRiskAdditionalFloodInfosUpdate, db: Session = Depends(get_db)):
    db_floodinfo = crud.poriskadditionalfloodinfos.update_floodinfo(db, floodinfo_id=floodinfo_id, floodinfo=floodinfo)
    if db_floodinfo is None:
        raise HTTPException(status_code=404, detail="Flood info not found")
    return db_floodinfo

@router.delete("/{floodinfo_id}", response_model=schemas.TbPoRiskAdditionalFloodInfos)
def delete_floodinfo(floodinfo_id: int, db: Session = Depends(get_db)):
    db_floodinfo = crud.poriskadditionalfloodinfos.delete_floodinfo(db, floodinfo_id=floodinfo_id)
    if db_floodinfo is None:
        raise HTTPException(status_code=404, detail="Flood info not found")
    return db_floodinfo
