import json
import datetime
import time

import seldom
from common.loginApi import Common

class testaccountStatementquerylist(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_accountStatementquerylist(self):
        """
                对账单-列表查询
        """
        self.payload = json.dumps({
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
        self.post("/api/report/accountStatement/queryList", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])


if __name__ == '__main__':
    seldom.main(debug=True)
