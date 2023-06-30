import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class queryCollectionExecutePageOfWebAil():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/queryCollectionExecutePageOfWeb"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def queryCollectionExecutePageOfWeb(self):
        """
                   web- 查询回款执行
        """
        payload = json.dumps({
            "model": {
                "list": [],
                "overdueStatus": 2
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = queryCollectionExecutePageOfWebAil()
    response = pc.queryCollectionExecutePageOfWeb()
    print(response.json())