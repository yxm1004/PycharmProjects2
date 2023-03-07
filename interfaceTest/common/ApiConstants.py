from interfaceTest import readConfig
localReadConfig = readConfig.ReadConfig()
class ApiConstants:
    @property
    def BASE_URL(self):
        base_url = localReadConfig.get_http("baseurl")
        return base_url

    # LOGIN_URL=BASE_URL+"/api/oauth/noToken/login"
    # PROJECTCREAT_URL=BASE_URL+"/api/report/project/create"
    # PROJECTQUERY_URL=BASE_URL+"/api/report/project/query/page"
    # PROJECTRENAME_URL=BASE_URL+"/api/report/bom/projectFile/rename"