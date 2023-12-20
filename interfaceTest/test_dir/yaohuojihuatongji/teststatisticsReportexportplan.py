import json
import seldom
from common.loginApi import Common
class teststatisticsReportexportplan(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_tstatisticsReportexportplan(self):
        """
           要货计划列表导出
        """
        self.payload = json.dumps({
            "startTime": "2023-12-01",
            "endTime": "2023-12-19",
            "orgIds": [],
            "list": [],
            "orderField": "totalCount",
            "orderType": "DESC"
        })
        self.post("/api/report/statisticsReport/export/plan", data=self.payload, headers=self.header)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
