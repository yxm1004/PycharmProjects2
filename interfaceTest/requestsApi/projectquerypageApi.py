import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class projectquerypageApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/project/query/page"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def projectquerypage(self):
        """
                分页查询项目列表
        """
        payload = json.dumps({
            "model": {
                "list": [],
                "projectStatus": "1"
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = projectquerypageApi()
    response = pc.projectquerypage()
    print(response.json())
