import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class complaintParentcensusApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/complaintParent/census"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def complaintParentcensus(self):
        """
                客诉-顶部统计
        """
        payload = {}
        response = requests.request("get", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc =complaintParentcensusApi()
    response = pc.complaintParentcensus()
    print(response.json())