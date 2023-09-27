import json
import seldom
from common.loginApi import Common
class testgetDeliveryPlanDTO(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_get_getDeliveryPlanDTO(self):
        """
           执行者视角-滚动交付-根据交付计划id查询交付计划
        """
        self.payload = {}
        self.get("/report/deliveryPlan/getDeliveryPlanDTO?id=1696720741711478784&appendStatus=0", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

