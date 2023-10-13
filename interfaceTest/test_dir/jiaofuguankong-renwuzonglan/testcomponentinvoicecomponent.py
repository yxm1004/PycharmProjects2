import json
import seldom
from common.loginApi import Common
class testcomponentinvoicecomponent(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_componentinvoicecomponent(self):
        """
           执行者视角-滚动交付-发货单构件添加
        """
        self.payload = json.dumps({
            "model": {
                "list": [
                    {
                        "columnFileValue": "1",
                        "columnFileKey": "scheme_car_number",
                        "calSymbol": 4,
                        "dataType": 3
                    }
                ],
                "screenList": [
                    {
                        "building": "2",
                        "floor": "2"
                    }
                ],
                "projectId": "1111",
                "relateInvoice": True
            },
            "extra": {},
            "current": 1,
            "size": 50,
            "order": "ascending,ascending,ascending,ascending",
            "sort": "building,floor,model,schemeCarNumber"
        })
        self.post("/api/report/component/invoice/component",data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)