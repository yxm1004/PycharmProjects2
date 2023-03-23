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