import json
import seldom
from common.loginApi import Common
class testtransportVehicle(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_put_transportVehicle(self):
        """
           车辆信息-修改
        """
        self.payload = json.dumps({
            "companyName": "东莞物流",
            "transportVehicle": "粤E123457",
            "carLength": "13.5",
            "driverName": "尹晓梅",
            "driverPhone": "15313487958",
            "driverName2": "",
            "driverPhone2": "",
            "driverName3": "",
            "driverPhone3": "",
            "id": "1735468733717377024"
        })
        self.put("/api/report/transportVehicle", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
