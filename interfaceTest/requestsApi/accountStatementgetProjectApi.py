import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class accountStatementgetProjectApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/getProject"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def accountStatementgetProject(self):
        """
                   进度款明细-项目筛选
        """
        payload = json.dumps({
            "time": "2023"
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = accountStatementgetProjectApi()
    response = pc.accountStatementgetProject()
    print(response.json())