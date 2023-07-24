import json
import datetime
import time

import seldom
from common.loginApi import Common

class testmasterPlan(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_masterPlan(self):
        """
                       历史版本——主计划
        """
        self.payload = {}
        self.get("/api/report/masterPlan/versionList?createdYearMonth=2023-06", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])

if __name__ == '__main__':
    seldom.main(debug=True)

