import json
import seldom
from common.loginApi import Common
class testeditDeliveryPlan(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_editDeliveryPlan(self):
        """
          发货计划-编辑车辆
        """
        self.payload = json.dumps({
            "id": "1727519518092177408",
            "platformCallTime": None,
            "requiredArrivalTime": "2023-11-23 16:48:30",
            "actualArrivalTime": None,
            "standardLoadingHours": "",
            "vehicleDeliveryTime": None,
            "requireProjectTime": "2023-11-24 10:48:30",
            "arrivalBuildingSiteTime": "2023-12-22 13:58:06",
            "leaveBuildingSiteTime": None
        })
        self.post("/api/report/deliveryPlan/editDeliveryPlan", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
