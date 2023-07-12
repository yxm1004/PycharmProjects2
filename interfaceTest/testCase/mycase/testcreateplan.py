import unittest
import requests
import json
from interfaceTest.common.GetToken import Token
from interfaceTest import readConfig


localReadConfig = readConfig.ReadConfig()
class testcreateplan(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 获取token
        tk = Token()
        self.token = 'Bearer ' + tk.get_token()
        print("self.token-------", self.token)

    def test_post_createplan(self):
        # 获取baseurl
        baseurl = localReadConfig.get_http("baseurl")
        url = baseurl + "/api/report/bom/projectFile/rename"
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
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()

