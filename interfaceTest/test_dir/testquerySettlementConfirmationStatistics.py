import json
import datetime
import time

import seldom
from common.loginApi import Common
class testquerySettlementConfirmationStatistics(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_querySettlementConfirmationStatistics(self):
        """
                    结算签确-统计
        """
        self.payload = json.dumps({
            "list": [],
            "overdueStatus": True
        })
        self.post("/api/report/accountStatement/querySettlementConfirmationStatistics", data=self.payload,headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)



