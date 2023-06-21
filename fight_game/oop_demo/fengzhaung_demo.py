class Account:

    # 普通属性
    bank = "BOC"
    # 内部属性
    _username = "Hogwarts"
    # 私有属性
    __password = "888"


# 通过类名访问类属性
print(Account.bank)  # 将会打印 BOC
print(Account._username)  # 使用 类.的方法无法自动提示，但可以打印 Hogwarts
print(Account.__password)  # 将会引发 AttributeError

print(Account.__dict__)

# 实例化
obj = Account()

# 实例访问类属性
print(obj.bank)  # 将会打印 BOC
print(obj._username)  # 将会打印 Hogwarts
print(obj.__username)  # 将会引发AttributeError