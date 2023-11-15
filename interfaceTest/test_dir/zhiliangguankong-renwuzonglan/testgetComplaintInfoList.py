import json
import seldom
from common.loginApi import Common
class testgetComplaintInfoList(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_getComplaintInfoList(self):
        """
           执行者视角-质量管控-客诉跟进
        """
        self.payload = json.dumps({
            "projectIds": [],
            "todo": False
        })
        self.post("/api/report/workbenchTaskRecord/getComplaintInfoList", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)