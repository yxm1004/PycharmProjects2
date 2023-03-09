import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class transportVehicleApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/transportVehicle"
        # 初始化头部
        lg = loginApi()
        #从登陆类里获取头部
        self.headers = lg.getheaders()
    def transportVehicle(self):
        """
            车辆司机-新增
        """
        payload = json.dumps({
            "companyName": "顺丰物流",
            "transportVehicle": "赣D8888",
            "carLength": "10",
            "driverName": "小尹",
            "driverPhone": "15313487958",
            "driverName2": "",
            "driverPhone2": "",
            "driverName3": "",
            "driverPhone3": ""
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = transportVehicleApi()
    response=pc.transportVehicle()
    print(response.json())