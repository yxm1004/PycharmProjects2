import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class queryBusinessReconciliationStatisticsApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/queryBusinessReconciliationStatistics"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def queryBusinessReconciliationStatistics(self):
        """
                    商务对账-统计
        """
        payload = json.dumps({
            "list": [],
            "overdueStatus": True,
            "projectIdList": []
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = queryBusinessReconciliationStatisticsApi()
    response = pc.queryBusinessReconciliationStatistics()
    print(response.json())

