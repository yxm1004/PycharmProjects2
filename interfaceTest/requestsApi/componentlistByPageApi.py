import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class componentlistByPageApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/component/listByPage"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def componentlistByPage(self):
        """
                   构件表-分页查询构件列表
        """
        payload = json.dumps({
            "model": {
                "list": [],
                "projectId": "434",
                "isNoProductionTask": True
            },
            "extra": {},
            "current": 1,
            "size": 50,
            "order": "ascend",
            "sort": "floor"
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc =componentlistByPageApi()
    response = pc.componentlistByPage()
    print(response.json())
