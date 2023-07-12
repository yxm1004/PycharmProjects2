import seldom
from seldom import data


class DataDriverTest(seldom.TestCase):

    @data([
        ("First case", "seldom"),
        ("Second case", "selenium"),
        ("Third case", "unittest"),
    ])
    def test_tuple_data(self, name, keyword):
        """
        Used tuple test data
        :param name: case desc
        :param keyword: case data
        """
        print(f"test data: {keyword}")

    # @data([
    #     ["First case", "seldom"],
    #     ["Second case", "selenium"],
    #     ["Third case", "unittest"],
    # ])
    # def test_list_data(self, name, keyword):
    #     """
    #     Used list test data
    #     """
    #     print(f"test data: {keyword}")
    #
    # @data([
    #     {"scene": 'First case', 'keyword': 'seldom'},
    #     {"scene": 'Second case', 'keyword': 'selenium'},
    #     {"scene": 'Third case', 'keyword': 'unittest'},
    # ])
    # def test_dict_data(self, scene, keyword):
    #     """
    #     used dict test data
    #     """
    #     print(f"case desc: {scene}")
    #     print(f"test data: {keyword}")
if __name__ == '__main__':
    print('11111111')
    seldom.main()