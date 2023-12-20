import json
import seldom
from common.loginApi import Common
class teststatisticsReportdelayColumnData(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_statisticsReportdelayColumnData(self):
        """
           获取延误统计项目简称,构件类型，协同工厂下拉列表
        """
        self.payload = json.dumps({
            "startTime": "2023-12-01",
            "endTime": "2023-12-19"
        })
        self.post("/api/report/statisticsReport/delayColumnData", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
