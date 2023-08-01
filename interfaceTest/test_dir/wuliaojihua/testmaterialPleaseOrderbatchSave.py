import json
import seldom
from common.loginApi import Common
class testmaterialPleaseOrderbatchSave(seldom.TestCase):
    def start(self):
        #调用登录公共方法构建报文头
        self.c = Common()
        self.header = self.c.SetHeader()
    def test_post_materialPleaseOrderbatchSave(self):
        """
            批量新增物料请购单
        """
        self.payload = json.dumps([
            {
                "projectId": "1068",
                "projectName": "大乐装0731号",
                "building": "6",
                "floor": 1,
                "floorLevels": 1,
                "requiredTime": "2023-07-31"
            }
        ])
        self.post("/api/report/materialPleaseOrder/batchSave", data=self.payload, headers=self.header)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)
