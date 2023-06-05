"""

"""
# 定义一个列表
students = []
print(students)
# 列表的追加
students.append("决定书")
print(students)
students.append("决定书2")
students.append("决定书3")
print(students)

# for 临时变量 in 列表
for i in students:
    print(i)
# []计算机所有的计算方式都是从0开始
# 删除操作，要求传入列表的索引
# students.pop(0)
# 删除操作，可以传入列表的具体值
students.remove("决定书2")
print(students)