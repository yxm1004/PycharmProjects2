import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class deliveryscheduleApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/statistics/delivery/schedule"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def deliveryschedule(self):
        """
                实时交付进度
        """
        payload = json.dumps({
            "month": "2023-06-13"
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = deliveryscheduleApi()
    response = pc.deliveryschedule()
    print(response.json())