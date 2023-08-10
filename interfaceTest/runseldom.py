import seldom
from XTestRunner import Weinxin


class YouTest:
    """执行test_dir下所有test文件并输出测试报告"""
    if __name__ == '__main__':
            # 指定运行其他目录&文件
            # 运行当前文件中的用例
            seldom.main(path='./test_dir',
                        base_url='https://jf-api-test-x1ksp5.dalezhuang.com',
                        title="大乐装测试报告",
                        tester="yinxm")  # 默认运行当前文件中所有用例
            weixin = Weinxin(
                # access_token="bdb12697-5c4a-4cb9-addb-49b7689f660a",  # 2817d6fc-56ad-4fa9-928a-62222c5f729b
                access_token="2817d6fc-56ad-4fa9-928a-62222c5f729b",
                at_mobiles=[15313487958],
                is_at_all=True,
            )
            # weixin.send_text(text="\n ### 测试发送消息")
            weixin.send_markdown(append="\n ### 附加信息")