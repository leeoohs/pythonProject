# 在pytest 中，setup 是一个关键字
# 在 **每条** 用例执行之前执行
def setup():
    print("setup执行啦")


# 在 **每条** 用例执行之后执行
def teardown():
    print("teardown执行啦")


# 如果没有使用 pytest 方式运行，那么就会当成正常的函数执行。
def test_demo1():
    print("12312")
    # 断言： Assertion
    assert 1 == 1
    assert 1 == 2


def demo():
    return True


def test_demo2():
    print("12312")
    # 断言： Assertion
    assert 1 == 1
    # 如果断言失败了，后面的代码就不会执行了
    assert 1 in ["1", 1]
    assert demo() # 只要结果是一个布尔值，断言就成功
    # assert 1 == 2