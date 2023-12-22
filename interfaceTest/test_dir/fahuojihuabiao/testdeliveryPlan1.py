import json
import seldom
from common.loginApi import Common
class testdeliveryPlan1(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_deliveryPlan1(self):
        """
          发货计划-新增
        """
        self.payload = json.dumps({
            "requireProjectTime": "2023-12-22 11:16:08",
            "warning": 1,
            "projectName": "项目1214号-A1#-3",
            "type": "叠合板",
            "inventoryStatus": "02",
            "projectCountpart": "尹小小",
            "projectPhone": "15879654576",
            "projectCountpartList": [
                {
                    "echoMap": {},
                    "id": "1735473416741679104",
                    "createTime": "2023-12-15 09:34:41",
                    "createdBy": "1630382479472852992",
                    "updateTime": "2023-12-15 09:34:41",
                    "updatedBy": "1630382479472852992",
                    "projectId": "1309",
                    "name": "你菜",
                    "phone": "158 7965 4575",
                    "consignee": "尹小小",
                    "consigneePhone": "15879654576",
                    "salesman": "哈米",
                    "salesmanPhone": "131 7097 8240",
                    "building": "A1#"
                }
            ],
            "salesCountpart": "哈米",
            "salesPhone": "131 7097 8240",
            "salesCountpartList": [
                {
                    "echoMap": {},
                    "id": "1735473416741679104",
                    "createTime": "2023-12-15 09:34:41",
                    "createdBy": "1630382479472852992",
                    "updateTime": "2023-12-15 09:34:41",
                    "updatedBy": "1630382479472852992",
                    "projectId": "1309",
                    "name": "你菜",
                    "phone": "158 7965 4575",
                    "consignee": "尹小小",
                    "consigneePhone": "15879654576",
                    "salesman": "哈米",
                    "salesmanPhone": "131 7097 8240",
                    "building": "A1#"
                }
            ],
            "afterSalesCountpart": "你菜",
            "afterSalesPhone": "158 7965 4575",
            "afterSalesCountpartList": [],
            "arrivalBuildingSiteTime": "",
            "requiredArrivalTime": "2023-12-21 17:16:08",
            "platformCallTime": "",
            "standardLoadingHours": "",
            "standardUnloadHours": "",
            "remark": "",
            "building": "A1#",
            "floor": "3",
            "projectId": "1309"
        })
        self.post("/api/report/deliveryPlan", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "该项目A1#-3层已存在"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])


if __name__ == '__main__':
    seldom.main(debug=True)