# app/crud/reports.py

from sqlalchemy.orm import Session
from sqlalchemy import func, case, cast, Float
from .. import models, schemas

def get_report_metrics(db: Session):
    # Número total de cotizaciones (# Prospects)
    total_quotes = db.query(func.count(models.TbPolicies.Policy_No))\
        .filter(models.TbPolicies.s_PolicyStatusCode == 'Prospect')\
        .scalar() or 0

    # Número de nuevas cotizaciones de negocio (# Prospect NB)
    # Consideraremos como nuevas cotizaciones aquellas creadas en los últimos 30 días
    from datetime import datetime, timedelta
    today = datetime.today()
    thirty_days_ago = today - timedelta(days=30)

    quote_nb = db.query(func.count(models.TbPolicies.Policy_No))\
        .filter(
            models.TbPolicies.s_PolicyStatusCode == 'Prospect',
            models.TbPolicies.d_CreatedDate >= thirty_days_ago
        )\
        .scalar() or 0

    # Prima total de nuevas cotizaciones de negocio (Prospect NB Premium)
    quote_nb_premium = db.query(func.sum(models.TbPolicies.n_CitizenTotalPremium))\
        .filter(
            models.TbPolicies.s_PolicyStatusCode == 'Prospect',
            models.TbPolicies.d_CreatedDate >= thirty_days_ago
        )\
        .scalar() or 0.0

    # Prima promedio de nuevas cotizaciones de negocio (Average NB Premium)
    average_nb_premium = quote_nb_premium / quote_nb if quote_nb > 0 else 0.0

    # Porcentaje de conversión de cotizaciones (Prospect Conversion %)
    # Suponemos que una cotización se convierte en póliza si existe una póliza con el mismo Policy_No y s_PolicyStatusCode distinto de 'Prospect'
    converted_quotes = db.query(func.count(models.TbPolicies.Policy_No))\
        .filter(
            models.TbPolicies.s_PolicyStatusCode != 'Prospect',
            models.TbPolicies.Policy_No.in_(
                db.query(models.TbPolicies.Policy_No)
                .filter(models.TbPolicies.s_PolicyStatusCode == 'Prospect')
            )
        )\
        .scalar() or 0

    quote_conversion_percent = (converted_quotes / total_quotes * 100) if total_quotes > 0 else 0.0

    # Número de pólizas vigentes (# PIF)
    pif = db.query(func.count(models.TbPolicies.Policy_No))\
        .filter(models.TbPolicies.s_PolicyStatusCode == 'Active')\
        .scalar() or 0

    # Número de pólizas expiradas (Cancelled Policies)
    expired_policies = db.query(func.count(models.TbPolicies.Policy_No))\
        .filter(models.TbPolicies.s_PolicyStatusCode == 'Cancelled')\
        .scalar() or 0

    # Prima total de pólizas expiradas (Cancelled Premium)
    expired_premium = db.query(func.sum(models.TbPolicies.n_CitizenTotalPremium))\
        .filter(models.TbPolicies.s_PolicyStatusCode == 'Cancelled')\
        .scalar() or 0.0

    # Porcentaje de retención (Retention %)
    total_policies = pif + expired_policies
    retention_percent = (pif / total_policies * 100) if total_policies > 0 else 0.0

    metrics = schemas.ReportMetrics(
        total_quotes=total_quotes,
        quote_nb=quote_nb,
        quote_conversion_percent=quote_conversion_percent,
        quote_nb_premium=quote_nb_premium,
        average_nb_premium=average_nb_premium,
        pif=pif,
        expired_policies=expired_policies,
        expired_premium=expired_premium,
        retention_percent=retention_percent
    )

    return metrics
