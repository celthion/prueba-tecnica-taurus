# app/main.py

from fastapi import FastAPI
from .routers import (
    claim,
    users,
    claim_checklist_responses,
    claim_checklist_tasks,
    holdingcompanies,
    policies,
    poriskadditionalfloodinfos,
    reports,
    groupings,
    visualizations,
)
from .database import engine
from . import models
from fastapi.middleware.cors import CORSMiddleware

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Microservicio Taurus",
    description="API para interactuar con la base de datos Taurus",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Incluir los routers
app.include_router(claim.router)
app.include_router(users.router)
app.include_router(claim_checklist_responses.router)
app.include_router(claim_checklist_tasks.router)
app.include_router(holdingcompanies.router)
app.include_router(policies.router)
app.include_router(poriskadditionalfloodinfos.router)
app.include_router(reports.router)
app.include_router(groupings.router)
app.include_router(visualizations.router)