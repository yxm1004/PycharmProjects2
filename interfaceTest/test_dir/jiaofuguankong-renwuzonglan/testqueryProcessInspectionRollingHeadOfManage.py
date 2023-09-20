import json
import seldom
from common.loginApi import Common
class testqueryProcessInspectionRollingHeadOfManage(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_queryProcessInspectionRollingHeadOfManage(self):
        """
           管理者视角-滚动量产-工序检查头部统计
        """
        self.payload = json.dumps({
            "endTime": "2023-09-30",
            "startTime": "2023-09-01",
            "overdue": True
        })
        self.post("/api/report/workbenchTaskRecord/queryProcessInspectionRollingHeadOfManage", data=self.payload,
                    headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

