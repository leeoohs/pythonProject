# 不定长参数
# 定义参数的时候 *args
# 调用函数的时候就可以传多个参数了

def demo(name, age, *args):
    print(f"{name}年龄为{age}")
    print(args)


demo("teacherLi", 29, 11, 181, 7)