import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class rankingRecordgetListApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/rankingRecord/getList?startTime=2023-06&endTime=2023-06"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def rankingRecordgetList(self):
        """
                   回款排行表列表
        """
        payload = {}
        response = requests.request("get", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = rankingRecordgetListApi()
    response = pc.rankingRecordgetList()
    print(response.json())
