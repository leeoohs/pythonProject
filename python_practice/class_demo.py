"""
类的定义
PEP8：规范，类名首字母大写
"""
class Animal:
    # 类 属性：静态的事务
    color = "blue"

    # 构造方法 __init___
    # 构造方法支持传参
    def __init__(self, name):
        # self 指代实例本身
        self.name = name
        print("这是构造函数")
    # 方法：动态的行为
    # 方法名：def 单词_单词()
    # 变量名：小写单词

    def run(self):
        print("动物在奔跑")
        a = self
        print(a)


# ==================
# 实例化一个类
# 实例对象 = 类名()
# 如果构造方法右参数的话，需要在类实例化的时候传递
animal1 = Animal(1)
animal2 = Animal(2)
animal3 = Animal(3)
# 获取类属性：实例名称.类属性
print(animal1.color)
# 调用类方法：实例名称.方法名
animal1.run()
# =====================类调用
# 调用类方法：实例名称.方法名
print(Animal.color)
# 调用类的方法
Animal("sam").run()


# 实例对象 = 类()
# 实例对象.类属性
# 实例对象.实例属性
# 实例对象.实例方法()


# 类
# 类.类属性
# 类.实例属性 XXX 不支持
# 类.实例方法() XXX 不支持