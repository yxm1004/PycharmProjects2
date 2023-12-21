import json
import seldom
from common.loginApi import Common
class testtransportVehicle(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_transportVehicle(self):
        """
           车辆司机-新增
        """
        self.payload = json.dumps({
            "companyName": "顺丰物流",
            "transportVehicle": "赣D123457",
            "carLength": "10",
            "driverName": "小尹",
            "driverPhone": "15313487958",
            "driverName2": "",
            "driverPhone2": "",
            "driverName3": "",
            "driverPhone3": ""
        })
        self.post("/api/report/transportVehicle", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "该运输车辆赣D123457已存在顺丰物流公司旗下！"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])


if __name__ == '__main__':
    seldom.main(debug=True)


