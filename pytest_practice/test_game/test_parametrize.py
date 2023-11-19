import pytest


# 多参数场景
# 参数2 ： 代表传入的数据信息，如果只有一个形参的话，
# 那么直接通过列表传入参数化的数据 []
# 如果有多个形参, 那么就需要传入多组数据 [[]]

@pytest.mark.parametrize("name, volume", [("AD", 100), ("ez", 200), ("sam", 300)])
def test_create_hero_success(name, volume):
    """

    :param name:
    :param volume:
    :return:
    """
    print(f"英雄{name}的血量为{volume}")