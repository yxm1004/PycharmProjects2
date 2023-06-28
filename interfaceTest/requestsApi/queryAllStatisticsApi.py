import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class queryAllStatisticsApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/queryAllStatistics"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def queryAllStatistics(self):
        """
                    结算回款-总统计
        """
        payload = json.dumps({
            "directors": [],
            "overdueStatus": True,
            "projectIdList": [],
            "projectStatusList": [],
            "salePersonList": []
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = queryAllStatisticsApi()
    response = pc.queryAllStatistics()
    print(response.json())