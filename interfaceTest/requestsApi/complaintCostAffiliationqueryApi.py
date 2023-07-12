import requests
import json

from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi

localRedConfig = readConfig.ReadConfig()

class complaintCostAffiliationqueryApi():
    def __init__(self):
        baseurl = localRedConfig.get_http("baseurl")
        self.url = baseurl+"/api/report/complaintCostAffiliation/query"
        #初始化头部
        lg = loginApi()
        #从登陆类里获取头部
        self .headers = lg.getheaders()
    def complaintCostAffiliationquery(self):
        """
                客诉-费用归属-批量查询
        """
        payload = json.dumps({})
        response = requests.request("post", self.url, headers=self.headers, data=payload)
        return response
if __name__ == '__main__':
    pc = complaintCostAffiliationqueryApi()
    response = pc.complaintCostAffiliationquery()
    print(response.json())

