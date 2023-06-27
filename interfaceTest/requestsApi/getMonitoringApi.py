import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class getMonitoringApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/billboards/getMonitoring"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def getMonitoring(self):
        """
                实时质量监测
        """
        payload = json.dumps({
            "screen": 0,
            "endTime": "2023-05-31",
            "startTime": "2023-05-01"
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = getMonitoringApi()
    response = pc.getMonitoring()
    print(response.json())