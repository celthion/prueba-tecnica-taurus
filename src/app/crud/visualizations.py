from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import models, schemas

def get_time_series_data(db: Session):
    data = db.query(
        func.date_format(models.TbPolicies.d_CreatedDate, '%Y-%m').label('date'),
        func.count(models.TbPolicies.Policy_No).label('policy_count'),
        func.coalesce(func.sum(models.TbPolicies.n_CitizenTotalPremium), 0.0).label('total_premium')
    ).group_by(func.date_format(models.TbPolicies.d_CreatedDate, '%Y-%m')).order_by(func.date_format(models.TbPolicies.d_CreatedDate, '%Y-%m')).all()
    

    return data