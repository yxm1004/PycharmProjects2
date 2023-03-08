import unittest
from configparser import ConfigParser


class TestAddNumbers(unittest.TestCase):
    def setUp(self):
        self.config = ConfigParser()
        self.config.read('test_data.cfg')

    def test_add_numbers(self):
        test_cases = self.config.items('test_data')
        for name, values in test_cases:
            x, y, expected_result = [int(x) for x in values.split(',')]

if __name__ == '__main__':
    unittest.main()
