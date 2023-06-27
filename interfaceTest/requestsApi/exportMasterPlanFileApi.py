import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class exportMasterPlanFileApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/masterPlan/exportMasterPlanFile"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def exportMasterPlanFile(self):
        """
                             导出主计划信息
        """
        payload = json.dumps({
            "createTime": "2023-06",
            "orgIds": [],
            "projectIds": [],
            "version": 0
        })
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = exportMasterPlanFileApi()
    response = pc.exportMasterPlanFile()
    print(response)