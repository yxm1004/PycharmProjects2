import json
import seldom
from common.loginApi import Common

class testtransportVehiclegetDriverInfo(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_transportVehiclegetDriverInfo(self):
        """
           执行者视角-滚动交付-获取司机联系信息
        """
        self.payload = {}
        self.get("/api/report/transportVehicle/getDriverInfo?transportVehicle=%E7%9A%96K+3E612&companyName=%E8%BF%90%E7%9B%88%E7%89%A9%E6%B5%81",
                 data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
