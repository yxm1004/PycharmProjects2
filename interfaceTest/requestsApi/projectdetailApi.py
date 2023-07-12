import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class projectdetailApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/project/detail/1035"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def projectdetail(self):
        """
                获取项目信息
        """
        self.payload = {}
        response = requests.request("get", self.url, headers=self.headers, data=self.payload)
        return response
if __name__ == '__main__':
    pc = projectdetailApi()
    response = pc.projectdetail()
    print(response.json())

