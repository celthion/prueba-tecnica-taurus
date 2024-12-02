# app/routers/reports.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/reports",
    tags=["reports"],
)

@router.get("/metrics", response_model=schemas.ReportMetrics)
def get_report_metrics(db: Session = Depends(get_db)):
    metrics = crud.reports.get_report_metrics(db)
    if metrics is None:
        raise HTTPException(status_code=404, detail="Metrics not found")
    return metrics
