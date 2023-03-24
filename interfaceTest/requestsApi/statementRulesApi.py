import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class statementRulesApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/subcontractingStatementRules/queryPage"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def statementRulesApi(self):
        """
                   获取委外对账规则列表
        """
        payload = "{\"model\":{\"list\":[],\"settleDays\":[],\"status\":\"1,2\"},\"extra\":{},\"current\":1,\"size\":50}S"
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = statementRulesApi()
    response = pc.statementRulesApi()
    print(response.json())



