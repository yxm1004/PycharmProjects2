import seldom


class YouTest:
    """执行test_dir下所有test文件并输出测试报告"""
    if __name__ == '__main__':
            # 指定运行其他目录&文件
            print('222222222222')
            # 运行当前文件中的用例
            seldom.main(path='./test_dir')  # 默认运行当前文件中所有用例