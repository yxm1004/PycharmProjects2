import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class querySettlementConfirmationStatisticsApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/queryAllStatistics"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def querySettlementConfirmationStatistics(self):
        """
                    结算签确-统计
        """

    payload = json.dumps({
        "list": [],
        "overdueStatus": True
    })
    response = requests.request("post", self.url, headers=self.headers, data=payload)
    return response

