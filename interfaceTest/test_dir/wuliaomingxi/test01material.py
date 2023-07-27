import json
import datetime
import time

import seldom
from common.loginApi import Common
class testmaterial(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_material(self):
        """
           物料-新增
        """
        # 用时间戳作为项目简称
        code = datetime.datetime.now()
        code = str(int(time.mktime(code.timetuple())))
        # print(abbreviation)
        self.payload = json.dumps({
            "orgId": "1471376234272260096",
            "unit": "kg",
            "code": code,
            "mid": "1607551110933905408",
            "midName": "钢材类",
            "name": "钢筋",
            "specification": "ф8",
            "warehouseCategory": "",
            "location": "",
            "safetyStock": "",
            "supplyType": "01",
            "material": "钢",
            "strength": "RRB400",
            "weight": "",
            "proposedPrice": ""
        })
        self.post("/api/report/material", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)


