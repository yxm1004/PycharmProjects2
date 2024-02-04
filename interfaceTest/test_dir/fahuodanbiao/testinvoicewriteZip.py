import json
import seldom
from common.loginApi import Common
class testinvoicewriteZip(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_invoicewriteZip(self):
        """
          根据筛选条件批量下载销售发货单
        """
        self.payload = json.dumps({
            "projectIds": [
                "1166",
                "1188",
                "1194",
                "1257",
                "1260",
                "1261",
                "1270",
                "1274",
                "1275",
                "1278",
                "1279",
                "1280",
                "1282",
                "1283",
                "1284",
                "1296"
            ],
            "endTime": "2023-11-30",
            "startTime": "2023-11-01",
            "tenant": "ZGdnYw=="
        })
        self.post("/api/report/invoice/writeZip", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
