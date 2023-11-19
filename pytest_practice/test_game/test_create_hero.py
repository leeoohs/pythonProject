# 实例化类 类名()
import allure
import pytest

from pythonProject.pytest_practice.game.hero_management import HeroManagement


# 问题： 用例冗余，成功的所有的用例步骤全部都是一样的，包括断言信息
#       不一样的地方，只有输入的数据信息
# 解决方案： 如果测试步骤与断言全部一样，只有输入的数据不一样，就可以使用《参数化》


# 装饰器的语法：@pyteat.mark.parametrize
# 装饰器，一定是写在函数定义的头上
# 反例XXXXXX
# @pytest.mark,parametrize
# def demo():
#   pass
# 反例XXXXXX
# 参数1： 有几个形参，“形参1， 形参2， 形参3”，装饰器内定义了几个形参，
# 就需要在 pytest 测试方法内添加几个形参， 名称需要保持一致
# 参数2：
@pytest.mark.parametrize("volume", [1, 2, 98, 99])
def test_create_hero_success(volume):
    """

    :param volume:
    :return:
    """
    hero_management = HeroManagement()
    print(f"英雄的血量为{volume}")
    hero_management.create_hero("jinx", volume, 20)
    res = hero_management.find_hero("jinx")
    assert res.get("name") == "jinx"
    assert res.get("volume") == volume


@pytest.mark.parametrize("volume", [0, 100], ids = ["边界值为0", "边界值为100"])
def test_create_hero_fail(volume):
    """

    :param volume:
    :return:
    """
    hero_management = HeroManagement()
    print(f"英雄的血量为{volume}")
    hero_management.create_hero("jinx", volume, 20)
    res = hero_management.find_hero("jinx")
    assert res == False


# 笛卡尔积， 使用两个装饰器分别传参
@pytest.mark.parametrize("name", ["jinx", "ez"])
@pytest.mark.parametrize("volume", [0, 100])
@allure.title("创建英雄失败的场景")
def test_create_hero_fail(name, volume):
    """

    :param volume:
    :return:
    """
    hero_management = HeroManagement()
    print(f"英雄的血量为{volume}")
    hero_management.create_hero("jinx", volume, 20)
    res = hero_management.find_hero(name)
    assert res == False