from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    DateTime,
    DECIMAL,
    ForeignKey,
    Boolean,
    Time,
    CHAR,
    Float,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from .database import Base


class TbClaim(Base):
    __tablename__ = 'tb_claim'

    ClaimId_PK = Column(Integer, primary_key=True)
    Claim_No = Column(Integer, nullable=False)
    Risk_Id = Column(Integer)
    n_TermMaster_FK = Column(Integer)
    n_potransaction_FK = Column(Integer)
    n_PolicyNoId_FK = Column(Integer)
    n_PORiskMasterFK = Column(Integer)
    Date_Of_Loss = Column(Date)
    Insured_Name = Column(Text)
    Agency_Name = Column(Text)
    n_AgencyAccount_FK = Column(Integer)
    Loss_Type_Code = Column(Text)
    Total_Paid_Amount = Column(DECIMAL(10, 2))
    Claim_Status_Code = Column(Text)
    Claim_SubStatus_Code = Column(Text)
    Inserted_Date = Column(DateTime)
    Updated_Date = Column(DateTime)

    Policy_No_SimpleSolve = Column(Text)
    n_InsuredPersonInfoId_FK = Column(Integer)
    n_AgencyPersoninfoId_FK = Column(Integer)
    n_SubAgentPersoninfo_FK = Column(Integer)
    Reported_By_PersonId_FK = Column(Integer)
    InHouseCounsel_Person_FK = Column(Integer)
    Reported_By_PersonId_FK_Old = Column(Integer)
    PA_PersonId_FK = Column(Integer)
    Reported_By_Deprecated = Column(Text)
    Reported_By_Relation_Code = Column(Text)
    ClaimTypeId_FK = Column(Integer)
    Amount_Claimed = Column(DECIMAL(10, 2))
    Letter_URL_Path = Column(Text)
    Remarks = Column(Text)
    Allocated_To_UserId_FK = Column(Integer, ForeignKey('tb_users.Admin_ID'))
    Date_Allocated = Column(DateTime)
    Date_First_Visited = Column(DateTime)
    Service_Repre_UserId_FK = Column(Integer)
    Approval_Status_Code = Column(Text)
    Claim_Approved_UserId_FK = Column(Integer)
    Comment = Column(Text)
    Date_Close = Column(DateTime)
    Total_Paid_Amt_New = Column(DECIMAL(10, 2))
    Attorney_Involved_YN = Column(CHAR(1))
    PA_Involved_YN = Column(CHAR(1))
    DFS_Complain_YN = Column(CHAR(1))
    Catastrophe_YN = Column(CHAR(1))
    Event_Name = Column(Text)
    Data_Source = Column(Text)
    n_PrimaryAttorneyPersonId_FK = Column(Integer)
    d_PrimaryAttoryAssignDate = Column(DateTime)
    n_CoAttorneyPersonId_FK = Column(Integer)
    d_CoAttoryAssignDate = Column(DateTime)
    n_Copytoclientfk = Column(Integer)
    s_CountyCode = Column(Text)
    Inserted_UserId_FK = Column(Integer, ForeignKey('tb_users.Admin_ID'))
    Updated_UserId_FK = Column(Integer, ForeignKey('tb_users.Admin_ID'))

    # Relaciones
    checklist_responses = relationship("TbClaimChecklistResponses", back_populates="claim", cascade="all, delete-orphan")
    allocated_to_user = relationship("TbUsers", foreign_keys=[Allocated_To_UserId_FK], back_populates="allocated_claims")
    inserted_user = relationship("TbUsers", foreign_keys=[Inserted_UserId_FK], back_populates="inserted_claims")
    updated_user = relationship("TbUsers", foreign_keys=[Updated_UserId_FK], back_populates="updated_claims")


class TbClaimChecklistResponses(Base):
    __tablename__ = 'tb_claim_checklist_responses'

    id = Column(Integer, primary_key=True)
    checklist_task_id = Column(Integer, ForeignKey('tb_claim_checklist_tasks.id'))
    claim_id = Column(Integer, ForeignKey('tb_claim.ClaimId_PK'))
    due_date = Column(Date)
    checklist_owner_id = Column(Integer)
    is_task_completed = Column(Boolean)
    short_notes = Column(Text)
    system_assign = Column(CHAR(1))
    created_by = Column(Integer)
    created_at = Column(DateTime)
    updated_by = Column(Integer)
    updated_at = Column(DateTime)

    # Relaciones
    claim = relationship("TbClaim", back_populates="checklist_responses")
    task = relationship("TbClaimChecklistTasks", back_populates="responses")


class TbClaimChecklistTasks(Base):
    __tablename__ = 'tb_claim_checklist_tasks'

    id = Column(Integer, primary_key=True)
    task_title = Column(Text)
    description = Column(Text)
    sequence_number = Column(Integer)
    is_active = Column(Boolean)
    created_by = Column(Integer)
    created_at = Column(DateTime)
    updated_by = Column(Integer)
    updated_at = Column(DateTime)

    # Relaciones
    responses = relationship("TbClaimChecklistResponses", back_populates="task", cascade="all, delete-orphan")


class TbHoldingCompanies(Base):
    __tablename__ = 'tb_holdingcompanies'

    n_HoldingCompanyId_PK = Column(Integer, primary_key=True)
    s_HoldingCompanyCode = Column(String(255))
    s_HoldingCompanyName = Column(String(255))
    n_Personinfo_FK = Column(Integer)
    company_address = Column(Text)
    website_url = Column(String(2083))
    logo_url = Column(String(2083))
    phone_no = Column(String(50))
    email = Column(String(255))
    naic_number = Column(Integer)
    company_metadata = Column('metadata', LONGTEXT)
    payment_wesite_url = Column(String(2083))
    payment_mailling_address = Column(Text)
    payment_overnight_address = Column(Text)
    start_time = Column(Time)
    end_time = Column(Time)
    primary_color = Column(String(50))
    secondary_color = Column(String(50))
    service_provider_logo = Column(String(2083))
    n_CreatedUser = Column(Integer)
    d_CreatedDate = Column(TIMESTAMP)
    n_UpdatedUser = Column(Integer)
    d_UpdatedDate = Column(TIMESTAMP)
    n_EditVersion = Column(Integer)


class TbPolicies(Base):
    __tablename__ = 'tb_policies'

    n_PolicyNoId_PK = Column(Integer, primary_key=True)
    Policy_No = Column(Text)
    Policy_No_Gfs = Column(Text)
    n_ProductId_FK = Column(Integer)
    n_OwnerId_FK = Column(Integer)
    n_IssueCompanyID_FK = Column(Integer)
    s_IssueCountryCode = Column(Text)
    s_IssueStateCode = Column(Text)
    n_UnderwriterClient_FK = Column(Integer)
    s_QuoteNumber = Column(Text)
    d_InceptionDate = Column(Date)
    n_BillAccountMaster_FK = Column(Integer)
    s_PolicyStatusCode = Column(Text)
    s_PolicyStatusReason = Column(Text)
    n_AgencyAccount_FK = Column(Integer)
    n_SubAgentPersoninfo_FK = Column(Integer)
    n_LatestTermMasterFK = Column(Integer)
    n_cancelTranFK = Column(Integer)
    s_RenewalTypeCode = Column(Text)
    n_RenewalTypeUpdateBy = Column(Integer)
    n_RenewalTypeUpdateDate = Column(DateTime)
    s_NonRenewReasonCode = Column(Text)
    d_BookingDate = Column(Date)
    Policy_No_SimpleSolve = Column(Text)
    d_InceptionDate_SimpleSolve = Column(Date)
    s_ExtendedCoverage = Column(CHAR(1))
    s_VmmCoverage = Column(CHAR(1))
    n_CitizenTotalPremium = Column(DECIMAL(10, 2))
    n_CitizenTotalPremiumRenewal = Column(DECIMAL(10, 2))
    d_InsuredLivingDate = Column(Date)
    d_PolicyOrigNBDate = Column(Date)
    s_Custom1 = Column(Text)
    n_CreatedUser = Column(Integer)
    d_CreatedDate = Column(DateTime)
    n_UpdatedUser = Column(Integer)
    d_UpdatedDate = Column(DateTime)
    n_EditVersion = Column(Integer)


class TbPoRiskAdditionalFloodInfos(Base):
    __tablename__ = 'tb_poriskadditionalfloodinfos'

    n_PORiskAdditionalFloodInfo_PK = Column(Integer, primary_key=True)
    n_PORiskMasterFK = Column(Integer)
    n_POTermMasterFK = Column(Integer)
    n_CreatedTransactionFK = Column(Integer)
    s_CommunityNumber = Column(Text)
    s_CommunityName = Column(Text)
    s_PanelNumber = Column(Text)
    s_MapSuffix = Column(Text)
    s_FloodZone = Column(Text)
    s_FloodZoneGroup = Column(Text)
    s_CommunitySFHA = Column(Text)
    s_CountyName = Column(Text)
    s_GrandfatheringTypeCode = Column(Text)
    s_BaseElevation = Column(Text)
    s_GICommunityNo = Column(Text)
    s_GIPanelNo = Column(Text)
    s_GIMapSuffix = Column(Text)
    s_GIMapZone = Column(Text)
    s_PriorPolicyNo = Column(Text)
    s_PriorPolicyExpDt = Column(Text)
    s_PriorCommunityNumber = Column(Text)
    s_PriorPanelNumber = Column(Text)
    s_PriorMapSuffix = Column(Text)
    s_PriorFloodZone = Column(Text)
    d_PriorMapDate = Column(Date)
    s_PriorBaseElevation = Column(Text)
    s_PolicyTypeCode = Column(Text)
    s_PolicyWaitingPeriod = Column(Text)
    d_PropertyPurchaseDt = Column(Date)
    s_PolicyMeetPRP = Column(Text)
    d_FloodLoanClosingDt = Column(Date)
    s_PriorCompanyNAIC = Column(Text)
    d_PriorNBDate = Column(Date)
    s_isInsuredTenant = Column(Text)
    s_RentalProperty = Column(Text)
    s_CondoOwnership = Column(Text)
    s_CondoDescription = Column(Text)
    s_IsCoverageFor = Column(Text)
    s_ManufactureMobileHome = Column(Text)
    s_DtOfConstructionSource = Column(Text)
    d_DateOfConstruction = Column(Date)
    s_BuildingCourseConstruction = Column(Text)
    s_BuildingOverWater = Column(Text)
    s_IsFoudationPartInWater = Column(Text)
    s_BuildingFederalLand = Column(Text)
    s_Occupancy = Column(Text)
    s_InsuredResides = Column(Text)
    s_NoOfUnits = Column(Text)
    s_BuildingPurpose = Column(Text)
    s_AddExtCoverage = Column(Text)
    s_Foundation = Column(Text)
    s_NoOfFloors = Column(Text)
    s_IsInsuredNonProfitEnt = Column(Text)
    s_IsBuildingHouseWarship = Column(Text)
    s_BuildingType = Column(Text)
    s_BuildingUse = Column(Text)
    s_IsSmallBusinessEmp = Column(Text)
    s_IsAgriculturalStruct = Column(Text)
    s_BuildingDescription = Column(Text)
    s_CBRSorOPA = Column(Text)
    d_CBRSOPADate = Column(Date)
    s_SevereLossProperty = Column(Text)
    s_FloodProgramType = Column(Text)
    s_FloodConstructionType = Column(Text)
    s_isBuildingWallRoof = Column(Text)
    d_InitialFirmDate = Column(Date)
    s_DetachedGarage = Column(Text)
    s_AddExtOtherAttachedGarage = Column(Text)
    n_ReplacementCost = Column(DECIMAL(15, 2))
    n_ReplacementCostRatio = Column(DECIMAL(10, 2))
    s_OtherBuilding = Column(Text)
    s_ContentLocationTRRP = Column(Text)
    s_PersonalPropertyHousehold = Column(Text)
    s_PersonalPropertyHouseholdDescribe = Column(Text)
    s_WithCOC_OR_EC = Column(Text)
    s_ElevationDifference = Column(Text)
    s_ElevationDifferenceTRRP = Column(Text)
    s_ElevationCertificateType = Column(Text)
    s_ElevatedBldgFreeObstruction = Column(Text)
    s_SubstantialImprovement = Column(Text)
    s_PolicyAssignment = Column(Text)
    n_PercResidentialPurposes = Column(DECIMAL(5, 2))
    s_IsTownRowCondo = Column(Text)
    s_ResidentialUnit = Column(Text)
    s_NonResidentialUnit = Column(Text)
    s_TotalSqFootage = Column(Text)
    s_NonResidSqFootage = Column(Text)
    s_FloorInBuild = Column(Text)
    s_MobileHomePark = Column(Text)
    d_MobileHomeParkDate = Column(Date)
    s_IsPolicyMortgage = Column(Text)
    s_BaseFloodElevation = Column(Text)
    d_CurrentFirmDate = Column(Date)
    s_IsPriorFIPPolicy = Column(Text)
    s_IsReqByLender = Column(Text)
    s_IsPriorNFIPLapsed = Column(Text)
    s_IsCommunitySuspension = Column(Text)
    d_SuspensionDate = Column(Date)
    d_ReinstatementDate = Column(Date)
    s_IsEffeWithIn180Days = Column(Text)
    s_NoOfElevator = Column(Text)
    s_BldgConstructionType = Column(Text)
    s_NoOfDetatchedStruct = Column(Text)
    s_IsBldgContainME = Column(Text)
    s_AllMachinaryElevated = Column(Text)
    s_UnitLocatedOnFloor = Column(Text)
    s_IsPropNewlyMapped = Column(Text)
    s_IsNewPurchase = Column(Text)
    s_IsBldgNRHP = Column(Text)
    d_SubstantialImprovmentDate = Column(Date)
    s_IsPreFirmSubsidyEligible = Column(Text)
    s_RiskRating20 = Column(CHAR(3))
    s_IsAddInsureds = Column(Text)
    s_TableNo = Column(Text)
    n_CreatedUser = Column(Integer)
    d_CreatedDate = Column(DateTime)
    n_UpdatedUser = Column(Integer)
    d_UpdatedDate = Column(DateTime)


class TbUsers(Base):
    __tablename__ = 'tb_users'

    Admin_ID = Column(Integer, primary_key=True)
    Username = Column(Text)
    Password = Column(Text)
    PasswordHash = Column(Text)
    First_Name = Column(Text)
    Last_Name = Column(Text)
    s_UserStatus = Column(Integer)
    Email = Column(Text)
    d_EffectiveDate = Column(Date)
    d_ExpiryDate = Column(Date)

    Admin_ID_Old = Column(Integer)
    Admin_ID_New = Column(Integer)
    UserId_PK_CMS = Column(Text)
    s_UserCode = Column(Text)
    n_PersonInfoId_FK = Column(Integer)
    UserName_Original = Column(Text)
    PasswordOld = Column(Text)
    Level = Column(Integer)
    s_MiddleName = Column(Text)
    s_ScreenName = Column(Text)
    s_JobTitle = Column(Text)
    s_DepartmentCode = Column(Text)
    s_SoftwareLicenceNo = Column(Text)
    s_UserTypeCode_NOTUSE = Column(Text)
    s_UserSubTypeCode_NOTUSE = Column(Text)
    s_PwdRecoverKey = Column(Text)
    s_PwdKeyExp = Column(DateTime)
    s_AuthKey_PolicyMap = Column(Text)
    s_IsAdmin = Column(CHAR(1))
    Created_On = Column(DateTime)
    Closing_Date = Column(DateTime)
    Access_Modules = Column(Text)
    Closing_Date_Crystal = Column(DateTime)
    s_ThemeName = Column(Text)
    gcm_regid = Column(Text)
    Last_UserID = Column(Integer)
    Last_Timestamp = Column(DateTime)
    Login_FirstTime = Column(CHAR(1))
    n_CreatedUser = Column(Integer)
    d_CreatedDate = Column(DateTime)
    n_UpdatedUser = Column(Integer)
    d_UpdatedDate = Column(DateTime)
    n_EditVersion = Column(Integer)
    avatar = Column(Text)
    active = Column(CHAR(1))
    activation_token = Column(Text)
    cognito_id = Column(Text)
    remember_token = Column(Text)

    # Relaciones inversas con TbClaim
    allocated_claims = relationship("TbClaim", foreign_keys="[TbClaim.Allocated_To_UserId_FK]", back_populates="allocated_to_user")
    inserted_claims = relationship("TbClaim", foreign_keys="[TbClaim.Inserted_UserId_FK]", back_populates="inserted_user")
    updated_claims = relationship("TbClaim", foreign_keys="[TbClaim.Updated_UserId_FK]", back_populates="updated_user")
