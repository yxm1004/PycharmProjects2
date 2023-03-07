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
    def PROJECTRENAME_URL(self):
        projectrename_url = self.base_url + "/api/report/bom/projectFile/rename"
        return projectrename_url

    @property
    def COMPONENTSAVE_URL(self):
        componentsave_url=self.base_url +"/api/report/component/saveComponentAndBom"
        return componentsave_url

    @property
    def CONFIRMCOMPONENTANDBOM_URL(self):
        confirmComponentAndBom_url = self.base_url + "/api/report/component/confirmComponentAndBom"
        return confirmComponentAndBom_url
