import json
import seldom
from common.loginApi import Common
class testexportProgressPayment(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_exportProgressPayment(self):
        """
                回款管理-导出
        """
        self.payload = json.dumps({
            "current": 1,
            "size": 50,
            "model": {
                "isDelay": False,
                "startTime": "2023-04",
                "endTime": "2023-07"
            },
            "extra": {}
        })
        self.post("/api/report/accountStatement/exportProgressPayment", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
