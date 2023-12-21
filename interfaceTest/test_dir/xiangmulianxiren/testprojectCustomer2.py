import json
import seldom
from common.loginApi import Common
class testprojectCustomer2(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_put_projectCustomer2(self):
        """
           项目联系人-修改
        """
        self.payload = json.dumps({
            "echoMap": {
                "projectId": "项目1214号"
            },
            "id": "1735473491769389056",
            "createTime": "2023-12-15 09:34:59",
            "createdBy": "1630382479472852992",
            "updateTime": "2023-12-15 09:34:59",
            "updatedBy": "1630382479472852992",
            "projectId": "1309",
            "name": "你菜",
            "phone": "15879654575",
            "consignee": "尹晓梅12",
            "consigneePhone": "15313487958",
            "salesman": "哈米",
            "salesmanPhone": "13170978240",
            "building": "B2#"
        })
        self.post("/api/report/projectCustomer", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

