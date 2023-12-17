import pytest


# 原始夹具
@pytest.fixture
def data():
    return [1, 2, 3]


@pytest.fixture
def data2():
    return ["a", "b", "c"]


@pytest.fixture(autouse=True)
def merge_data(data, data2):
    return data+data2


# 有些时候需要对数据进行二次定制，
# 有些时候则是要使用原始的数据信息。
@pytest.fixture
def data_plus(data):
    new_data = []
    for i in data:
        i = i+1
        new_data.append(i)
    return new_data


# 数据的形参叫什么，夹具的函数名就必须一致
def test_data(data, data2):
    print(data)
    print(data2)
    # print(merge_data)