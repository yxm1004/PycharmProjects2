import unittest
import requests
import json
from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig
from interfaceTest.requestsApi.loginApi import loginApi


localReadConfig = readConfig.ReadConfig()
class testcreateplan(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 获取token
        tk = Token()
        self.token = 'Bearer ' + tk.get_token()
        print("self.token-------", self.token)
        # 初始化头部
        lg = loginApi()
        # 从登陆类里获取头部
        self.headers = lg.getheaders()

    def test_post_createplan(self):
        # 获取baseurl
        baseurl = localReadConfig.get_http("baseurl")
        url = baseurl + "/api/report/masterPlan/createPlan"
        """
                       创建主计划
        """

        payload = json.dumps({
            "considerMaintenanceTime": "3",
            "excludeHolidays": [
                "1"
            ],
            "expectedProductCycle": "2",
            "planTime": "3",
            "roundStatus": False
        })
        response = requests.request("POST", url, headers=self.headers, data=payload)
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()

