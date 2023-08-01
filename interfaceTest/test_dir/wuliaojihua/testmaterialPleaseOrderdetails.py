import json
import seldom

from common.BatchSave import BatchSave
from common.loginApi import Common
class testmaterialPleaseOrderdetails(seldom.TestCase):
    @classmethod
    def start_class(self):

        self.b = BatchSave()
        data = self.b.get_pm()
        self.code = data.get("code")
        self.id = data.get("id")
        self.createdBy = data.get("createdBy")
        self.updatedBy = data.get("updatedBy")

        # 调用登录公共方法构建报文头
        self.c = Common()
        self.SetFormHeader = self.c.SetFormHeader()


    def test001_get_materialPleaseOrderdetails(self):
        """
            物料请购单详情
        """
        data = {"code":self.code}
        print(data)
        self.get("/api/report/materialPleaseOrder/details", params=data, headers=self.SetFormHeader)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])
    def test002_post_OrderbatchUpdate(self):
        """
            批量编辑物料请购单
        """
        self.payload = json.dumps([
            {
                "building": "6",
                "code": self.code,
                "createTime": "2023-08-01",
                "createdBy": self.createdBy,
                "floor": "5",
                "floorLevels": "2",
                "id": self.id,
                "projectId": 1068,
                "requiredTime": "2023-08-01",
                "updateTime": "2023-08-01",
                "updatedBy": self.updatedBy
            }
        ])
        self.SetFormHeader["Content-Type"] = 'application/json'
        header = self.SetFormHeader
        self.post("/api/report/materialPleaseOrder/batchUpdate", data=self.payload, headers=self.SetFormHeader)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])
    def test003_delete_OrderdeleteOrder(self):
        """
            删除物料请购单
        """
        data = {"code":self.code}
        self.delete("/api/report/materialPleaseOrder/deleteOrder", params=data, headers=self.SetFormHeader)
        self.assertStatusCode(200)
        assert_data = "成功"  # 断言成功
        # print("test-----------------"+self.response["msg"])
        # 取返回msg值断言
        self.assertJSON(assert_data, self.response["msg"])
        self.assertJSON(True, self.response["isSuccess"])


if __name__ == '__main__':
    seldom.main(debug=True)

