import json
import datetime
import time

import seldom
from common.loginApi import Common
class test02material(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_put_material(self):
        """
           物料-修改
        """
        # 用时间戳作为物料编码
        code = datetime.datetime.now()
        code = str(int(time.mktime(code.timetuple())))
        # print(code)
        self.payload = json.dumps({
            "echoMap": {
                "unit": "",
                "updatedBy": "尹小小",
                "warehouseCategory": "",
                "createdBy": "尹小小",
                "supplyType": "自购",
                "mId": {
                    "id": "1607551110933905408",
                    "createTime": "2022-12-27 09:37:06",
                    "createdBy": "1562105981800808448",
                    "updateTime": "2022-12-27 09:37:06",
                    "updatedBy": "1562105981800808448",
                    "label": "钢材类",
                    "parentId": "0",
                    "sortValue": 1,
                    "children": None,
                    "echoMap": {},
                    "treePath": "",
                    "type": "0",
                    "deleteStatus": False
                },
                "orgId": "康酷瑞（广州）装配式建筑有限公司"
            },
            "id": "1684495755609374720",
            "createTime": "2023-07-27 17:27:39",
            "createdBy": "尹小小  2023-07-27 17:07",
            "updateTime": "2023-07-27 17:27:39",
            "updatedBy": "尹小小 2023-07-27 17:07",
            "orgId": "1514430640907354112",
            "name": "钢筋",
            "code": code,
            "specification": "ф8",
            "supplyType": "01",
            "unit": "kg",
            "purchasingCycle": None,
            "proposedPrice": None,
            "allowedPurchase": False,
            "batchNumberManagement": False,
            "crossProjectPick": False,
            "strength": "RRB400",
            "weight": None,
            "material": "钢",
            "state": True,
            "warehouseCategory": "",
            "location": "",
            "safetyStock": None,
            "totalInventory": None,
            "deleteStatus": 0,
            "statisticalClassification": None,
            "isEdit": True,
            "mid": "1607551110933905408",
            "midName": "钢材类"
        })
        self.put("/api/report/material", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
