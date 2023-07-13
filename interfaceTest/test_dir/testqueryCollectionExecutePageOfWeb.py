import json
import datetime
import time

import seldom
from common.loginApi import Common

class testqueryCollectionExecutePageOfWeb(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_queryCollectionExecutePageOfWeb(self):
        """
                   web- 查询回款执行
        """
        self.payload = json.dumps({
            "model": {
                "list": [],
                "overdueStatus": 2
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        self.post("/api/report/accountStatement/queryCollectionExecutePageOfWeb", data=self.payload,headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)