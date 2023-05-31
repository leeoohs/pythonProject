"""

"""

# 创建

hero = {"key": "value"}
jinx = {"name": "jinx",
        "power": 100}
# 变量名["key"] -> 返回对应的value
# print(jinx["name1"])
# 如果字典没有这个元素，那么就会直接添加
jinx["volum"] = 200
print(jinx)
# 如果字典有这个元素，则会修改对应的值
jinx["power"] = 200
print(jinx)

# KeyError: 'name1'，为了解抛异常的问题
print(jinx.get("name1", "不存在"))
print(jinx.get("name"))