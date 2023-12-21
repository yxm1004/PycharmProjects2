import json
import seldom
from common.loginApi import Common
class testprojectCustomer(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_projectCustomer(self):
        """
           项目联系人-新增
        """
        self.payload = json.dumps({
            "projectId": "434",
            "building": "6",
            "consignee": "尹小小",
            "consigneePhone": "13170978240",
            "salesman": "尹卡卡",
            "salesmanPhone": "15313487958",
            "name": "",
            "phone": ""
        })
        self.post("/api/report/projectCustomer", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "该项目6楼栋已存在"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])


if __name__ == '__main__':
    seldom.main(debug=True)
