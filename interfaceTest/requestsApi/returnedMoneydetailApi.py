import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class returnedMoneydetailApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/returnedMoney/detail/1024"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def returnedMoneydetail(self):
        """
                  回款详情
        """
        payload = {}
        response = requests.request("get", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = returnedMoneydetailApi()
    response = pc.returnedMoneydetail()
    print(response.json())