import json
import datetime
import time

import seldom
from common.loginApi import Common

class testcheckInvoicingMoney(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_checkInvoicingMoney(self):
        """
               检查开票金额是否可以编辑
        """
        self.payload = {}
        self.get("/api/report/invoicingRecord/checkInvoicingMoney?id=1682230365931962368&invoicedAmount=1800.00", data=self.payload,
                 headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])