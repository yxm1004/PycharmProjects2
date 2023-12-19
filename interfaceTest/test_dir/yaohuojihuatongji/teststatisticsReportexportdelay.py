import json
import seldom
from common.loginApi import Common
class teststatisticsReportexportdelay(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_statisticsReportexportdelay(self):
        """
           延误统计列表导出
        """
        self.payload = json.dumps({
            "startTime": "2023-12-01",
            "endTime": "2023-12-19",
            "list": []
        })
        self.post("/api/report/statisticsReport/export/delay", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
