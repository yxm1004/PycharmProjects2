import json
import datetime
import time

import seldom
from common.loginApi import Common

class testquerycreatedYearMonth(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_querycreatedYearMonth(self):
        """
                查询已经创建主计划的年月份
        """
        self.payload = {}
        self.get("/api/report/masterPlan/queryCreatedYearMonth", data=self.payload, headers=self.header)
        self.assertStatusCode(200)



if __name__ == '__main__':
    seldom.main(debug=True)