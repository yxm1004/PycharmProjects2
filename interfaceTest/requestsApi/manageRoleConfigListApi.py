import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class manageRoleConfigListApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/manageRoleConfig/manageRoleConfigList"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def manageRoleConfigList(self):
        """
                任务管理岗位配置列表
        """
        payload = json.dumps({
            "type": 2
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = manageRoleConfigListApi()
    response = pc.manageRoleConfigList()
    print(response.json())