import unittest

import requests
import json


class APITestmycase(unittest.TestCase):
    def test_post_page(self):
        url = "https://cz-api-test.dalezhuang.com/api/report/party/invoice/detail/page"
        payload = json.dumps({
            "current": 1,
            "extra": {},
            "model": {
                "id": 1631594528563527700,
                "projectId": 0,
                "tenantCode": ""
            },
            "order": "descending",
            "size": 999,
            "sort": "id"
        })
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': 'Bearer test',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        #断言
        self.assertEqual(response.status_code, 200)

# 测试这个方法
if __name__ == '__main__':
    unittest.main()
