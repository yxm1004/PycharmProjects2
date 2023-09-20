import json
import seldom
from common.loginApi import Common
class testqueryRollingDelivery(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_queryRollingDelivery(self):
        """
           执行者视角-获取滚动交付列表
        """
        self.payload = json.dumps({
            "current": 1,
            "model": {
                "todo": False,
                "projectIdList": []
            },
            "order": "descending",
            "size": 10,
            "sort": "id",
            "projectIds": []
        })
        self.post("/api/report/workbenchTaskRecord/queryRollingDelivery", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

