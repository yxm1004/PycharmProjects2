import json
import seldom
from common.loginApi import Common
class testreturnedMoneygetColumnData(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_returnedMoneygetColumnData(self):
        """
            回款明细--获取列筛选数据
        """
        self.payload = json.dumps({
            "columnKey": "abbreviation",
            "dataType": "2",
            "list": [
                {
                    "dataType": "3",
                    "columnFileValue": "2024-01-01,2024-01-31",
                    "columnFileKey": "entry_date",
                    "calSymbol": "3"
                }
            ]
        })
        self.post("/api/report/returnedMoney/getColumnData", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)