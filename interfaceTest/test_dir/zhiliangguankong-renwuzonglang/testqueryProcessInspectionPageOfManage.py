import json
import seldom
from common.loginApi import Common

class testqueryProcessInspectionPageOfManage(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_queryProcessInspectionPageOfManage(self):
        """
           管理者视角-质量管控-查询工序检查
        """
        self.payload = json.dumps({
            "model": {
                "startTime": "2023-11-01",
                "endTime": "2023-11-15"
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        self.post("/api/report/workbenchTaskRecord/queryProcessInspectionPageOfManage", data=self.payload,
                 headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
