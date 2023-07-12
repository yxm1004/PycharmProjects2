import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class updateLimitTimeConfigApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/limitTimeConfig/updateLimitTimeConfig"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def updateLimitTimeConfig(self):
        """
                修改结算回款限时配置
        """
        payload = json.dumps({
            "limitTime": "24",
            "type": 2
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = updateLimitTimeConfigApi()
    response = pc.updateLimitTimeConfig()
    print(response.json())