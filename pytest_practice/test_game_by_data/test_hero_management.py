import pytest

from pythonProject.pytest_practice.game.hero_management import HeroManagement
from pythonProject.pytest_practice.test_game_by_data.load_utits import LoadUitls


# 测试类与测试类的定义
class TestHero:
    # **所有的类**执行之前进行执行
    def setup_class(self):
        print("这是一个测试类")
    # 在**每一个方法**执行之前执行
    # 在 类里面setup_method、teardown_method 与 setup、teardown 是一个含义
    def setup_method(self):
        print("这是一个方法级别的前置处理")

    def teardown_class(self):
        print("这是后置处理teardown_class")
    # 在**每一个方法**执行之后执行
    def teardown_method(self):
        print("这是一个方法级别的后置处理teardown_method")
    # 增加英雄：输入英雄姓名、血量、和攻击力，名称为字符串，血量、攻击力为正整数，
    # 其中血量的最大值为 99，最小值为 1

    # 当血量值设定有效的场景
    @pytest.mark.parametrize("volume", LoadUitls.load_yaml("volume_data.yaml")["success"])
    def test_create_hero_volume_success(self, volume):
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

    # 当血量值设定无效的场景， 参数化传入的数据通常为[1, 2, 3, 4](1, 2, 3)
    # 当调用方法的时候。 比如load_yaml()的时候，返回值需要为列表
    @pytest.mark.parametrize("volume", LoadUitls.load_yaml("volume_data.yaml")["fail"])
    def test_create_hero_volume_fail(self, volume):
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

    def test_delete_hero(self):
        assert False

    def test_create_hero(self):
        assert False

    def test_find_hero(self):
        assert False

    def test_get_data(self):
        data = LoadUitls.load_yaml("volume_data.yaml")
        print(data)