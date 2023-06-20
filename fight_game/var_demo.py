class VarDemo:
    # 类变量：在类内，方法外，前面没有self
    var1 = "类变量"

    def __init__(self):
        # 实例变量：在方法内，且前面有self
        self.name = "实例变量"
        # 局部变量：在方法内，且没有self，只在方法内可用
        age = "局部变量"


# 通过类获取变量
print(VarDemo.var1)  # 类变量可用
print(VarDemo.name)  # 实例变量不可用
print(VarDemo.age)  # 局部变量不可用

var_demo = VarDemo()
print(var_demo.var1)  # 类变量可用
print(var_demo.name)  # 实例变量可用
print(var_demo.age)  # 局部变量不可用