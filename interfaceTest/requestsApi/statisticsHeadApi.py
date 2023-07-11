import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class statisticsHeadApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/returnedMoney/statisticsHead"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def statisticsHeard(self):
        """
                  回款管理列表头部统计
        """
        payload = json.dumps({
            "startTime": "2023-04",
            "endTime": "2023-07"
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = statisticsHeadApi()
    response = pc.statisticsHeard()
    print(response.json())
