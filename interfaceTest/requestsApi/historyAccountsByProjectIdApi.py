import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class historyAccountsByProjectId():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/historyAccounts/historyAccountsByProjectId?projectId=1024"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def historyAccountsByProjectId(self):
        """
                   查询项目历史对账日志详情
        """
        payload = {}
        response = requests.request("get", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = historyAccountsByProjectId()
    response =pc.historyAccountsByProjectId()
    print(response.json())