# app/routers/visualizations.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/visualizations",
    tags=["visualizations"],
)

@router.get("/time_series", response_model=List[schemas.TimeSeriesData])
def get_time_series_data(db: Session = Depends(get_db)):
    data = crud.visualizations.get_time_series_data(db)
    return data

