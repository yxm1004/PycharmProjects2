import unittest
#接口和测试case分离
from FileUploader import FileUploader


class TestFileUploader(unittest.TestCase):
    def setUp(self):
        # 初始化测试环境
        self.fileuploader = FileUploader()
        self.filename = "test.txt"
        self.content = "This is a test file."

    def test_upload(self):
        # 测试文件上传接口
        response = self.fileuploader.upload(self.filename, self.content)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()["success"] == True)

    def test_confirm(self):
        # 测试确认上传接口
        self.fileuploader.upload(self.filename, self.content)
        response = self.fileuploader.confirm(self.filename)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()["success"] == True)


if __name__ == '__main__':
    unittest.main()
