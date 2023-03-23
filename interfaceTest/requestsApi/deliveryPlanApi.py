import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class deliveryPlanApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/deliveryPlan"
        # 初始化头部
        lg = loginApi()
        #从登陆类里获取头部
        self.headers = lg.getheaders()
    def deliveryPlan(self):
        """
            发货计划-新增
        """
        payload = json.dumps({
            "requireProjectTime": "2023-03-23 18:04:22",
            "warning": 0,
            "projectName": "交付0323-6-3",
            "type": "叠合板",
            "inventoryStatus": "01",
            "projectCountpart": "尹小小",
            "projectPhone": "13170978240",
            "salesCountpart": "尹卡卡",
            "salesPhone": "153 1348 7958",
            "afterSalesCountpart": "",
            "afterSalesPhone": "",
            "arrivalBuildingSiteTime": "",
            "requiredArrivalTime": "",
            "platformCallTime": "",
            "standardLoadingHours": "",
            "standardUnloadHours": "",
            "remark": "",
            "building": "6",
            "floor": "3",
            "projectId": "461"
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = deliveryPlanApi()
    response=pc.deliveryPlan()
    print(response.json())