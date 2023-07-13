import json
import datetime
import time

import seldom
from common.loginApi import Common

class testdeliveryschedule(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_deliveryschedule(self):
        """
                实时交付进度
        """
        self.payload = json.dumps({
            "month": "2023-06-13"
        })
        self.post("/api/report/statistics/delivery/schedule", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)

