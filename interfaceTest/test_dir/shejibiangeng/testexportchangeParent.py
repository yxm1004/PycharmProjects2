import json
import seldom
from common.loginApi import Common
class testexportchangeParent(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_exportchangeParent(self):
        """
            设计工单导出
        """
        self.payload = json.dumps({
            "endTime": "2023-07-20",
            "startTime": "2023-07-01"
        })
        self.post("/api/report/changeParent/export/changeParent", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
