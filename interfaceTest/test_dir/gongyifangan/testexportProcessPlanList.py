import json
import datetime
import time

import seldom
from common.loginApi import Common
class testexportProcessPlanList(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_exportProcessPlanList(self):
        """
            导出工艺方案列表
        """
        self.payload = json.dumps({
            "projectId": "1061"
        })
        self.post("/api/report/processPlan/exportProcessPlanList", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
