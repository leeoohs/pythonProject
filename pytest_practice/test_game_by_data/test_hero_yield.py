import pytest

from pythonProject.pytest_practice.game.hero_management import HeroManagement


# 测试类与测试类的定义
class TestHero:
    # **所有的类**执行之前进行执行
    def setup_class(self):
        print("这是一个测试类")
    # 在**每一个方法**执行之前执行
    # 在 类里面setup_method、teardown_method 与 setup、teardown 是一个含义

    def setup(self):
        # data = LoadUitls.load_yaml("volume_data.yaml")["success"]
        self.data = 1

    def test_create_hero_volume_success(self, data):
        """

        :param volume:
        :return:
        """
        hero_management = HeroManagement()
        print(f"英雄的血量为{data}")
        hero_management.create_hero("jinx", data, 20)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == data


# 测试类与测试类的定义
class TestHero2:
    # **所有的类**执行之前进行执行
    def setup_class(self):
        print("这是一个测试类")
    # 在**每一个方法**执行之前执行
    # 在 类里面setup_method、teardown_method 与 setup、teardown 是一个含义

    def setup(self):
        # data = LoadUitls.load_yaml("volume_data.yaml")["success"]
        self.data = 1

    def test_create_hero_volume_success(self, data):
        """

        :param volume:
        :return:
        """
        hero_management = HeroManagement()
        print(f"英雄的血量为{data}")
        hero_management.create_hero("jinx", data, 20)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == data


# 测试类与测试类的定义
class TestHero3:
    # **所有的类**执行之前进行执行
    def setup_class(self):
        print("这是一个测试类")
    # 在**每一个方法**执行之前执行
    # 在 类里面setup_method、teardown_method 与 setup、teardown 是一个含义

    def setup(self):
        # data = LoadUitls.load_yaml("volume_data.yaml")["success"]
        self.data = 1

    def test_create_hero_volume_success(self, data):
        """

        :param volume:
        :return:
        """
        hero_management = HeroManagement()
        print(f"英雄的血量为{data}")
        hero_management.create_hero("jinx", data, 20)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == data