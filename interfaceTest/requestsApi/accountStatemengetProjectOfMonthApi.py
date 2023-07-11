import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class accountStatementgetProjectOfMonth():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/getProjectOfMonth?startTime=2023-04&endTime=2023-07"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def accountStatementgetProjectOfMonth(self):
        """
                   对账单-自定义分页查询
        """
        payload = {}
        response = requests.request("get", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = accountStatementgetProjectOfMonth()
    response = pc.accountStatementgetProjectOfMonth()
    print(response.json())