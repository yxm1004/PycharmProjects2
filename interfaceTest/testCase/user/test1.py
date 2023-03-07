# -*- coding: utf-8 -*-
import requests
import unittest

from ReadConfigini import read_config_file


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.config = read_config_file('config.ini')

    def test_get_user(self):
        url = self.config['HTTP']['baseurl']
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_user2222222(self):
        url = self.config['HTTP']['baseurl']
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass


# if __name__ == '__main__':
#     unittest.main()
