import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class projectCustomerApi:
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/projectCustomer"
        # 初始化头部
        lg = loginApi()
        #从登陆类里获取头部
        self.headers = lg.getheaders()
    def projectCustomer(self):
        """
            项目联系人-新增
        """
        payload = json.dumps({
            "projectId": "434",
            "building": "6",
            "consignee": "尹小小",
            "consigneePhone": "13170978240",
            "salesman": "尹卡卡",
            "salesmanPhone": "15313487958",
            "name": "",
            "phone": ""
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    #这只是实例化了
    pc = projectCustomerApi()
    #调用项目联系人新增方法
    response=pc.projectCustomer()
    print(response.json())
