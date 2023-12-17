import pytest


@pytest.fixture
def data():
    """
    yield 之前为前置处理
    之后为后置处理
    yield 后面跟的数据代表夹具的返回值，可以直接给测试用例使用。
    :return:
    """
    print("这是用例执之前的操作")
    # 类似于 return
    yield 1
    # 与return不同， 还会继续执行
    print("这是用例执行之后的操作")


def test_data(data):
    print(data)
    print("这是我执行的测试数据信息")
