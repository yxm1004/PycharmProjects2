import json
import seldom
from common.loginApi import Common
class testprojectupdate(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_projectupdate(self):
        """
            编辑项目信息
        """
        self.payload = json.dumps({
            "echoMap": {
                "province": "北京市",
                "city": "北京市",
                "region": "丰台区"
            },
            "id": "461",
            "bomProjectId": "1638840413895172096",
            "contractNo": "",
            "contractBelong": "",
            "name": "交付0323",
            "projectType": 1,
            "abbreviation": "交付0323",
            "province": 1,
            "city": 2,
            "region": 6,
            "addressDetail": "",
            "note": "",
            "contactPerson": "",
            "contactPhone": "",
            "salePerson": "尹卡卡",
            "salePhone": "153 1348 7958",
            "clientName": "",
            "customers": [],
            "manufacturer": "大乐装 | 数字化交付平台",
            "projectAmounts": None,
            "allocationType": 1,
            "coordinationFactory": "",
            "orgId": "",
            "logo": None,
            "allocationList": [
                {
                    "coordinationFactory": "",
                    "orgId": "",
                    "details": [
                        {}
                    ]
                }
            ],
            "createMark": True,
            "orderType": "大乐装（东莞）建筑科技有限公司",
            "status": 1,
            "address": [
                1,
                2,
                6
            ],
            "amounts": []
        })
        self.post("/api/report/project/update", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)