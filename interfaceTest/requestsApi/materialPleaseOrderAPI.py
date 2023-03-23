import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class materialPleaseOrderApi():
      def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/materialPleaseOrder/batchSave"
        # 初始化头部
        lg = loginApi()
        #从登陆类里获取头部
        self.headers = lg.getheaders()
      def materialPleaseOrder(self):
          """
                     新增物料请购单-新增
          """
          payload = json.dumps([
              {
                  "building": "6",
                  "floor": "2",
                  "floorLevels": 1,
                  "projectId": 461,
                  "requiredTime": "2023-03-10"
              }
          ])
          response = requests.request("POST", self.url, headers=self.headers, data=payload)
          return response
if __name__ == '__main__':
    pc = materialPleaseOrderApi()
    response = pc.materialPleaseOrder()
    print(response.json())



