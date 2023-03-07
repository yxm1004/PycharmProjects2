# -*- coding: utf-8 -*-
import requests
import unittest


class APITestCase1(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://www.baidu.com"

    def test_get_user(self):
        url = self.base_url
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print("zheshiyongli")

    # def tearDown(self):
    #     pass


# if __name__ == '__main__':
#     unittest.main()
