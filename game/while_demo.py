

# while判断条件
#     如果为真，则一直执行代码块内的内容
#     如果为假，则不会执行代码块里面的内容
while True:
    # 需要被重复执行的代码加一个缩进
    print("京东防控")
    # 问题： 死循环。给出中止条件
    break

count = 0
while count < 5:
    # print(count)
    # 自增
    count = count + 1
    if count == 1:
        # 跳过 count = 1 的循环
        continue
    print(count)
