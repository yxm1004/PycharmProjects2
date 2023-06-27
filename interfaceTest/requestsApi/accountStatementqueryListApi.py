import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localReadConfig = readConfig.ReadConfig()

class accountStatementquerylistApi():
    def __init__(self):
        baseurl = localReadConfig.get_http("baseurl")
        self.url = baseurl + "/api/report/accountStatement/getMonitoring"
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()
    def accountStatementquerylist(self):
        """
                对账单-列表查询
        """
        payload = json.dumps({
            "list": [
                {
                    "columnFileValue": 0,
                    "columnFileKey": "check_status",
                    "calSymbol": 4,
                    "dataType": 1
                },
                {
                    "columnFileValue": 0,
                    "columnFileKey": "overdueDays",
                    "calSymbol": 7,
                    "dataType": 1
                }
            ],
            "orderField": "overdueDays",
            "orderType": "DESC",
            "endTime": "2023-05-31",
            "startTime": "2023-05-01"
        })
        response = requests.request("POST", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = accountStatementquerylistApi()
    response = pc.accountStatementquerylist()
    print(response.json())