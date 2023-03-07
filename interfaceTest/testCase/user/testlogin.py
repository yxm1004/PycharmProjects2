# -*- coding: utf-8 -*-
import json

import requests
import unittest

from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()


class APITestlogin(unittest.TestCase):
    def test_post_login(self):
        url = localReadConfig.get_http("baseurl")
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': 'Bearer test',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "account": "15313487958",
            "avatar": "",
            "code": "",
            "grantType": "password",
            "key": "",
            "name": "",
            "openId": "",
            "password": "900520",
            "refreshToken": ""
        })
        response = requests.post(url, data=payload, headers=headers)
        #取出响应结果字段
        data1 = json.loads(response.text)
        #多级字段取值
        va=data1["data"]["token"]
        print(va)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
