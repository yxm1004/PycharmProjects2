import json
import datetime
import time

import seldom
from common.loginApi import Common

class testqueryBusinessReconciliationStatistics(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_queryBusinessReconciliationStatistics(self):
        """
                    商务对账-统计
        """
        self.payload = json.dumps({
            "list": [],
            "overdueStatus": True,
            "projectIdList": []
        })
        self.post("/api/report/billboards/yesterday/totalAmount", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)

