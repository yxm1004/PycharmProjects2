import requests
import json

from seldom.request import HttpRequest, check_response

from common.loginApi import Common


class BatchSave(HttpRequest):


    """
    获取参数
    pm.globals.set("code",jsonData.data[0].code)
    pm.globals.set("id",jsonData.data[0].id)
    pm.globals.set("createdBy",jsonData.data[0].createdBy)
    pm.globals.set("updatedBy",jsonData.data[0].updatedBy)
    """
    def get_pm(self):
        data=self.bathSave()
        return data[0]
        # data=self.bathSave()
        # code=data[0].get("code")
        # id=data[0].get("id")
        # createdBy=data[0].get("createdBy")
        # updatedBy=data[0].get("updatedBy")
        #
        # print("22222222222222222222"+data[0].get("code"))

    @check_response(
        describe="获取参数data",
        status_code=200,
        ret="data",
        check={"msg": "成功"},
        debug=True
    )
    def bathSave(self):

        self.c = Common()
        self.header = self.c.SetHeader()

        url = "https://jf-api-test-x1ksp5.dalezhuang.com/api/report/materialPleaseOrder/batchSave"

        payload = json.dumps([
          {
            "projectId": "1068",
            "projectName": "大乐装0731号",
            "building": "6",
            "floor": 1,
            "floorLevels": 1,
            "requiredTime": "2023-07-31"
          }
        ])
        r = self.post(url, headers=self.header, data=payload)
        return r

if __name__ == '__main__':
    b=BatchSave()
    d=b.get_pm()
    print(d.get("code"))