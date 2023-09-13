import json
import datetime
import time

import seldom
from common.loginApi import Common
class testexportComponentList(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_exportComponentList(self):
        """
            导出构件清单
        """
        self.payload = json.dumps({
            "projectId": "1058",
            "list": []
        })
        self.post("/api/report/component/exportComponentList", data=self.payloa, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)