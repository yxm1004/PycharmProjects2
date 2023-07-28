import json
import seldom
from common.loginApi import Common
class testupdateMold(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_updateMold(self):
        """
            修改模具
        """
        self.payload = json.dumps({
            "echoMap": {},
            "id": "1684829462727753728",
            "createTime": "2023-07-28 15:33:41",
            "createdBy": "1630382479472852992",
            "updateTime": "2023-07-28 15:33:41",
            "updatedBy": "1630382479472852992",
            "moldNumber": "1234567899",
            "defUsefulLife": 300,
            "currentLife": 0,
            "orgId": "1514430640907354112",
            "orgName": "大乐装（惠州）建筑科技有限公司",
            "note": "备注789",
            "proofs": [
                "https://cz-filemino.dalezhuang.com/report-test/652d2d592c664b40b94e008fef851127.webp"
            ],
            "cover": "https://cz-filemino.dalezhuang.com/report-test/652d2d592c664b40b94e008fef851127.webp",
            "dummy": 0,
            "fileDTOList": None,
            "moldGroupDTOList": [
                {
                    "echoMap": {},
                    "id": "1684804358186729472",
                    "createTime": "2023-07-28 13:53:56",
                    "createdBy": "1638799875954966528",
                    "updateTime": "2023-07-28 13:53:56",
                    "updatedBy": "1638799875954966528",
                    "componentType": "2",
                    "name": "1690523634",
                    "normalHours": 12,
                    "managerUserId": "1639110090675978240",
                    "managerPhone": "15879654575",
                    "note": "",
                    "proof": None,
                    "cover": None,
                    "staticProject": "静态项目01",
                    "groupNumber": "molestie",
                    "proofs": None,
                    "fileDTOList": None
                }
            ],
            "taskComponentVOS": None,
            "deleteStatus": 0,
            "moldGroupIds": [
                "1684804358186729472"
            ]
        })
        self.post("/api/report/mold/updateMold", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
