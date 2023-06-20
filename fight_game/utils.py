# 实现一个装饰器
# 什么是装饰器？他装饰什么?通常是一个函数/方法。也可以装饰一个类
# 怎么装饰
# @装饰器
# def 被装饰的函数()
import datetime


def timer(func):  # 定义装饰器的名称(func)
    def inner(*args):  # 定义内函数()。内函数的参数为 被装饰函数的形参
        # print("这是一个装饰器")
        start_time = datetime.datetime.now()
        func(*args)
        end_time = datetime.datetime.now()
        print(f"打斗的持续时间为{end_time - start_time}")

    return inner


@timer
def demo(name):
    print(name)
    print("这是一个小demo")


@timer
def demo2(name, age, sex, weight):
    print("这是一个小demo2")


@timer
def demo3():
    print("这是一个小demo3")


# demo("哥哥")
# demo2("leo", 1, "公的", "4.5kg")