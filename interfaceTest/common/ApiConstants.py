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
    def ACCOUNTSTATEMENTQUERY_URL(self):
        accountStatementquery_url = self .base_url +"/api/report/accountStatement/queryPage"
        return accountStatementquery_url

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

