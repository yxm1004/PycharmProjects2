import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class querySettlementConfirmationApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/querySettlementConfirmation"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def querySettlementConfirmation(self):
        """
                    结算签确-分页查询
        """
        payload = json.dumps({
            "model": {
                "list": [],
                "overdueStatus": True
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = querySettlementConfirmationApi()
    response = pc.querySettlementConfirmation()
    print(response.json())