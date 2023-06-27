import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class materialqueryPageAPi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/material/queryPage"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def materialqueryPage(self):
        """
                物料主档自定义分页查询
        """
        payload = json.dumps({
            "model": {
                "list": []
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = materialqueryPageAPi()
    response = pc.materialqueryPage
    print(response)