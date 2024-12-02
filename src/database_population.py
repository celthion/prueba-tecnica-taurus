import pandas as pd
import numpy as np
import asyncio
from databases import Database
from src.config.env import TAURUS_CONNECTION_URL
from src.config.logger import logger

# Conexión a la base de datos
database = Database(TAURUS_CONNECTION_URL)

async def cargar_datos():
    await database.connect()
    logger.info("Conexión a la base de datos establecida")
    
    # Deshabilitar las restricciones de claves foráneas
    await database.execute("SET FOREIGN_KEY_CHECKS = 0;")
    logger.info("Restricciones de claves foráneas deshabilitadas")
    
    await cargar_tb_claim()
    await cargar_tb_claim_checklist_tasks()
    await cargar_tb_claim_checklist_responses()
    await cargar_tb_holdingcompanies()
    await cargar_tb_policies()
    await cargar_tb_poriskadditionalfloodinfos()
    await cargar_tb_users()
    
    # Habilitar nuevamente las restricciones de claves foráneas
    await database.execute("SET FOREIGN_KEY_CHECKS = 1;")
    logger.info("Restricciones de claves foráneas habilitadas")
    
    await database.disconnect()
    logger.info("Conexión a la base de datos cerrada")

async def cargar_tb_claim():
    df_claim = pd.read_csv('src/data/tb_claim.csv')
    
    # Convertir columnas datetime y manejar NaT
    datetime_columns = [
        'Date_Of_Loss', 'Inserted_Date', 'Updated_Date', 'Date_Allocated',
        'Date_First_Visited', 'Date_Close', 'd_PrimaryAttoryAssignDate',
        'd_CoAttoryAssignDate'
    ]
    for col in datetime_columns:
        df_claim[col] = pd.to_datetime(df_claim[col], errors='coerce')
    
    # Convertir columnas booleanas
    boolean_columns = [
        'Attorney_Involved_YN', 'PA_Involved_YN', 'DFS_Complain_YN', 'Catastrophe_YN'
    ]
    for col in boolean_columns:
        df_claim[col] = df_claim[col].map({'Y': 'Y', 'N': 'N'}).fillna('N')
    
    logger.info("Datos de tb_claim cargados desde CSV")

    # Seleccionar todas las columnas
    columns = [
        'ClaimId_PK', 'Claim_No', 'Risk_Id', 'n_TermMaster_FK', 'n_potransaction_FK',
        'Policy_No_SimpleSolve', 'n_PolicyNoId_FK', 'n_PORiskMasterFK', 'Date_Of_Loss',
        'Insured_Name', 'n_InsuredPersonInfoId_FK', 'Agency_Name', 'n_AgencyPersoninfoId_FK',
        'n_AgencyAccount_FK', 'n_SubAgentPersoninfo_FK', 'Reported_By_PersonId_FK',
        'InHouseCounsel_Person_FK', 'Reported_By_PersonId_FK_Old', 'PA_PersonId_FK',
        'Reported_By_Deprecated', 'Reported_By_Relation_Code', 'ClaimTypeId_FK',
        'Loss_Type_Code', 'Amount_Claimed', 'Letter_URL_Path', 'Remarks',
        'Allocated_To_UserId_FK', 'Date_Allocated', 'Date_First_Visited',
        'Service_Repre_UserId_FK', 'Approval_Status_Code', 'Claim_Approved_UserId_FK',
        'Comment', 'Claim_Status_Code', 'Claim_SubStatus_Code', 'Date_Close',
        'Total_Paid_Amount', 'Total_Paid_Amt_New', 'Attorney_Involved_YN',
        'PA_Involved_YN', 'DFS_Complain_YN', 'Catastrophe_YN', 'Event_Name',
        'Data_Source', 'n_PrimaryAttorneyPersonId_FK', 'd_PrimaryAttoryAssignDate',
        'n_CoAttorneyPersonId_FK', 'd_CoAttoryAssignDate', 'n_Copytoclientfk',
        's_CountyCode', 'Inserted_UserId_FK', 'Inserted_Date', 'Updated_UserId_FK',
        'Updated_Date'
    ]
    df_claim = df_claim[columns]

    # Convertir el DataFrame a tipo 'object' para evitar problemas con tipos de datos
    df_claim = df_claim.astype(object)

    # Reemplazar NaN y NaT por None en todo el DataFrame
    df_claim = df_claim.where(pd.notnull(df_claim), None)

    query = """
    INSERT INTO tb_claim (
        ClaimId_PK, Claim_No, Risk_Id, n_TermMaster_FK, n_potransaction_FK,
        Policy_No_SimpleSolve, n_PolicyNoId_FK, n_PORiskMasterFK, Date_Of_Loss,
        Insured_Name, n_InsuredPersonInfoId_FK, Agency_Name, n_AgencyPersoninfoId_FK,
        n_AgencyAccount_FK, n_SubAgentPersoninfo_FK, Reported_By_PersonId_FK,
        InHouseCounsel_Person_FK, Reported_By_PersonId_FK_Old, PA_PersonId_FK,
        Reported_By_Deprecated, Reported_By_Relation_Code, ClaimTypeId_FK,
        Loss_Type_Code, Amount_Claimed, Letter_URL_Path, Remarks,
        Allocated_To_UserId_FK, Date_Allocated, Date_First_Visited,
        Service_Repre_UserId_FK, Approval_Status_Code, Claim_Approved_UserId_FK,
        Comment, Claim_Status_Code, Claim_SubStatus_Code, Date_Close,
        Total_Paid_Amount, Total_Paid_Amt_New, Attorney_Involved_YN,
        PA_Involved_YN, DFS_Complain_YN, Catastrophe_YN, Event_Name,
        Data_Source, n_PrimaryAttorneyPersonId_FK, d_PrimaryAttoryAssignDate,
        n_CoAttorneyPersonId_FK, d_CoAttoryAssignDate, n_Copytoclientfk,
        s_CountyCode, Inserted_UserId_FK, Inserted_Date, Updated_UserId_FK,
        Updated_Date
    ) VALUES (
        :ClaimId_PK, :Claim_No, :Risk_Id, :n_TermMaster_FK, :n_potransaction_FK,
        :Policy_No_SimpleSolve, :n_PolicyNoId_FK, :n_PORiskMasterFK, :Date_Of_Loss,
        :Insured_Name, :n_InsuredPersonInfoId_FK, :Agency_Name, :n_AgencyPersoninfoId_FK,
        :n_AgencyAccount_FK, :n_SubAgentPersoninfo_FK, :Reported_By_PersonId_FK,
        :InHouseCounsel_Person_FK, :Reported_By_PersonId_FK_Old, :PA_PersonId_FK,
        :Reported_By_Deprecated, :Reported_By_Relation_Code, :ClaimTypeId_FK,
        :Loss_Type_Code, :Amount_Claimed, :Letter_URL_Path, :Remarks,
        :Allocated_To_UserId_FK, :Date_Allocated, :Date_First_Visited,
        :Service_Repre_UserId_FK, :Approval_Status_Code, :Claim_Approved_UserId_FK,
        :Comment, :Claim_Status_Code, :Claim_SubStatus_Code, :Date_Close,
        :Total_Paid_Amount, :Total_Paid_Amt_New, :Attorney_Involved_YN,
        :PA_Involved_YN, :DFS_Complain_YN, :Catastrophe_YN, :Event_Name,
        :Data_Source, :n_PrimaryAttorneyPersonId_FK, :d_PrimaryAttoryAssignDate,
        :n_CoAttorneyPersonId_FK, :d_CoAttoryAssignDate, :n_Copytoclientfk,
        :s_CountyCode, :Inserted_UserId_FK, :Inserted_Date, :Updated_UserId_FK,
        :Updated_Date
    )
    """

    try:
        await database.execute_many(query=query, values=df_claim.to_dict(orient='records'))
        logger.info("Datos de tb_claim insertados en la base de datos")
    except Exception as e:
        logger.error(f"Error al insertar datos en tb_claim: {e}")

async def cargar_tb_claim_checklist_tasks():
    df_tasks = pd.read_csv('src/data/tb_claim_checklist_tasks.csv')
    df_tasks['is_active'] = df_tasks['is_active'].map({'YES': True, 'NO': False})
    
    # Convertir columnas datetime y manejar NaT
    datetime_columns = ['created_at', 'updated_at']
    for col in datetime_columns:
        df_tasks[col] = pd.to_datetime(df_tasks[col], errors='coerce')
    
    logger.info("Datos de tb_claim_checklist_tasks cargados desde CSV")

    columns = [
        'id', 'task_title', 'description', 'sequence_number', 'is_active',
        'created_by', 'created_at', 'updated_by', 'updated_at'
    ]
    df_tasks = df_tasks[columns]

    # Convertir el DataFrame a tipo 'object' para evitar problemas con tipos de datos
    df_tasks = df_tasks.astype(object)

    # Reemplazar NaN y NaT por None en todo el DataFrame
    df_tasks = df_tasks.where(pd.notnull(df_tasks), None)

    query = """
    INSERT INTO tb_claim_checklist_tasks (
        id, task_title, description, sequence_number, is_active,
        created_by, created_at, updated_by, updated_at
    ) VALUES (
        :id, :task_title, :description, :sequence_number, :is_active,
        :created_by, :created_at, :updated_by, :updated_at
    )
    """

    try:
        await database.execute_many(query=query, values=df_tasks.to_dict(orient='records'))
        logger.info("Datos de tb_claim_checklist_tasks insertados en la base de datos")
    except Exception as e:
        logger.error(f"Error al insertar datos en tb_claim_checklist_tasks: {e}")

async def cargar_tb_claim_checklist_responses():
    df_responses = pd.read_csv('src/data/tb_claim_checklist_responses.csv')
    df_responses['is_task_completed'] = df_responses['is_task_completed'].map({'Y': True, 'N': False})
    df_responses['system_assign'] = df_responses['system_assign'].map({'Y': 'Y', 'N': 'N'}).fillna('N')

    # Convertir columnas datetime y manejar NaT
    datetime_columns = ['due_date', 'created_at', 'updated_at']
    for col in datetime_columns:
        df_responses[col] = pd.to_datetime(df_responses[col], errors='coerce')
    
    logger.info("Datos de tb_claim_checklist_responses cargados desde CSV")

    columns = [
        'id', 'checklist_task_id', 'claim_id', 'due_date', 'checklist_owner_id',
        'is_task_completed', 'short_notes', 'system_assign', 'created_by',
        'created_at', 'updated_by', 'updated_at'
    ]
    df_responses = df_responses[columns]

    # Convertir el DataFrame a tipo 'object' para evitar problemas con tipos de datos
    df_responses = df_responses.astype(object)

    # Reemplazar NaN y NaT por None en todo el DataFrame
    df_responses = df_responses.where(pd.notnull(df_responses), None)

    query = """
    INSERT INTO tb_claim_checklist_responses (
        id, checklist_task_id, claim_id, due_date, checklist_owner_id,
        is_task_completed, short_notes, system_assign, created_by,
        created_at, updated_by, updated_at
    ) VALUES (
        :id, :checklist_task_id, :claim_id, :due_date, :checklist_owner_id,
        :is_task_completed, :short_notes, :system_assign, :created_by,
        :created_at, :updated_by, :updated_at
    )
    """

    try:
        await database.execute_many(query=query, values=df_responses.to_dict(orient='records'))
        logger.info("Datos de tb_claim_checklist_responses insertados en la base de datos")
    except Exception as e:
        logger.error(f"Error al insertar datos en tb_claim_checklist_responses: {e}")

async def cargar_tb_holdingcompanies():
    # Cargar los datos desde el archivo CSV
    df_holdingcompanies = pd.read_csv('src/data/tb_holdingcompanies.csv')
    logger.info("Datos de tb_holdingcompanies cargados desde CSV")

    # Definir las columnas que coinciden con la estructura del CREATE TABLE
    columns = [
        'n_HoldingCompanyId_PK', 's_HoldingCompanyCode', 's_HoldingCompanyName', 
        'n_Personinfo_FK', 'company_address', 'website_url', 'logo_url', 'phone_no', 
        'email', 'naic_number', 'metadata', 'payment_wesite_url', 'payment_mailling_address',
        'payment_overnight_address', 'start_time', 'end_time', 'primary_color', 
        'secondary_color', 'service_provider_logo', 'n_CreatedUser', 'd_CreatedDate',
        'n_UpdatedUser', 'd_UpdatedDate', 'n_EditVersion'
    ]

    # Seleccionar las columnas relevantes
    df_holdingcompanies = df_holdingcompanies[columns]

    # Convertir todo el DataFrame a tipo 'object' para evitar problemas de tipos de datos
    df_holdingcompanies = df_holdingcompanies.astype(object)

    # Reemplazar NaN y NaT por None en todo el DataFrame
    df_holdingcompanies = df_holdingcompanies.where(pd.notnull(df_holdingcompanies), None)

    # Consulta de inserción actualizada para incluir todas las columnas
    query = """
    INSERT INTO tb_holdingcompanies (
        n_HoldingCompanyId_PK, s_HoldingCompanyCode, s_HoldingCompanyName, 
        n_Personinfo_FK, company_address, website_url, logo_url, phone_no, 
        email, naic_number, metadata, payment_wesite_url, payment_mailling_address,
        payment_overnight_address, start_time, end_time, primary_color, 
        secondary_color, service_provider_logo, n_CreatedUser, d_CreatedDate,
        n_UpdatedUser, d_UpdatedDate, n_EditVersion
    ) VALUES (
        :n_HoldingCompanyId_PK, :s_HoldingCompanyCode, :s_HoldingCompanyName, 
        :n_Personinfo_FK, :company_address, :website_url, :logo_url, :phone_no, 
        :email, :naic_number, :metadata, :payment_wesite_url, :payment_mailling_address,
        :payment_overnight_address, :start_time, :end_time, :primary_color, 
        :secondary_color, :service_provider_logo, :n_CreatedUser, :d_CreatedDate,
        :n_UpdatedUser, :d_UpdatedDate, :n_EditVersion
    )
    """

    try:
        # Insertar los datos en la base de datos
        await database.execute_many(query=query, values=df_holdingcompanies.to_dict(orient='records'))
        logger.info("Datos de tb_holdingcompanies insertados en la base de datos")
    except Exception as e:
        logger.error(f"Error al insertar datos en tb_holdingcompanies: {e}")


async def cargar_tb_policies():
    df_policies = pd.read_csv('src/data/tb_policies.csv')

    # Convertir columnas datetime y manejar NaT
    datetime_columns = [
        'd_InceptionDate', 'd_BookingDate', 'n_RenewalTypeUpdateDate',
        'd_InceptionDate_SimpleSolve', 'd_InsuredLivingDate', 'd_PolicyOrigNBDate',
        'd_CreatedDate', 'd_UpdatedDate'
    ]
    for col in datetime_columns:
        df_policies[col] = pd.to_datetime(df_policies[col], errors='coerce')
    
    # Convertir columnas booleanas
    boolean_columns = ['s_ExtendedCoverage', 's_VmmCoverage']
    for col in boolean_columns:
        df_policies[col] = df_policies[col].map({'Y': 'Y', 'N': 'N'}).fillna('N')

    logger.info("Datos de tb_policies cargados desde CSV")

    columns = [
        'n_PolicyNoId_PK', 'Policy_No', 'Policy_No_Gfs', 'n_ProductId_FK',
        'n_OwnerId_FK', 'n_IssueCompanyID_FK', 's_IssueCountryCode',
        's_IssueStateCode', 'n_UnderwriterClient_FK', 's_QuoteNumber',
        'd_InceptionDate', 'n_BillAccountMaster_FK', 's_PolicyStatusCode',
        's_PolicyStatusReason', 'n_AgencyAccount_FK', 'n_SubAgentPersoninfo_FK',
        'n_LatestTermMasterFK', 'n_cancelTranFK', 's_RenewalTypeCode',
        'n_RenewalTypeUpdateBy', 'n_RenewalTypeUpdateDate', 's_NonRenewReasonCode',
        'd_BookingDate', 'Policy_No_SimpleSolve', 'd_InceptionDate_SimpleSolve',
        's_ExtendedCoverage', 's_VmmCoverage', 'n_CitizenTotalPremium',
        'n_CitizenTotalPremiumRenewal', 'd_InsuredLivingDate', 'd_PolicyOrigNBDate',
        's_Custom1', 'n_CreatedUser', 'd_CreatedDate', 'n_UpdatedUser',
        'd_UpdatedDate', 'n_EditVersion'
    ]
    df_policies = df_policies[columns]

    # Convertir el DataFrame a tipo 'object' para evitar problemas con tipos de datos
    df_policies = df_policies.astype(object)

    # Reemplazar NaN y NaT por None en todo el DataFrame
    df_policies = df_policies.where(pd.notnull(df_policies), None)

    query = """
    INSERT INTO tb_policies (
        n_PolicyNoId_PK, Policy_No, Policy_No_Gfs, n_ProductId_FK,
        n_OwnerId_FK, n_IssueCompanyID_FK, s_IssueCountryCode,
        s_IssueStateCode, n_UnderwriterClient_FK, s_QuoteNumber,
        d_InceptionDate, n_BillAccountMaster_FK, s_PolicyStatusCode,
        s_PolicyStatusReason, n_AgencyAccount_FK, n_SubAgentPersoninfo_FK,
        n_LatestTermMasterFK, n_cancelTranFK, s_RenewalTypeCode,
        n_RenewalTypeUpdateBy, n_RenewalTypeUpdateDate, s_NonRenewReasonCode,
        d_BookingDate, Policy_No_SimpleSolve, d_InceptionDate_SimpleSolve,
        s_ExtendedCoverage, s_VmmCoverage, n_CitizenTotalPremium,
        n_CitizenTotalPremiumRenewal, d_InsuredLivingDate, d_PolicyOrigNBDate,
        s_Custom1, n_CreatedUser, d_CreatedDate, n_UpdatedUser,
        d_UpdatedDate, n_EditVersion
    ) VALUES (
        :n_PolicyNoId_PK, :Policy_No, :Policy_No_Gfs, :n_ProductId_FK,
        :n_OwnerId_FK, :n_IssueCompanyID_FK, :s_IssueCountryCode,
        :s_IssueStateCode, :n_UnderwriterClient_FK, :s_QuoteNumber,
        :d_InceptionDate, :n_BillAccountMaster_FK, :s_PolicyStatusCode,
        :s_PolicyStatusReason, :n_AgencyAccount_FK, :n_SubAgentPersoninfo_FK,
        :n_LatestTermMasterFK, :n_cancelTranFK, :s_RenewalTypeCode,
        :n_RenewalTypeUpdateBy, :n_RenewalTypeUpdateDate, :s_NonRenewReasonCode,
        :d_BookingDate, :Policy_No_SimpleSolve, :d_InceptionDate_SimpleSolve,
        :s_ExtendedCoverage, :s_VmmCoverage, :n_CitizenTotalPremium,
        :n_CitizenTotalPremiumRenewal, :d_InsuredLivingDate, :d_PolicyOrigNBDate,
        :s_Custom1, :n_CreatedUser, :d_CreatedDate, :n_UpdatedUser,
        :d_UpdatedDate, :n_EditVersion
    )
    """

    try:
        await database.execute_many(query=query, values=df_policies.to_dict(orient='records'))
        logger.info("Datos de tb_policies insertados en la base de datos")
    except Exception as e:
        logger.error(f"Error al insertar datos en tb_policies: {e}")

async def cargar_tb_poriskadditionalfloodinfos():
    df_floodinfos = pd.read_csv('src/data/tb_poriskadditionalfloodinfos.csv')

    # Convertir columnas datetime y manejar NaT
    datetime_columns = [
        'd_PriorMapDate', 'd_PropertyPurchaseDt', 'd_FloodLoanClosingDt',
        'd_PriorNBDate', 'd_DateOfConstruction', 'd_CBRSOPADate',
        'd_InitialFirmDate', 'd_MobileHomeParkDate', 'd_CurrentFirmDate',
        'd_SuspensionDate', 'd_ReinstatementDate', 'd_SubstantialImprovmentDate',
        'd_CreatedDate', 'd_UpdatedDate'
    ]
    for col in datetime_columns:
        df_floodinfos[col] = pd.to_datetime(df_floodinfos[col], errors='coerce')

    # Convertir columnas booleanas si las hubiera (no se especificaron en este caso)

    logger.info("Datos de tb_poriskadditionalfloodinfos cargados desde CSV")

    columns = df_floodinfos.columns.tolist()
    df_floodinfos = df_floodinfos[columns]

    # Convertir el DataFrame a tipo 'object' para evitar problemas con tipos de datos
    df_floodinfos = df_floodinfos.astype(object)

    # Reemplazar NaN y NaT por None en todo el DataFrame
    df_floodinfos = df_floodinfos.where(pd.notnull(df_floodinfos), None)
    df_floodinfos = df_floodinfos.drop(columns=['metadata'])
    columns.remove('metadata')
    query = f"""
    INSERT INTO tb_poriskadditionalfloodinfos (
        {', '.join(columns)}
    ) VALUES (
        {', '.join([f":{col}" for col in columns])}
    )
    """

    try:
        await database.execute_many(query=query, values=df_floodinfos.to_dict(orient='records'))
        logger.info("Datos de tb_poriskadditionalfloodinfos insertados en la base de datos")
    except Exception as e:
        logger.error(f"Error al insertar datos en tb_poriskadditionalfloodinfos: {e}")

async def cargar_tb_users():
    df_users = pd.read_csv('src/data/tb_users.csv')

    # Convertir columnas datetime y manejar NaT
    datetime_columns = [
        'd_EffectiveDate', 'd_ExpiryDate', 's_PwdKeyExp', 'Created_On',
        'Closing_Date', 'Closing_Date_Crystal', 'Last_Timestamp',
        'd_CreatedDate', 'd_UpdatedDate'
    ]
    for col in datetime_columns:
        df_users[col] = pd.to_datetime(df_users[col], errors='coerce')
    
    # Convertir campos booleanos
    boolean_columns = ['s_IsAdmin', 'active', 'Login_FirstTime']
    for col in boolean_columns:
        df_users[col] = df_users[col].map({'Y': 'Y', 'N': 'N'}).fillna('N')

    logger.info("Datos de tb_users cargados desde CSV")

    columns = df_users.columns.tolist()
    df_users = df_users[columns]

    # Convertir el DataFrame a tipo 'object' para evitar problemas con tipos de datos
    df_users = df_users.astype(object)

    # Reemplazar NaN y NaT por None en todo el DataFrame
    df_users = df_users.where(pd.notnull(df_users), None)

    query = f"""
    INSERT INTO tb_users (
        {', '.join(columns)}
    ) VALUES (
        {', '.join([f":{col}" for col in columns])}
    )
    """

    try:
        await database.execute_many(query=query, values=df_users.to_dict(orient='records'))
        logger.info("Datos de tb_users insertados en la base de datos")
    except Exception as e:
        logger.error(f"Error al insertar datos en tb_users: {e}")

if __name__ == "__main__":
    asyncio.run(cargar_datos())
