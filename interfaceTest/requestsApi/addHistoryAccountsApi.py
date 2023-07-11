import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class addHistoryAccountsApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/historyAccounts/addHistoryAccounts"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def addHistoryAccounts(self):
        """
                   新增或修改历史账款记录
        """
        payload = json.dumps({
            "projectId": "1024",
            "logDTOList": [],
            "receivableAccount": "320",
            "collectAccount": "20",
            "remarks": "7.11备注"
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = addHistoryAccountsApi()
    response = pc.addHistoryAccounts()
    print(response.json())
