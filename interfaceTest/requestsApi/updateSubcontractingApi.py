import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()
class updateSubcontractingApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/subcontractingStatementRules/updateSubcontracting"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def updateSubcontracting(self):
        """
                   修改委外对账配置
        """
        payload = json.dumps({
            "guaranteProportion": 5,
            "id": 0,
            "orderAllocation": 0,
            "outOrderAllocationDTOS": [
                {
                    "code": "WW20230324",
                    "coordinationFactory": "大乐装(惠州)",
                    "details": [
                        {
                            "building": "6",
                            "floors": [
                                3
                            ],
                            "schemeCarNumbers": [],
                            "type": "叠合板",
                            "unitPrice": 990
                        }
                    ],
                    "enclosure": "",
                    "orgId": 1514430640907354000
                }
            ],
            "projectId": 461,
            "projectType": 0,
            "receivableProportion": 15,
            "settleDay": 1,
            "settleStyle": 2,
            "settlementFundsProportion": 30
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = updateSubcontractingApi()
    response = pc.updateSubcontracting()
    print(response.json())
