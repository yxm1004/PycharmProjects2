import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class getProductionMonitoringApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/productionTask/getProductionMonitoring"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def getProductionMonitoring(self):
        """
                实时生产监测
        """
        payload = json.dumps({
            "screen": 0,
            "endTime": "2023-05-31",
            "startTime": "2023-05-01"
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
   pc = getProductionMonitoringApi()
   response = pc.getProductionMonitoring()
   print(response.json())