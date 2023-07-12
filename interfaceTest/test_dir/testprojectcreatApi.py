import time
import unittest

import requests
import seldom

class testprojectcreat(seldom.TestCase):

    def test_post_projectcreat(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.post("/api/report/project/create", params=payload)
        self.assertEqual(r.status_code, 200)
if __name__ == '__main__':
    unittest.main()