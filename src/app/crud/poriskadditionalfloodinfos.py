# app/crud/poriskadditionalfloodinfos.py

from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas

def get_floodinfo(db: Session, floodinfo_id: int) -> Optional[models.TbPoRiskAdditionalFloodInfos]:
    return db.query(models.TbPoRiskAdditionalFloodInfos).filter(models.TbPoRiskAdditionalFloodInfos.n_PORiskAdditionalFloodInfo_PK == floodinfo_id).first()

def get_floodinfos(db: Session, skip: int = 0, limit: int = 100) -> List[models.TbPoRiskAdditionalFloodInfos]:
    return db.query(models.TbPoRiskAdditionalFloodInfos).offset(skip).limit(limit).all()

def create_floodinfo(db: Session, floodinfo: schemas.TbPoRiskAdditionalFloodInfosCreate) -> models.TbPoRiskAdditionalFloodInfos:
    db_floodinfo = models.TbPoRiskAdditionalFloodInfos(**floodinfo.dict())
    db.add(db_floodinfo)
    db.commit()
    db.refresh(db_floodinfo)
    return db_floodinfo

def update_floodinfo(db: Session, floodinfo_id: int, floodinfo: schemas.TbPoRiskAdditionalFloodInfosUpdate) -> Optional[models.TbPoRiskAdditionalFloodInfos]:
    db_floodinfo = get_floodinfo(db, floodinfo_id)
    if db_floodinfo:
        for key, value in floodinfo.dict(exclude_unset=True).items():
            setattr(db_floodinfo, key, value)
        db.commit()
        db.refresh(db_floodinfo)
        return db_floodinfo
    return None

def delete_floodinfo(db: Session, floodinfo_id: int) -> Optional[models.TbPoRiskAdditionalFloodInfos]:
    db_floodinfo = get_floodinfo(db, floodinfo_id)
    if db_floodinfo:
        db.delete(db_floodinfo)
        db.commit()
        return db_floodinfo
    return None
