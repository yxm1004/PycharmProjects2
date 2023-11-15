import json
import seldom
from common.loginApi import Common
class testqueryDeliverInspectionStatisticsOfManage(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_queryDeliverInspectionStatisticsOfManage(self):
        """
           管理者视角-质量管控-发货检查头部统计
        """
        self.payload = json.dumps({
            "startTime": "2023-11-01",
            "endTime": "2023-11-15"
        })
        self.post("/api/report/workbenchTaskRecord/queryDeliverInspectionStatisticsOfManage", data=self.payload,
                  headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)