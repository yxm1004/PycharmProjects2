import json
import seldom
from common.loginApi import Common
class testgetFirstAcceptanceSelectData(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_getFirstAcceptanceSelectData(self):
        """
           获取首件命令单确认下拉数据
        """
        self.payload = json.dumps({
            "taskId": "1697158367316803584",
            "building": "4",
            "floor": 4
        })
        self.post("/api/report/productionTask/getFirstAcceptanceSelectData", data=self.payload,
                  headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)