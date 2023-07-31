import json
import seldom
from common.loginApi import Common
class testmaterialPleaseOrderbatchUpdate(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_materialPleaseOrderbatchUpdate(self):
        """
            批量编辑物料请购单
        """
        self.payload = json.dumps([
            {
                "building": "6",
                "code": "PR20230731170456",
                "createTime": "2023-03-10",
                "createdBy": 1630382479472853000,
                "floor": "3",
                "floorLevels": "1",
                "id": 1685939593490202600,
                "projectId": 434,
                "requiredTime": "2023-03-10",
                "updateTime": "2023-03-10",
                "updatedBy": 1630382479472853000
            }
        ])
        self.post("/api/report/materialPleaseOrder/batchUpdate", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)