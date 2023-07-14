import json
import datetime
import time

import seldom
from common.loginApi import Common

class teststockMonitor(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_stockMonitor(self):
        """
                       实时库存监测
         """
        self.payload = json.dumps({
            "state": 0
        })
        self.post("/api/report/statistics/stockMonitor", data=self.payload,headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)

