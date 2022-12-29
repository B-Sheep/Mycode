#函数的定义

# def printInfo():
#     print("-------------")
#     print("人生苦短,我学python")
#     print("-------------")


# #函数的调用
# printInfo()


# #带参数的函数
# #在“函数定义”的时候，a,b称为“形式参数”。
# def addNum(a,b):
#     c = a+b
#     print(c)


# #在“函数调用”的时候，11和22称为“实际参数”
# addNum(11,22)



#带返回值的函数
 
# def add2Num(a,b):
#     return a + b

# result = add2Num(110,20)          #函数执行完后，函数调用的地方结果为函数中return的运算结果

# print(result)
#结果：return"返回"了结果：return 结束了函数的执行


# def subtraction(a,b):
#     # if a < b:
#     #     return b - a 
#     # else:
#     #     return a-b
#     if a<b:
#         print("a<b")
#         return b-a
#     print("a>=b")
#     return a-b



# print(subtraction(-3,5))
#print(subtraction(5,-3))



#函数的分类
#1.内置函数
#2.标准库函数
#3.第三方库函数
#4.用户自定义函数



# #函数（调用）
# def add2Num(a,b):
#     return a+b

# def add3Num(a,b,c):
#     #sum = a+b+c
#     return add2Num(add2Num(a,b),c)

# print(add3Num(10,20,30))



#打印一条线
# def line():
#     print("-"*30)


#根据用户输入的数字，打印相应数量的线条
# def Line(num):
#     i = 0
#     while i < num:
#         line()
#         i += 1

# num = float(input("请输入数字"))
# Line(num)



#求三个数的和
def Sum(a,b,c):
    return a+b+c
    

#求三个数的和的平均值
def average3Number(a,b,c):
    return Sum(a,b,c)/3

result = average3Number(3,4,5)
print(result)



















