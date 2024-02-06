import json
import seldom
from common.loginApi import Common
class testreturnedMoneyexportDetails(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_returnedMoneyexportDetails(self):
        """
            导出回款明细
        """
        self.payload = json.dumps({
            "list": [],
            "orderField": "entry_date",
            "orderType": "ASC",
            "startTime": "2024-01-01",
            "endTime": "2024-01-31"
        })
        self.post("/api/report/returnedMoney/exportDetails", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
