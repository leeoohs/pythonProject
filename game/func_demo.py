# 函数的定义
# def 函数的名称(形参1， 形参2， 形参3):
def func_name(name, age):
    print(name)
    print(age)


# 函数的调用
# 函数名称(实参1， 实参2， 实参3)
# 形参和实参一定要对应
# func_name("teacherLi", "18")
# # func_name("teacherLi")
# # func_name("teacherLi", "18", "1")
#
#
# # ======================================
# # 函数的return
# def func_name(name, age):
#     print(name)
#     print(age)
#
#
# def func_name1(name, age):
#     print(name)
#     print(age)
#     return name
#
#
# # 如果没有使用return 关键字，或者return的时候没有指定值，name就都会返回None
# def func_name2(name, age):
#     print(name)
#     print(age)
#     return
#
#
# print(func_name("teacherLi", "18"))
# print("=====================")
# print(func_name1("teacherLi", "18"))
# print("=====================")
# print(func_name2("teacherLi", "18"))


# return的中止作用
def func_name3():
    a = 0
    while True:
        a = a + 1
        if a == 3:
            return a


print(func_name3())
