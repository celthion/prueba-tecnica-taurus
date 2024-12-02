# app/crud/groupings.py

from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models, schemas

def get_grouping_by_company(db: Session):
    data = db.query(
        models.TbPolicies.n_IssueCompanyID_FK.label('company_id'),
        func.count(models.TbPolicies.Policy_No).label('policy_count'),
        func.coalesce(func.sum(models.TbPolicies.n_CitizenTotalPremium), 0.0).label('total_premium')
    ).group_by(models.TbPolicies.n_IssueCompanyID_FK).all()
    return data

def get_grouping_by_agent(db: Session):
    data = db.query(
        models.TbPolicies.n_AgencyAccount_FK.label('agent_id'),
        func.count(models.TbPolicies.Policy_No).label('policy_count'),
        func.coalesce(func.sum(models.TbPolicies.n_CitizenTotalPremium), 0.0).label('total_premium')
    ).group_by(models.TbPolicies.n_AgencyAccount_FK).all()
    return data

def get_grouping_by_state(db: Session):
    data = db.query(
        models.TbPolicies.s_PolicyStatusCode.label('state_code'),
        func.count(models.TbPolicies.Policy_No).label('policy_count'),
        func.coalesce(func.sum(models.TbPolicies.n_CitizenTotalPremium), 0.0).label('total_premium')
    ).group_by(models.TbPolicies.s_PolicyStatusCode).all()
    return data
