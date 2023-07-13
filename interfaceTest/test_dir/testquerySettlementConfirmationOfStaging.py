import json
import datetime
import time

import seldom
from common.loginApi import Common
class testquerySettlementConfirmationOfStaging(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_querySettlementConfirmationOfStaging(self):
        """
                    工作台结算签确-分页查询
        """
        self.payload = json.dumps({
            "current": 1,
            "model": {
                "unDealStatus": False
            },
            "order": "descending",
            "size": 10,
            "sort": "id"
        })
        self.post("/api/report/accountStatement/querySettlementConfirmationOfStaging", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)