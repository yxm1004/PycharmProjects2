import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class exportProgressPaymentApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/exportProgressPayment"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def exportProgressPayment(self):
        """
                  回款管理-导出
        """
        payload = json.dumps({
            "current": 1,
            "size": 50,
            "model": {
                "isDelay": False,
                "startTime": "2023-04",
                "endTime": "2023-07",
                "projectIds": []
            },
            "extra": {}
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = exportProgressPaymentApi()
    response = pc.exportProgressPayment()
    print(response)