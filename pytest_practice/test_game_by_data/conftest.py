# pytest 用来管理公共方法、公共配置的文件
# 1. 公共的fixture
# 2. hook函数的定制
import pytest


# 通过scope参数灵活控制夹具的使用具体是类级别或者其他级别
@pytest.fixture(scope="function")
def data():
    print("测试之前操作的内容")
    yield 1
    print("测试之后操作的内容")


# 创建conftest.py 文件 ，将下面内容添加进去，运行脚本
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name=i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid=i.nodeid.encode("utf-8").decode("unicode_escape")
