import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class yesterdaytotalAmountApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/billboards/yesterday/totalAmount"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def yesterdaytotalAmount(self):
        """
                           获取昨日产值-交付值
            """

        payload = {}
        response = requests.request("get", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = yesterdaytotalAmountApi()
    response = pc.yesterdaytotalAmount()
    print(response.json())