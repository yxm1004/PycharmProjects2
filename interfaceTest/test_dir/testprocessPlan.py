import json
import datetime
import time

import seldom
from common.loginApi import Common

class processPlan(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()

    def test_put_processPlan(self):
        """
                       工艺方案修改
        """
        self.payload = json.dumps({
            "id": "1679318602571841536",
            "productionRounds": "2",
            "schemeNumber": "2",
            "schemeSequence": "2",
            "schemeCarNumber": "2",
            "operation": "0"
        })


        self.put("/api/report/processPlan", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
     seldom.main(debug=True)