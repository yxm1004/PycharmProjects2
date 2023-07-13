import seldom


class TestCase(seldom.TestCase):

    def start(self):
        print("一条测试用例开始")

    def end(self):
        print("一条测试结果")

    def test_search_seldom(self):
        self.open("https://www.baidu.com")
        self.type_enter(id_="kw", text="seldom")

    def test_search_poium(self):
        self.open("https://www.baidu.com")
        self.type_enter(id_="kw", text="poium")