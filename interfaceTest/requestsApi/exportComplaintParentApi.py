import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class exportComplaintParentApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/complaintParent/exportComplaintParent"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def exportComplaintParent(self):
        """
                客诉单分页列表
        """
        payload = json.dumps({
            "endTime": "2023-05-15",
            "startTime": "2023-04-15"
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = exportComplaintParentApi()
    response = pc.exportComplaintParent()
    print(response.json())

