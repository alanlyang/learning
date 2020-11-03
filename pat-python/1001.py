# 处理输入，空格分割，转化为int
a, b = map(int, input().split(" "))
# 调用format方法，自动根据format_spec来进行格式化
print(format(a+b, ","))
# 也可以写成 print("{:,}".format(a+b))