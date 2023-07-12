import seldom
from seldom import data_class


@data_class([
    {"username": "user_1", "password": "abc123"},
    {"username": "user_2", "password": "abc456"},
])
class DDTTest(seldom.TestCase):

    def test_data_func(self):
        """ data driver case """
        print("username->", self.username)
        print("password->", self.password)


if __name__ == '__main__':
    seldom.main(debug=True)