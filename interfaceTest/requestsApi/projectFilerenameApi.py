import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class projectrFilerenameApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/bom/projectFile/rename"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def projectrFilerename(self):
        payload = json.dumps({
            "fileId": "1632951176049876992",
            "name": "香江悦府20"
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = projectrFilerenameApi()
    response = pc.projectrFilerename()
    print(response.json())

