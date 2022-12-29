#生成器
#本质就是迭代器

#作用：自定义迭代器数据生成过程

#定义生成器有两种方式：
#(1)生成器函数
#(2)生成器表达式

# def getNum():
#     print("返回1")
#     #return 1
#     yield 1

# res = getNum()           #返回了生成器对象：generator
# print(res)

# from collections.abc import Iterator
# print(isinstance(res,Iterator))

# print("运行了next：",next(res))
# print("运行了next：",next(res))


#(1)yield 产出，相当于返回每次迭代的结果值

# def getNum():
#     print("返回1")
#     #return 1
#     yield 1

#     print("返回2")
#     #return 1
#     yield 2

#     print("返回3")
#     #return 1
#     yield 3

#     print("返回4")
#     #return 1
#     yield 4


# res = getNum()           #返回了生成器对象：generator
# print("运行了next：",next(res))
# print("运行了next：",next(res))
# print("运行了next：",next(res))
# print("运行了next：",next(res))


# for i in res:
#     print("运行了next：",i)



# import random

# def getNum(length):
#     for i in range(length):
#         yield f"当前的数值为：{random.randint(1,10)}"

# num = getNum(10)
# for i in range(10):
#     print(next(num))
# print("-"*30)
# num = getNum(5)
# for i in range(5):
#     print(next(num))


#(2)send
    
# def getResult(x):
#     print("接收到x：",x)
#     y = yield x*x

#     print("接收到y：",y)
#     z = yield y**3

#     print("接收到y：",y)
#     yield z +1000

# res = getResult(2)
# # print("第一次访问:",next(res))

# print("第一次访问:",res.send(None))
# print("第二次访问:",res.send(10))

# print("第三次访问:",res.send(50))



#得到指定数字的平方
# def getSquare(num):
#     x = num
#     while True:
#         x = yield x**2
        
# gs = getSquare(1)
# # print(next(gs))
# print(gs.send(None))
# print(gs.send(10))
# print(gs.send(50))



#(3)yield from


# def getNum():
#     t = [1,2,3,4]
#     yield from t

# res = getNum()
# for i in res:
#     print(i)


#2.生成器表达式        （联系推导式）

#只有一点不同：不是[]，而是()

g = (i*2 for i in range(5))
for i in g:
    print(i)


