#5.逻辑运算符

#and , 与 ，表示“并且”
#or ， 或 ，表示“或者”
#not ，非 ，表示“不是”

#and， 所有条件都成立才可以
# age = 20
# vision = 5.0
# if age>= 20 and vision>=5.0:
#     print("可以开公交车")
# else:
#     print("不可以开公交车")


# #or， 满足一个条件就成立
# month = 5
# if month == 3 or month == 4 or month ==5:
#     print("春季")
# else:
#     print("不是春季")


# #not
# drink = 1
# if not drink:
#     print("可以开车")
# else:
#     print("不可以开车")


# # 短路原则
# # and, 如果前面为False，后面不计算，只要有一个不成立，全都不成立。
# # or， 如果前面为True，后面不计算，只要有一个成立，全都成立


# print(bool(10 and 20))
# print(10 and 20)
# print(0 and 20)
# #---------------
# print("----------------------")
# print(10 or 20)
# print(0 or 20)


# #优先级
# #not 高于 and 高于 or
# print(1>2 or 4>3 and not 6<5)

# print((1>2) or (4>3 and (not 6<5)))




# #6.成员运算符

# str = "IT私塾"
# print("IT" in str)
# print("it" in str)
# \


# #7.身份运算符

# #id()函数返回对象的唯一标识符，标识符是一个整数。
# #        cpython中id() 函数用于获取对象的内存地址。

# a = "IT私塾"
# print(id(a))

#is  两个标识符是否为同一个对象
#is not  两个标识符不是同一个对像

#Python的整数缓存（了解）
#1. 交互模式下   [-5,256]
#2.pycharm或者vscode或者文件中 [-∞，∞]

a = 10000
b = 10000
print(a == b)
print(a is b)

print(a, id(a))
print(b, id(b))







