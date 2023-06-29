import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class getSettlementConfirmationColumnDataApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/getSettlementConfirmationColumnData"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def getSettlementConfirmationColumnData(self):
        """
                   web- 结算签确-获取列表筛选数据
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
    pc = getSettlementConfirmationColumnDataApi()
    response = pc.getSettlementConfirmationColumnData()
    print(response.json())

