import json
import datetime
import time

import seldom
from common.loginApi import Common

class queryBusinessReconciliationApi(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_queryBusinessReconciliation(self):
        """
                       商务对账-分页查询
        """
        self.payload = json.dumps({
            "model": {
                "list": [],
                "overdueStatus": True
            },
            "extra": {},
            "current": 1,
            "size": 50
        })

        self.put("/api/report/accountStatement/queryBusinessReconciliation", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
