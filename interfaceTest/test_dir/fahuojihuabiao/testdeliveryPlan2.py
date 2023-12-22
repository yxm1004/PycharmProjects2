import json
import seldom
from common.loginApi import Common
class testdeliveryPlan2(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_put_deliveryPlan2(self):
        """
          发货计划-修改
        """
        self.payload = json.dumps({
            "echoMap": {
                "inventoryStatus": "无库存",
                "projectId": "设计院1123号",
                "logisticsStatus": "已送达",
                "status": "已制单"
            },
            "id": "1727519518092177408",
            "requireGoodsTime": None,
            "temporaryDelivery": None,
            "requireProjectTime": "2023-11-24 10:48:30",
            "requireProjectDate": None,
            "projectId": "1284",
            "projectName": None,
            "building": "3#",
            "floor": "3",
            "type": "叠合板",
            "trainNumber": "1",
            "inventoryStatus": "02",
            "invoiceId": "1727580268135510016",
            "code": "SO20231123001",
            "status": 1,
            "afterSalesCountpart": "尹晓梅",
            "afterSalesPhone": "153 1348 7958",
            "projectCountpart": "尹哈哈",
            "projectPhone": "18979687606",
            "salesCountpart": "尹晓梅",
            "salesPhone": "153 1348 7958",
            "platformCallTime": None,
            "requiredArrivalTime": "2023-11-23 16:48:30",
            "actualArrivalTime": None,
            "vehicleDeliveryTime": None,
            "arrivalBuildingSiteTime": "2023-12-22 11:58:06",
            "requiredArrivalBuildingSiteTime": None,
            "leaveBuildingSiteTime": None,
            "carLength": None,
            "transportCompany": "运盈物流",
            "transportVehicle": "晋ML2128",
            "driverName": "廖更强",
            "driverPhone": "15014791599",
            "hoistingReview": None,
            "problemAttribution": None,
            "delayTime": "0",
            "loadedTimeout": "0.0",
            "waitTime": "0",
            "transportTime": "0",
            "retentionTime": "0.0",
            "createTime": "2023-11-23 10:48:44",
            "warning": 2,
            "area": None,
            "logisticsStatus": 5,
            "logisticsTime": -673,
            "major": 2,
            "exception": 0,
            "standardLoadingHours": "",
            "standardUnloadHours": "",
            "noteList": None,
            "remark": "",
            "isExtra": False,
            "isShowButton": True,
            "sendTime": None,
            "createMark": True,
            "clientName": "白云建筑局",
            "deliveryAddress": "广东省广州市白云区白云建筑局01",
            "manufacturer": "合同归属新-深圳大乐装（南山）",
            "note": None,
            "projectStatus": 0,
            "orgId": "1514430640907354112",
            "orgName": None,
            "logisticsNumber": 1,
            "collaborativeFactory": "大乐装（东莞）",
            "collaborativeFactoryId": "1514430716274802688",
            "orderCoordinationFactoryId": "1514430716274802688"
        })
        self.put("/api/report/deliveryPlan", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
