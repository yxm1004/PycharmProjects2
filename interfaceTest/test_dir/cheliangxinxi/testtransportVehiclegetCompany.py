import json
import seldom
from common.loginApi import Common
class testtransportVehiclegetCompany(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_transportVehiclegetCompany(self):
        """
           获取承运公司
        """
        self.payload = {}
        self.get("/api/report/transportVehicle/getCompany?companyName=%E4%B8%9C%E8%8E%9E%E7%89%A9%E6%B5%81", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
