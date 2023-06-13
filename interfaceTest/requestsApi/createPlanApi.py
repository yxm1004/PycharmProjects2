import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class createPlanApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/masterPlan/createPlan"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def createPlanApl(self):
        """
                       创建主计划
        """
        payload = json.dumps({
            "considerMaintenanceTime": "3",
            "excludeHolidays": [
                "1"
            ],
            "expectedProductCycle": "2",
            "planTime": "3",
            "roundStatus": False
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
   pc = createPlanApi()
   response = pc.createPlanApl()
   print(response.json())


