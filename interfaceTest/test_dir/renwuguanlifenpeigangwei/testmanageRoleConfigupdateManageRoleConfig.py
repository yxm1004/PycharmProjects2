import json
import seldom
from common.loginApi import Common
class testmanageRoleConfigupdateManageRoleConfig(seldom.TestCase):
    def start(self):
        # 调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_manageRoleConfigupdateManageRoleConfig(self):
        """
           修改任务管理岗位配置
        """
        self.payload = json.dumps({
            "dealRoleList": [
                {
                    "dealRoleList": [
                        {
                            "echoMap": {
                                "roleId": "超级管理员"
                            },
                            "id": "1701782551871356928",
                            "createTime": None,
                            "createdBy": None,
                            "updateTime": None,
                            "updatedBy": None,
                            "limitTimeConfigId": "1693809112615223296",
                            "firstType": 1,
                            "type": 10,
                            "roleType": 1,
                            "roleId": "1527113361416781824",
                            "limitTime": None
                        },
                        {
                            "echoMap": {
                                "roleId": "管理员"
                            },
                            "id": "1701782551871356929",
                            "createTime": None,
                            "createdBy": None,
                            "updateTime": None,
                            "updatedBy": None,
                            "limitTimeConfigId": "1693809112615223296",
                            "firstType": 1,
                            "type": 10,
                            "roleType": 1,
                            "roleId": "1562382153361129472",
                            "limitTime": None
                        }
                    ],
                    "type": "10",
                    "id": "1693809112615223296",
                    "limitTime": "9"
                },
                {
                    "dealRoleList": [
                        {
                            "echoMap": {
                                "roleId": "超级管理员"
                            },
                            "id": "1701782551871356933",
                            "createTime": None,
                            "createdBy": None,
                            "updateTime": None,
                            "updatedBy": None,
                            "limitTimeConfigId": "1693557959948238848",
                            "firstType": 1,
                            "type": 11,
                            "roleType": 1,
                            "roleId": "1527113361416781824",
                            "limitTime": None
                        },
                        {
                            "echoMap": {
                                "roleId": "管理员"
                            },
                            "id": "1701782551871356934",
                            "createTime": None,
                            "createdBy": None,
                            "updateTime": None,
                            "updatedBy": None,
                            "limitTimeConfigId": "1693557959948238848",
                            "firstType": 1,
                            "type": 11,
                            "roleType": 1,
                            "roleId": "1562382153361129472",
                            "limitTime": None
                        }
                    ],
                    "type": "11",
                    "id": "1693557959948238848",
                    "limitTime": 5
                },
                {
                    "dealRoleList": [
                        {
                            "echoMap": {
                                "roleId": "超级管理员"
                            },
                            "id": "1701782551871356935",
                            "createTime": None,
                            "createdBy": None,
                            "updateTime": None,
                            "updatedBy": None,
                            "limitTimeConfigId": "1693864152365268992",
                            "firstType": 1,
                            "type": 12,
                            "roleType": 1,
                            "roleId": "1527113361416781824",
                            "limitTime": None
                        }
                    ],
                    "type": "12",
                    "id": "1693864152365268992",
                    "limitTime": 24
                },
                {
                    "dealRoleList": [
                        {
                            "echoMap": {
                                "roleId": "管理员"
                            },
                            "id": "1701782551871356936",
                            "createTime": None,
                            "createdBy": None,
                            "updateTime": None,
                            "updatedBy": None,
                            "limitTimeConfigId": "1693864152369463296",
                            "firstType": 1,
                            "type": 18,
                            "roleType": 1,
                            "roleId": "1562382153361129472",
                            "limitTime": None
                        },
                        {
                            "echoMap": {
                                "roleId": "超级管理员"
                            },
                            "id": "1701782551871356937",
                            "createTime": None,
                            "createdBy": None,
                            "updateTime": None,
                            "updatedBy": None,
                            "limitTimeConfigId": "1693864152369463296",
                            "firstType": 1,
                            "type": 18,
                            "roleType": 1,
                            "roleId": "1527113361416781824",
                            "limitTime": None
                        }
                    ],
                    "type": "18",
                    "id": "1693864152369463296",
                    "limitTime": 24
                }
            ],
            "firstType": 1,
            "manageRoleList": [
                {
                    "roleId": "1527113361416781824",
                    "roleType": 2
                },
                {
                    "roleId": "1562382153361129472",
                    "roleType": 2
                }
            ]
        })
        self.post("/api/report/manageRoleConfig/updateManageRoleConfig", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
