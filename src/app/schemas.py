# app/schemas.py

from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel


# Esquemas para TbClaim

class TbClaimBase(BaseModel):
    Claim_No: int
    Risk_Id: Optional[int]
    n_TermMaster_FK: Optional[int]
    n_potransaction_FK: Optional[int]
    n_PolicyNoId_FK: Optional[int]
    n_PORiskMasterFK: Optional[int]
    Date_Of_Loss: Optional[date]
    Insured_Name: Optional[str]
    Agency_Name: Optional[str]
    n_AgencyAccount_FK: Optional[int]
    Loss_Type_Code: Optional[str]
    Total_Paid_Amount: Optional[float]
    Claim_Status_Code: Optional[str]
    Claim_SubStatus_Code: Optional[str]
    Inserted_Date: Optional[datetime]
    Updated_Date: Optional[datetime]

class TbClaimCreate(TbClaimBase):
    pass  

class TbClaimUpdate(BaseModel):
    Claim_No: Optional[int]
    Insured_Name: Optional[str]
    Claim_Status_Code: Optional[str]

class TbClaim(TbClaimBase):
    ClaimId_PK: int

    class Config:
        orm_mode = True

# Esquemas para TbClaimChecklistResponses

class TbClaimChecklistResponsesBase(BaseModel):
    checklist_task_id: int
    claim_id: int
    due_date: Optional[date]
    checklist_owner_id: Optional[int]
    is_task_completed: Optional[bool]
    short_notes: Optional[str]
    system_assign: Optional[str]
    created_by: Optional[int]
    created_at: Optional[datetime]
    updated_by: Optional[int]
    updated_at: Optional[datetime]

class TbClaimChecklistResponsesCreate(TbClaimChecklistResponsesBase):
    pass

class TbClaimChecklistResponsesUpdate(BaseModel):
    checklist_task_id: Optional[int]
    claim_id: Optional[int]
    is_task_completed: Optional[bool]


class TbClaimChecklistResponses(TbClaimChecklistResponsesBase):
    id: int

    class Config:
        orm_mode = True

# Esquemas para TbClaimChecklistTasks

class TbClaimChecklistTasksBase(BaseModel):
    task_title: str
    description: Optional[str]
    sequence_number: Optional[int]
    is_active: Optional[bool]
    created_by: Optional[int]
    created_at: Optional[datetime]
    updated_by: Optional[int]
    updated_at: Optional[datetime]

class TbClaimChecklistTasksCreate(TbClaimChecklistTasksBase):
    pass

class TbClaimChecklistTasksUpdate(BaseModel):
    task_title: Optional[str]
    is_active: Optional[bool]

class TbClaimChecklistTasks(TbClaimChecklistTasksBase):
    id: int

    class Config:
        orm_mode = True

# Esquemas para TbHoldingCompanies

class TbHoldingCompaniesBase(BaseModel):
    s_HoldingCompanyCode: Optional[str]
    s_HoldingCompanyName: Optional[str]
    n_Personinfo_FK: Optional[int]
    company_address: Optional[str]
    website_url: Optional[str]
    logo_url: Optional[str]
    phone_no: Optional[str]
    email: Optional[str]
    naic_number: Optional[int]
    company_metadata: Optional[str]
    payment_wesite_url: Optional[str]
    payment_mailling_address: Optional[str]
    payment_overnight_address: Optional[str]
    start_time: Optional[str]
    end_time: Optional[str]
    primary_color: Optional[str]
    secondary_color: Optional[str]
    service_provider_logo: Optional[str]
    n_CreatedUser: Optional[int]
    d_CreatedDate: Optional[datetime]
    n_UpdatedUser: Optional[int]
    d_UpdatedDate: Optional[datetime]
    n_EditVersion: Optional[int]

class TbHoldingCompaniesCreate(TbHoldingCompaniesBase):
    pass

class TbHoldingCompaniesUpdate(BaseModel):
    s_HoldingCompanyCode: Optional[str]

class TbHoldingCompanies(TbHoldingCompaniesBase):
    n_HoldingCompanyId_PK: int

    class Config:
        orm_mode = True

# Esquemas para TbPolicies

class TbPoliciesBase(BaseModel):
    Policy_No: Optional[str]
    Policy_No_Gfs: Optional[str]
    n_ProductId_FK: Optional[int]
    n_OwnerId_FK: Optional[int]
    n_IssueCompanyID_FK: Optional[int]
    s_IssueCountryCode: Optional[str]
    s_IssueStateCode: Optional[str]
    n_UnderwriterClient_FK: Optional[int]
    s_QuoteNumber: Optional[str]
    d_InceptionDate: Optional[date]
    n_BillAccountMaster_FK: Optional[int]
    s_PolicyStatusCode: Optional[str]
    s_PolicyStatusReason: Optional[str]
    n_AgencyAccount_FK: Optional[int]
    n_SubAgentPersoninfo_FK: Optional[int]
    n_LatestTermMasterFK: Optional[int]
    n_cancelTranFK: Optional[int]
    s_RenewalTypeCode: Optional[str]
    n_RenewalTypeUpdateBy: Optional[int]
    n_RenewalTypeUpdateDate: Optional[datetime]
    s_NonRenewReasonCode: Optional[str]
    d_BookingDate: Optional[date]
    Policy_No_SimpleSolve: Optional[str]
    d_InceptionDate_SimpleSolve: Optional[date]
    s_ExtendedCoverage: Optional[str]
    s_VmmCoverage: Optional[str]
    n_CitizenTotalPremium: Optional[float]
    n_CitizenTotalPremiumRenewal: Optional[float]
    d_InsuredLivingDate: Optional[date]
    d_PolicyOrigNBDate: Optional[date]
    s_Custom1: Optional[str]
    n_CreatedUser: Optional[int]
    d_CreatedDate: Optional[datetime]
    n_UpdatedUser: Optional[int]
    d_UpdatedDate: Optional[datetime]
    n_EditVersion: Optional[int]

class TbPoliciesCreate(TbPoliciesBase):
    pass

class TbPoliciesUpdate(BaseModel):
    Policy_No: Optional[str]

class TbPolicies(TbPoliciesBase):
    n_PolicyNoId_PK: int

    class Config:
        orm_mode = True

# Esquemas para TbPoRiskAdditionalFloodInfos

class TbPoRiskAdditionalFloodInfosBase(BaseModel):
    n_PORiskMasterFK: Optional[int]
    n_POTermMasterFK: Optional[int]
    n_CreatedTransactionFK: Optional[int]
    s_CommunityNumber: Optional[str]
    s_CommunityName: Optional[str]
    s_PanelNumber: Optional[str]
    s_MapSuffix: Optional[str]
    s_FloodZone: Optional[str]
    s_FloodZoneGroup: Optional[str]
    s_CommunitySFHA: Optional[str]
    s_CountyName: Optional[str]
    s_GrandfatheringTypeCode: Optional[str]
    s_BaseElevation: Optional[str]
    s_GICommunityNo: Optional[str]
    s_GIPanelNo: Optional[str]
    s_GIMapSuffix: Optional[str]
    s_GIMapZone: Optional[str]
    s_PriorPolicyNo: Optional[str]
    s_PriorPolicyExpDt: Optional[str]
    s_PriorCommunityNumber: Optional[str]
    s_PriorPanelNumber: Optional[str]
    s_PriorMapSuffix: Optional[str]
    s_PriorFloodZone: Optional[str]
    d_PriorMapDate: Optional[date]
    s_PriorBaseElevation: Optional[str]
    s_PolicyTypeCode: Optional[str]
    s_PolicyWaitingPeriod: Optional[str]
    d_PropertyPurchaseDt: Optional[date]
    s_PolicyMeetPRP: Optional[str]
    d_FloodLoanClosingDt: Optional[date]
    s_PriorCompanyNAIC: Optional[str]
    d_PriorNBDate: Optional[date]
    s_isInsuredTenant: Optional[str]
    s_RentalProperty: Optional[str]
    s_CondoOwnership: Optional[str]
    s_CondoDescription: Optional[str]
    s_IsCoverageFor: Optional[str]
    s_ManufactureMobileHome: Optional[str]
    s_DtOfConstructionSource: Optional[str]
    d_DateOfConstruction: Optional[date]
    s_BuildingCourseConstruction: Optional[str]
    s_BuildingOverWater: Optional[str]
    s_IsFoudationPartInWater: Optional[str]
    s_BuildingFederalLand: Optional[str]
    s_Occupancy: Optional[str]
    s_InsuredResides: Optional[str]
    s_NoOfUnits: Optional[str]
    s_BuildingPurpose: Optional[str]
    s_AddExtCoverage: Optional[str]
    s_Foundation: Optional[str]
    s_NoOfFloors: Optional[str]
    s_IsInsuredNonProfitEnt: Optional[str]
    s_IsBuildingHouseWarship: Optional[str]
    s_BuildingType: Optional[str]
    s_BuildingUse: Optional[str]
    s_IsSmallBusinessEmp: Optional[str]
    s_IsAgriculturalStruct: Optional[str]
    s_BuildingDescription: Optional[str]
    s_CBRSorOPA: Optional[str]
    d_CBRSOPADate: Optional[date]
    s_SevereLossProperty: Optional[str]
    s_FloodProgramType: Optional[str]
    s_FloodConstructionType: Optional[str]
    s_isBuildingWallRoof: Optional[str]
    d_InitialFirmDate: Optional[date]
    s_DetachedGarage: Optional[str]
    s_AddExtOtherAttachedGarage: Optional[str]
    n_ReplacementCost: Optional[float]
    n_ReplacementCostRatio: Optional[float]
    s_OtherBuilding: Optional[str]
    s_ContentLocationTRRP: Optional[str]
    s_PersonalPropertyHousehold: Optional[str]
    s_PersonalPropertyHouseholdDescribe: Optional[str]
    s_WithCOC_OR_EC: Optional[str]
    s_ElevationDifference: Optional[str]
    s_ElevationDifferenceTRRP: Optional[str]
    s_ElevationCertificateType: Optional[str]
    s_ElevatedBldgFreeObstruction: Optional[str]
    s_SubstantialImprovement: Optional[str]
    s_PolicyAssignment: Optional[str]
    n_PercResidentialPurposes: Optional[float]
    s_IsTownRowCondo: Optional[str]
    s_ResidentialUnit: Optional[str]
    s_NonResidentialUnit: Optional[str]
    s_TotalSqFootage: Optional[str]
    s_NonResidSqFootage: Optional[str]
    s_FloorInBuild: Optional[str]
    s_MobileHomePark: Optional[str]
    d_MobileHomeParkDate: Optional[date]
    s_IsPolicyMortgage: Optional[str]
    s_BaseFloodElevation: Optional[str]
    d_CurrentFirmDate: Optional[date]
    s_IsPriorFIPPolicy: Optional[str]
    s_IsReqByLender: Optional[str]
    s_IsPriorNFIPLapsed: Optional[str]
    s_IsCommunitySuspension: Optional[str]
    d_SuspensionDate: Optional[date]
    d_ReinstatementDate: Optional[date]
    s_IsEffeWithIn180Days: Optional[str]
    s_NoOfElevator: Optional[str]
    s_BldgConstructionType: Optional[str]
    s_NoOfDetatchedStruct: Optional[str]
    s_IsBldgContainME: Optional[str]
    s_AllMachinaryElevated: Optional[str]
    s_UnitLocatedOnFloor: Optional[str]
    s_IsPropNewlyMapped: Optional[str]
    s_IsNewPurchase: Optional[str]
    s_IsBldgNRHP: Optional[str]
    d_SubstantialImprovmentDate: Optional[date]
    s_IsPreFirmSubsidyEligible: Optional[str]
    s_RiskRating20: Optional[str]
    s_IsAddInsureds: Optional[str]
    s_TableNo: Optional[str]
    n_CreatedUser: Optional[int]
    d_CreatedDate: Optional[datetime]
    n_UpdatedUser: Optional[int]
    d_UpdatedDate: Optional[datetime]

class TbPoRiskAdditionalFloodInfosCreate(TbPoRiskAdditionalFloodInfosBase):
    pass

class TbPoRiskAdditionalFloodInfosUpdate(BaseModel):
    n_PORiskMasterFK: Optional[int]


class TbPoRiskAdditionalFloodInfos(TbPoRiskAdditionalFloodInfosBase):
    n_PORiskAdditionalFloodInfo_PK: int

    class Config:
        orm_mode = True

# Esquemas para TbUsers

class TbUsersBase(BaseModel):
    Username: Optional[str]
    Password: Optional[str]
    PasswordHash: Optional[str]
    First_Name: Optional[str]
    Last_Name: Optional[str]
    s_UserStatus: Optional[int]
    Email: Optional[str]
    d_EffectiveDate: Optional[date]
    d_ExpiryDate: Optional[date]

class TbUsersCreate(TbUsersBase):
    Username: str
    Password: str
    Email: str

class TbUsersUpdate(BaseModel):
    Username: Optional[str]
    Email: Optional[str]


class TbUsers(TbUsersBase):
    Admin_ID: int

    class Config:
        orm_mode = True

class ReportMetrics(BaseModel):
    total_quotes: int
    quote_nb: int
    quote_conversion_percent: float
    quote_nb_premium: float
    average_nb_premium: float
    pif: int
    expired_policies: int
    expired_premium: float
    retention_percent: float

    class Config:
        from_attributes = True

class CompanyGrouping(BaseModel):
    company_id: Optional[int]
    policy_count: int
    total_premium: float

    class Config:
        from_attributes = True

class AgentGrouping(BaseModel):
    agent_id: Optional[int]
    policy_count: int
    total_premium: float

    class Config:
        from_attributes = True

class StateGrouping(BaseModel):
    state_code: Optional[str]
    policy_count: int
    total_premium: float

    class Config:
        from_attributes = True

class TimeSeriesData(BaseModel):
    date: str
    policy_count: int
    total_premium: float

    class Config:
        orm_mode = True