"""
seldom confrun.py hooks function
"""

def start_run():
    """
    Test the hook function before running
    """
    ...


def end_run():
    """
    Test the hook function after running
    """
    ...


# def browser():
#     """
#     Web UI test:
#     browser: gc(google chrome)/ff(firefox)/edge/ie/safari
#     """
#     return "gc"


def base_url():
    """
    http test
    api base url需要则是的地址
    """
    return "https://jf-api-test-x1ksp5.dalezhuang.com"


# def app_info():
#     """
#     app UI test
#     appium app config
#     """
#     desired_caps = {
#         'deviceName': 'JEF_AN20',
#         'automationName': 'UiAutomator2',
#         'platformName': 'Android',
#         'platformVersion': '10.0',
#         'appPackage': 'com.meizu.flyme.flymebbs',
#         'appActivity': '.ui.LoadingActivity',
#         'noReset': True,
#     }
#     return desired_caps


# def app_server():
#     """
#     app UI test
#     appium server/desktop address
#     """
#     return "http://127.0.0.1:4723"

def debug():
    """
    debug mod
    debug模式不输出测试报告
    """
    return False


def rerun():
    """
    error/failure rerun times
    """
    return 0


def report():
    """
    setting report path
    Used:
    return "d://mypro/result.html"
    return "d://mypro/result.xml"
    """
    return None


def timeout():
    """
    setting timeout
    """
    return 10


def title():
    """
    setting report title
    """
    return "交付平台接口测试报告"


def tester():
    """
    setting report tester
    """
    return "yinxm"


def description():
    """
    setting report description
    """
    return ["windows", "jenkins"]


def language():
    """
    setting report language
    return "en"
    return "zh-CN" 测试报告语言，英文或中文
    """
    return "zh-CN"


def whitelist():
    """test label white list"""
    return []


def blacklist():
    """test label black list"""
    return []