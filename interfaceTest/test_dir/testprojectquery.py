import json
import datetime
import time

import seldom
from common.loginApi import Common

class testprojectquery(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()

    def test_post_projectquerypage (self):
        """
                       分页查询项目列表
        """
        self.payload = json.dumps({
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
        self.post("/api/report/project/query/page", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)


