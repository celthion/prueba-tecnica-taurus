from src.config.env import INITIAL_CONNECTION_URL
from databases import Database
import asyncio
from src.config.logger import logger

# Crear una instancia de la base de datos con la URL de conexión inicial
database = Database(INITIAL_CONNECTION_URL)

# Definición del esquema SQL para crear la base de datos y las tablas
schema_sql = """
CREATE DATABASE IF NOT EXISTS taurus;
USE taurus;

CREATE TABLE tb_claim (
    ClaimId_PK INT PRIMARY KEY,
    Claim_No INT NOT NULL,
    Risk_Id INT,
    n_TermMaster_FK INT,
    n_potransaction_FK INT,
    n_PolicyNoId_FK INT,
    n_PORiskMasterFK INT,
    Date_Of_Loss DATE,
    Insured_Name TEXT,
    Agency_Name TEXT,
    n_AgencyAccount_FK INT,
    Loss_Type_Code TEXT,
    Total_Paid_Amount DECIMAL(10, 2),
    Claim_Status_Code TEXT,
    Claim_SubStatus_Code TEXT,
    Inserted_Date DATETIME,
    Updated_Date DATETIME,

    Policy_No_SimpleSolve TEXT,
    n_InsuredPersonInfoId_FK INT,
    n_AgencyPersoninfoId_FK INT,
    n_SubAgentPersoninfo_FK INT,
    Reported_By_PersonId_FK INT,
    InHouseCounsel_Person_FK INT,
    Reported_By_PersonId_FK_Old INT,
    PA_PersonId_FK INT,
    Reported_By_Deprecated TEXT,
    Reported_By_Relation_Code TEXT,
    ClaimTypeId_FK INT,
    Amount_Claimed DECIMAL(10, 2),
    Letter_URL_Path TEXT,
    Remarks TEXT,
    Allocated_To_UserId_FK INT,
    Date_Allocated DATETIME,
    Date_First_Visited DATETIME,
    Service_Repre_UserId_FK INT,
    Approval_Status_Code TEXT,
    Claim_Approved_UserId_FK INT,
    Comment TEXT,
    Date_Close DATETIME,
    Total_Paid_Amt_New DECIMAL(10, 2),
    Attorney_Involved_YN CHAR(1),
    PA_Involved_YN CHAR(1),
    DFS_Complain_YN CHAR(1),
    Catastrophe_YN CHAR(1),
    Event_Name TEXT,
    Data_Source TEXT,
    n_PrimaryAttorneyPersonId_FK INT,
    d_PrimaryAttoryAssignDate DATETIME,
    n_CoAttorneyPersonId_FK INT,
    d_CoAttoryAssignDate DATETIME,
    n_Copytoclientfk INT,
    s_CountyCode TEXT,
    Inserted_UserId_FK INT,
    Updated_UserId_FK INT
);

CREATE TABLE tb_claim_checklist_responses (
    id INT PRIMARY KEY,
    checklist_task_id INT,
    claim_id INT,
    due_date DATE,
    checklist_owner_id INT,
    is_task_completed BOOLEAN,
    short_notes TEXT,
    system_assign CHAR(1),
    created_by INT,
    created_at DATETIME,
    updated_by INT,
    updated_at DATETIME,
    FOREIGN KEY (claim_id) REFERENCES tb_claim(ClaimId_PK)
);

CREATE TABLE tb_claim_checklist_tasks (
    id INT PRIMARY KEY,
    task_title TEXT,
    description TEXT,
    sequence_number INT,
    is_active BOOLEAN,
    created_by INT,
    created_at DATETIME,
    updated_by INT,
    updated_at DATETIME
);

CREATE TABLE tb_holdingcompanies (
    n_HoldingCompanyId_PK INT PRIMARY KEY, 
    s_HoldingCompanyCode VARCHAR(255),   
    s_HoldingCompanyName VARCHAR(255),    
    n_Personinfo_FK INT,                  
    company_address TEXT,                 
    website_url VARCHAR(2083),           
    logo_url VARCHAR(2083),              
    phone_no VARCHAR(50),                 
    email VARCHAR(255),                   
    naic_number INT,                      
    metadata LONGTEXT,                        
    payment_wesite_url VARCHAR(2083),     
    payment_mailling_address TEXT,        
    payment_overnight_address TEXT,      
    start_time TIME,                      
    end_time TIME,                        
    primary_color VARCHAR(50),            
    secondary_color VARCHAR(50),          
    service_provider_logo VARCHAR(2083),  
    n_CreatedUser INT,                    
    d_CreatedDate TIMESTAMP,             
    n_UpdatedUser INT,                   
    d_UpdatedDate TIMESTAMP,             
    n_EditVersion INT                     
);


CREATE TABLE tb_policies (
    n_PolicyNoId_PK INT PRIMARY KEY,
    Policy_No TEXT,
    Policy_No_Gfs TEXT,
    n_ProductId_FK INT,
    n_OwnerId_FK INT,
    n_IssueCompanyID_FK INT,
    s_IssueCountryCode TEXT,
    s_IssueStateCode TEXT,
    n_UnderwriterClient_FK INT,
    s_QuoteNumber TEXT,
    d_InceptionDate DATE,
    n_BillAccountMaster_FK INT,
    s_PolicyStatusCode TEXT,
    s_PolicyStatusReason TEXT,
    n_AgencyAccount_FK INT,
    n_SubAgentPersoninfo_FK INT,
    n_LatestTermMasterFK INT,
    n_cancelTranFK INT,
    s_RenewalTypeCode TEXT,
    n_RenewalTypeUpdateBy INT,
    n_RenewalTypeUpdateDate DATETIME,
    s_NonRenewReasonCode TEXT,
    d_BookingDate DATE,
    Policy_No_SimpleSolve TEXT,
    d_InceptionDate_SimpleSolve DATE,
    s_ExtendedCoverage CHAR(1),
    s_VmmCoverage CHAR(1),
    n_CitizenTotalPremium DECIMAL(10,2),
    n_CitizenTotalPremiumRenewal DECIMAL(10,2),
    d_InsuredLivingDate DATE,
    d_PolicyOrigNBDate DATE,
    s_Custom1 TEXT,
    n_CreatedUser INT,
    d_CreatedDate DATETIME,
    n_UpdatedUser INT,
    d_UpdatedDate DATETIME,
    n_EditVersion INT
);


CREATE TABLE tb_poriskadditionalfloodinfos (
    n_PORiskAdditionalFloodInfo_PK INT PRIMARY KEY,
    n_PORiskMasterFK INT,
    n_POTermMasterFK INT,
    n_CreatedTransactionFK INT,
    s_CommunityNumber TEXT,
    s_CommunityName TEXT,
    s_PanelNumber TEXT,
    s_MapSuffix TEXT,
    s_FloodZone TEXT,
    s_FloodZoneGroup TEXT,
    s_CommunitySFHA TEXT,
    s_CountyName TEXT,
    s_GrandfatheringTypeCode TEXT,
    s_BaseElevation TEXT,
    s_GICommunityNo TEXT,
    s_GIPanelNo TEXT,
    s_GIMapSuffix TEXT,
    s_GIMapZone TEXT,
    s_PriorPolicyNo TEXT,
    s_PriorPolicyExpDt TEXT,
    s_PriorCommunityNumber TEXT,
    s_PriorPanelNumber TEXT,
    s_PriorMapSuffix TEXT,
    s_PriorFloodZone TEXT,
    d_PriorMapDate DATE,
    s_PriorBaseElevation TEXT,
    s_PolicyTypeCode TEXT,
    s_PolicyWaitingPeriod TEXT,
    d_PropertyPurchaseDt DATE,
    s_PolicyMeetPRP TEXT,
    d_FloodLoanClosingDt DATE,
    s_PriorCompanyNAIC TEXT,
    d_PriorNBDate DATE,
    s_isInsuredTenant TEXT,
    s_RentalProperty TEXT,
    s_CondoOwnership TEXT,
    s_CondoDescription TEXT,
    s_IsCoverageFor TEXT,
    s_ManufactureMobileHome TEXT,
    s_DtOfConstructionSource TEXT,
    d_DateOfConstruction DATE,
    s_BuildingCourseConstruction TEXT,
    s_BuildingOverWater TEXT,
    s_IsFoudationPartInWater TEXT,
    s_BuildingFederalLand TEXT,
    s_Occupancy TEXT,
    s_InsuredResides TEXT,
    s_NoOfUnits TEXT,
    s_BuildingPurpose TEXT,
    s_AddExtCoverage TEXT,
    s_Foundation TEXT,
    s_NoOfFloors TEXT,
    s_IsInsuredNonProfitEnt TEXT,
    s_IsBuildingHouseWarship TEXT,
    s_BuildingType TEXT,
    s_BuildingUse TEXT,
    s_IsSmallBusinessEmp TEXT,
    s_IsAgriculturalStruct TEXT,
    s_BuildingDescription TEXT,
    s_CBRSorOPA TEXT,
    d_CBRSOPADate DATE,
    s_SevereLossProperty TEXT,
    s_FloodProgramType TEXT,
    s_FloodConstructionType TEXT,
    s_isBuildingWallRoof TEXT,
    d_InitialFirmDate DATE,
    s_DetachedGarage TEXT,
    s_AddExtOtherAttachedGarage TEXT,
    n_ReplacementCost DECIMAL(15,2),
    n_ReplacementCostRatio DECIMAL(10,2),
    s_OtherBuilding TEXT,
    s_ContentLocationTRRP TEXT,
    s_PersonalPropertyHousehold TEXT,
    s_PersonalPropertyHouseholdDescribe TEXT,
    s_WithCOC_OR_EC TEXT,
    s_ElevationDifference TEXT,
    s_ElevationDifferenceTRRP TEXT,
    s_ElevationCertificateType TEXT,
    s_ElevatedBldgFreeObstruction TEXT,
    s_SubstantialImprovement TEXT,
    s_PolicyAssignment TEXT,
    n_PercResidentialPurposes DECIMAL(5,2),
    s_IsTownRowCondo TEXT,
    s_ResidentialUnit TEXT,
    s_NonResidentialUnit TEXT,
    s_TotalSqFootage TEXT,
    s_NonResidSqFootage TEXT,
    s_FloorInBuild TEXT,
    s_MobileHomePark TEXT,
    d_MobileHomeParkDate DATE,
    s_IsPolicyMortgage TEXT,
    s_BaseFloodElevation TEXT,
    d_CurrentFirmDate DATE,
    s_IsPriorFIPPolicy TEXT,
    s_IsReqByLender TEXT,
    s_IsPriorNFIPLapsed TEXT,
    s_IsCommunitySuspension TEXT,
    d_SuspensionDate DATE,
    d_ReinstatementDate DATE,
    s_IsEffeWithIn180Days TEXT,
    s_NoOfElevator TEXT,
    s_BldgConstructionType TEXT,
    s_NoOfDetatchedStruct TEXT,
    s_IsBldgContainME TEXT,
    s_AllMachinaryElevated TEXT,
    s_UnitLocatedOnFloor TEXT,
    s_IsPropNewlyMapped TEXT,
    s_IsNewPurchase TEXT,
    s_IsBldgNRHP TEXT,
    d_SubstantialImprovmentDate DATE,
    s_IsPreFirmSubsidyEligible TEXT,
    s_RiskRating20 CHAR(3),
    s_IsAddInsureds TEXT,
    s_TableNo TEXT,
    n_CreatedUser INT,
    d_CreatedDate DATETIME,
    n_UpdatedUser INT,
    d_UpdatedDate DATETIME
);


CREATE TABLE tb_users (
    Admin_ID INT PRIMARY KEY,
    Username TEXT,
    Password TEXT,
    PasswordHash TEXT,
    First_Name TEXT,
    Last_Name TEXT,
    s_UserStatus INT,
    Email TEXT,
    d_EffectiveDate DATE,
    d_ExpiryDate DATE,

    Admin_ID_Old INT,
    Admin_ID_New INT,
    UserId_PK_CMS TEXT,
    s_UserCode TEXT,
    n_PersonInfoId_FK INT,
    UserName_Original TEXT,
    PasswordOld TEXT,
    Level INT,
    s_MiddleName TEXT,
    s_ScreenName TEXT,
    s_JobTitle TEXT,
    s_DepartmentCode TEXT,
    s_SoftwareLicenceNo TEXT,
    s_UserTypeCode_NOTUSE TEXT,
    s_UserSubTypeCode_NOTUSE TEXT,
    s_PwdRecoverKey TEXT,
    s_PwdKeyExp DATETIME,
    s_AuthKey_PolicyMap TEXT,
    s_IsAdmin CHAR(1),
    Created_On DATETIME,
    Closing_Date DATETIME,
    Access_Modules TEXT,
    Closing_Date_Crystal DATETIME,
    s_ThemeName TEXT,
    gcm_regid TEXT,
    Last_UserID INT,
    Last_Timestamp DATETIME,
    Login_FirstTime CHAR(1),
    n_CreatedUser INT,
    d_CreatedDate DATETIME,
    n_UpdatedUser INT,
    d_UpdatedDate DATETIME,
    n_EditVersion INT,
    avatar TEXT,
    active CHAR(1),
    activation_token TEXT,
    cognito_id TEXT,
    remember_token TEXT
);
"""

# Función asincrónica para crear la base de datos y las tablas
async def create_database():
    logger.info("Conectando a la base de datos...")
    await database.connect()
    logger.info("Ejecutando el esquema SQL para crear la base de datos y las tablas...")
    await database.execute(schema_sql)
    logger.info("Desconectando de la base de datos...")
    await database.disconnect()
    logger.info("Base de datos creada y desconectada exitosamente.")

# Ejecutar la función asincrónica para crear la base de datos
asyncio.run(create_database())