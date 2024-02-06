import json
import seldom
from common.loginApi import Common
class testreturnedMoneydetails(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_returnedMoneydetails(self):
        """
                回款明细
        """
        self.payload = json.dumps({
            "model": {
                "list": [],
                "orderField": "entry_date",
                "orderType": "DESC",
                "startTime": "2024-01-01",
                "endTime": "2024-01-31"
            },
            "extra": {},
            "current": 1,
            "size": 50
        })
        self.post("/api/report/returnedMoney/details", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
