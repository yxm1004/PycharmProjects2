import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class  exportMaterialApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/material/exportMaterial"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def exportMaterial(self):
        """
             导出所有物料
        """
        payload = {}
        response = requests.request("get", self.url, headers=self.headers, data=payload)
        return response

if __name__ == '__main__':
    pc = exportMaterialApi()
    response = pc.exportMaterial()
    print(response )