import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class accountStatementgetMonitoringApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/getMonitoring"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def accountStatementgetMonitoring(self):
        """
                对账回款监测
        """
        payload = json.dumps({
            "screen": 0,
            "endTime": "2023-05-31",
            "startTime": "2023-05-01"
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = accountStatementgetMonitoringApi()
    response = pc.accountStatementgetMonitoring()
    print(response.json())