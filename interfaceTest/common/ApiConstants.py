import self as self

from interfaceTest import readConfig
localReadConfig = readConfig.ReadConfig()
class ApiConstants:
    def __init__(self):
        self.base_url = localReadConfig.get_http("baseurl")

    @property
    def LOGIN_URL(self):
        login_url = self.base_url+"/api/oauth/noToken/login"
        return login_url

    @property
    def PROJECTCREAT_URL(self):
        projectcreat_url = self.base_url + "/api/report/project/create"
        return projectcreat_url

    @property
    def PROJECTQUERY_URL(self):
        projectquery_url = self.base_url + "/api/report/project/query/page"
        return projectquery_url

    @property
    def PROJECTFILERENAME_URL(self):
        projectrFilerename_url = self.base_url + "/api/report/bom/projectFile/rename"
        return projectrFilerename_url

    @property
    def COMPONENTSAVE_URL(self):
        componentsave_url=self.base_url +"/api/report/component/saveComponentAndBom"
        return componentsave_url

    @property
    def CONFIRMCOMPONENTANDBOM_URL(self):
        confirmComponentAndBom_url = self.base_url + "/api/report/component/confirmComponentAndBom"
        return confirmComponentAndBom_url

    @property
    def  PROCESSPLAN_URL(self):
         processplan_url = self.base_url +"/api/report/processPlan"
         return processplan_url

    @property
    def PRODUCTIONTASK_URL(self):
        productionTask_url = self.base_url +"/api/report/productionTask"
        return productionTask_url
    @property
    def PROJECTCUSTOMER_URL(self):
        projectCustomer_url = self.base_url +"/api/report/projectCustomer"
        return projectCustomer_url

    @property
    def TRANSPORTVECHICE_URL(self):
        transportVehicle_url = self.base_url +"/api/report/transportVehicle"
        return transportVehicle_url

    @property
    def DELIVERYPLAN_URL(self):
        deliveryPlan_url = self.base_url +"/api/report/deliveryPlan"
        return deliveryPlan_url

    @property
    def MATERIALPLEASEORDER_URL(self):
        materialPleaseOrder_url = self .base_url +"/api/report/materialPleaseOrder/batchSave"
        return materialPleaseOrder_url

    @property
    def PROJECTUPDATE_URL(self):
        projectupdate_url = self .base_url +"/api/report/project/update"
        return projectupdate_url

    @property
    def PROCESSPLAN_URL(self):
        processPlan_url = self.base_url + "/api/report/processPlan"
        return processPlan_url
    @property
    def STATEMENTRULRESQUERY_url(self):
        statementRulesquery_url = self.base_url +"/api/report/subcontractingStatementRules/queryPage"
        return statementRulesquery_url

    @property
    def UPDATESUBCONTRACTING_URL(self):
        updateSubcontracting_url = self .base_url +"/api/report/subcontractingStatementRules/updateSubcontracting"
        return updateSubcontracting_url

    @property
    def ACCOUNTSTATEMENTQUERYPAGE_URL(self):
        accountStatementqueryPage_url = self .base_url +"/api/report/accountStatement/queryPage"
        return accountStatementqueryPage_url


    @property
    def SUBCONTRACTINGSTATEMENTQUERY_URL(self):
        subcontractingStatemnetquery_url = self .base_url +"/api/report/subcontractingStatement/queryPage"
        return subcontractingStatemnetquery_url

    @property
    def QUERYMASTERPLAN_URL(self):
        querymasterplan_url = self.base_url +"/api/report/masterPlan/queryMasterPlan"
        return querymasterplan_url
    @property
    def CREATEPLAN_URL(self):
        createrplan_url = self .base_url +"/api/report/masterPlan/createPlan"
        return createrplan_url

    @property
    def MATERIALQUERYPAGE_URL(self):
        materialqueryPage_url = self.base_url +"/api/report/material/queryPage"
        return materialqueryPage_url

    @property
    def EXPORTMATERIAL_URL(self):
        exportMaterial_url = self.base_url +"/api/report/material/queryPage"
        return exportMaterial_url
    @property
    def STOCKMONITOR_URL(self):
        stockMonitor_URL = self.base_url +"/api/report/statistics/stockMonitor"
        return stockMonitor_URL

    @property
    def YESTERDAYTOTALAMOUNT_URK(self):
        yesterdaytotalAmount_url = self.base_url +"/api/report/billboards/yesterday/totalAmount"
        return yesterdaytotalAmount_url

    @property
    def DELIVERYSCHEDULE_URL(self):
        deliveryschedule_url = self.base_url +"/api/report/statistics/delivery/schedule"
        return deliveryschedule_url

    @property
    def GETPRODUCTIONMONITORING_URL(self):
        getProductionMonitoring_url = self.base_url +"/api/report/productionTask/getProductionMonitoring"
        return getProductionMonitoring_url

    @property
    def GETMONITORING_URL(self):
        getMonitoring_url = self.base_url +"/api/report/billboards/getMonitoring"
        return getMonitoring_url

    @property
    def ACCOUNTSTATEMENTGETMONITORING_URL(self):
        accountStataementgetmonitoring_url = self.base_url+"/api/report/accountStatement/getMonitoring"
        return accountStataementgetmonitoring_url

    @property
    def ACCOUNTSTATEMENTQUERYLIST_URL(self):
        accountStatementquerylist_url = self.base_url +"/api/report/accountStatement/queryList"
        return accountStatementquerylist_url

    @property
    def CREATEDYEARMONTH_URL(self):
        createdYearMonth_url = self .base_url +"/api/report/masterPlan/versionList?createdYearMonth=2023-06"
        return createdYearMonth_url

    @property
    def EXPORTMASTERPLANFILE_URL(self):
        exportMasterPlanFile_url = self.base_url +"/api/report/masterPlan/exportMasterPlanFile"
        return exportMasterPlanFile_url

    @property
    def QUERYBUSINESSRECONCILIATION_URL(self):
        queryBusinessReconciliation_url = self.base_url +"/api/report/accountStatement/queryBusinessReconciliation"
        return queryBusinessReconciliation_url


    @property
    def QUERYBUSINESSRECONCILIATIONSTATISTICS_URL(self):
        queryBusinessReconciliationStatistics_url = self.base_url +"/api/report/accountStatement/queryBusinessReconciliationStatistics"
        return queryBusinessReconciliationStatistics_url

    @property
    def GETBUSiNESSRECONCILIATIONCOLUMNDATA_URL(self):
        getBusinessReconciliationColumnData_url = self.base_url +"/api/report/accountStatement/getBusinessReconciliationColumnData"
        return getBusinessReconciliationColumnData_url


    @property
    def QUERYALLSTATISTICS_URL(self):
        queryAllStatistics_url = self.base_url +"/api/report/accountStatement/queryAllStatistics"
        return queryAllStatistics_url
    @property
    def QUERYSETTLEMENTCONFIRMATIONSTATISTICS_URL(self):
        querySettlementConfirmationStatistics_url = self.base_url +"/api/report/accountStatement/querySettlementConfirmationStatistics"
        return querySettlementConfirmationStatistics_url

    @property
    def QUERYSETTLEMENTCONFIRMATION_URL(self):
        querySettlementConfirmation_url = self.base_url +"/api/report/accountStatement/querySettlementConfirmation"
        return querySettlementConfirmation_url

    @property
    def GETSETTLEMENTCONFIRMATIONCOINMNDATA_URL(self):
        getSettlementConfirmationColumnData_url = self.base_url +"/api/report/accountStatement/getSettlementConfirmationColumnData"
        return getSettlementConfirmationColumnData_url

    @property
    def QUERYCOLLECTIONEXECUTEPAGEOFWEB_URL(self):
        queryCollectionExecutePageOfWeb_url = self.base_url +"/api/report/accountStatement/queryCollectionExecutePageOfWeb"
        return queryCollectionExecutePageOfWeb_url

    @property
    def RANKINGRECORDGETLIST_URL(self):
        rankingRecordgetList_url = self.base_url +"/api/report/rankingRecord/getList?startTime=2023-06&endTime=2023-06"
        return rankingRecordgetList_url

    @property
    def COMPONENTLISTBYPAGE_URL(self):
        componentlistByPage_url = self.base_url +"/api/report/component/listByPage"
        return componentlistByPage_url

    @property
    def STATISTICSHEAD_URL(self):
        statisticsHead_url = self.base_url +"/api/report/returnedMoney/statisticsHead"
        return statisticsHead_url
    @property
    def STATISTICSLIST_URL(self):
        statisticsList_url = self.base_url +"/api/report/returnedMoney/statisticsList"
        return statisticsList_url

    @property
    def EXPORTPROGRESSPAYMENT_URL(self):
        exportProgressPayment_url = self.base_url+"/api/report/accountStatement/exportProgressPayment"
        return exportProgressPayment_url

    @property
    def RETURNEDMONERYDETAIL_URL(self):
        returnedMoneydetail_url= self.base_url+"/api/report/returnedMoney/detail/1024"
        return returnedMoneydetail_url

    @property
    def ACCOUNTSTATEMENTGETPROJECTOFMONTH_URL(self):
        accountStatementgetProjectOfMonth_url = self.base_url+"/api/report/accountStatement/getProjectOfMonth?startTime=2023-04&endTime=2023-07"
        return accountStatementgetProjectOfMonth_url
    @property
    def ACCOUNTSTATEMENTGETPROJECT_URL(self):
        accountStatementgetProject_url = self.base_url+"/api/report/accountStatement/getProject"
        return accountStatementgetProject_url
    @property
    def ACCOUNTSTATEMENTQUERYPAGEBACK_URL(self):
        accountStatementqueryPageBack_url = self.base_url+"/api/report/accountStatement/queryPageBack"
        return accountStatementqueryPageBack_url
    @property
    def ACCOUNTSTATEMENTGETTOPBACK_URL(self):
        accountStatementgetTopBack_url = self.base_url+"/api/report/accountStatement/getTopBack"
        return accountStatementgetTopBack_url
    @property
    def HISTORYACCOUNTSBYPROJECTID_URL(self):
        historyAccountsByProjectId_url = self.base_url+"/api/report/historyAccounts/historyAccountsByProjectId?projectId=1024"
        return historyAccountsByProjectId_url

    @property
    def ADDHISTORYACCOUNTS_URL(self):
        addHistoryAccounts_url = self.base_url+"/api/report/historyAccounts/addHistoryAccounts"
        return addHistoryAccounts_url
    @property
    def PAGECOMPLAINTCOMPONENT_URL(self):
        pageComplaintComponent_url = self.base_url+"/api/report/complaintParent/pageComplaintComponent"
        return pageComplaintComponent_url

    @property
    def EXPORTCOMPLAINTPARENT_URL(self):
        exportComplaintParent_url = self.base_url+"/api/report/complaintParent/exportComplaintParent"
        return exportComplaintParent_url
    @property
    def COMPLAINTPARENTCENSUS_URL(self):
        complaintParentcensus_url = self.base_url +"/api/report/complaintParent/census"
        return complaintParentcensus_url
    @property
    def COMPLAINTCOSTAFFILIATIONQUERY_URL(self):
        complaintCostAffiliationquery_url = self.base_url+"/api/report/complaintCostAffiliation/query"
        return complaintCostAffiliationquery_url


