import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class accountStatementgetTopBackApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/getTopBack"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def accountStatementgetTopBack(self):
        """
                   进度款明细-顶部查询
        """
        payload = json.dumps({
            "current": 1,
            "size": 50,
            "model": {
                "time": "2023"
            },
            "extra": {}
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = accountStatementgetTopBackApi()
    response = pc.accountStatementgetTopBack()
    print(response.json())