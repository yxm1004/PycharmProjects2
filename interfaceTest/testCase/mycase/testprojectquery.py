import unittest
import json
import requests

class testreport(unittest.TestCase ):
    def test_post_report (self):
        url = "https://cz-api-test.dalezhuang.com/api/report/project/query/page"

        payload = json.dumps({
            "current": 1,
            "extra": {},
            "model": {
                "list": [
                    {
                        "calSymbol": "",
                        "columnFileKey": "",
                        "columnFileValue": "",
                        "dataType": ""
                    }
                ],
                "orderField": "",
                "orderType": "",
                "searchDTO": {
                    "columns": [],
                    "keyword": ""
                },
                "specialSearch": {
                    "columnFileKey": "",
                    "valueList": []
                }
            },
            "order": "descending",
            "size": 10,
            "sort": "id"
        })
        headers = {
            'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
            'tenant': 'ZGdnYw==',
            'token': 'Bearer test',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)


        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest .mian()

