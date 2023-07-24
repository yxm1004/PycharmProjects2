import json
import datetime
import time

import seldom
from common.loginApi import Common

class testinvoicingRecordqueryPage(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_testinvoicingRecordqueryPage(self):
        """
                    开票登记-自定义分页查询
        """
        self.payload = json.dumps({
            "model": {
                "list": [],
                "projectId": "1063"
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        self.post("/api/report/invoicingRecord/queryPage", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])


if __name__ == '__main__':
    seldom.main(debug=True)