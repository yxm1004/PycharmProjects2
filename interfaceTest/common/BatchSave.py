import requests
import json

from seldom.request import HttpRequest, check_response


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
        headers = {
          'Authorization': 'Basic Y2xvdWRmYWN0b3J5X3dlYjpjbG91ZGZhY3Rvcnlfd2ViX3NlY3JldA==',
          'tenant': 'ZGdnYw==',
          'token': 'Bearer eyJ0eXAiOiJKc29uV2ViVG9rZW4iLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi5bC55pmT5qKFIiwidG9rZW5fdHlwZSI6InRva2VuIiwidXNlcmlkIjoiMTYzMDM4MjQ3OTQ3Mjg1Mjk5MiIsImFjY291bnQiOiIxNTMxMzQ4Nzk1OCIsImlhdCI6MTY5MDg1MjMwMiwibmJmIjoxNjkwODUyMzAyLCJleHAiOjE2OTA4ODExMDJ9._A7Q1zgv-oM5ue_opb0JJlPLV1v_eHQmlX6HSyiryTI',
          'Content-Type': 'application/json'
        }

        r = self.post(url, headers=headers, data=payload)
        return r

if __name__ == '__main__':
    b=BatchSave()
    d=b.get_pm()
    print(d.get("code"))