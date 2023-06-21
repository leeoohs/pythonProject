class Cat:
    color = "大橘为重"

    def run(self):
        print("猫咪在奔跑")


# 继承
# 1.子类能够使用或者访问父类的所有属性与方法
# 2.如果子类的属性、方法和父类同名的话，那么会使用子类的属性
# 如果同名的情况下，子类还想调用父类的方法，如何使用？
# super()此时的super 代指的就是 父类 super()代指的为父类()
# class 子类（父类）
class OrangeCat(Cat):
    color = "orange"

    def run(self):
        # super().run() 等同于Cat().run
        print(super().color)
        print("橘猫在奔跑")


daxm = OrangeCat()
print(daxm.color)
daxm.run()

