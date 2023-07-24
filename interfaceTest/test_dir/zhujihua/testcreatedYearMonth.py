import json
import datetime
import time

import seldom
from common.loginApi import Common

class testcreatedYearMonth(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_createdYearMonth(self):
        """
                对账单-列表查询
        """
        self.payload = {}
        self.get("/api/report/masterPlan/versionList?createdYearMonth=2023-06", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        self.assertEqual(msg="成功")


if __name__ == '__main__':
    seldom.main(debug=True)