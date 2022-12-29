#1.高阶函数
#把函数当成参数传递的函数
# def printInfo():
#     print("info....")

# #高阶函数
# def runFunc(func):
#     func()

# runFunc(printInfo)


#2.常用的高阶函数
#(1)map
#语法：map(func,iterable,.......)
#功能：把可迭代对象中的数据逐一拿出来，
#经过函数处理之后，将结果放到map中并返回一个迭代器对象。



#字符串列表转化为整数列表
# l1 = ["1","2","3","4"]
# res = map(int,l1)
# print(res)
# print(list(res))

# for item in res:
#     print(item)


# from collections.abc import Iterable,Iterator
# print(isinstance(res,Iterable))
# print(isinstance(res,Iterator))


#自定义函数

#求列表中字符串所表达数值的平方
# l1 = ["1","2","3","4"]


# def getSquare(x):
#     return int(x)**2

# res = map(getSquare,l1)
# print("自定义函数：",list(res))


# #使用lambda表达式
# res = map(lambda x:int(x)**2,l1)
# print("lambda函数：",list(res))



#多个可迭代对象，作为参数
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]

# res = map(lambda x,y:x+y,l1,l2)
# print(list(res))



#应用案例
# dic = {"北京":"京","上海":"泸","广东":"粤","四川":"川"}

# #第一种实现方法
# res = {}
# for a,b in dic.items():
#     res[b] = a
# print(res)


#第二种
# dic = {"北京":"京","上海":"泸","广东":"粤","四川":"川"}
# # def change(item):
# #     return(item[1],item[0])

# # res = map(change,dic.items())

# res = map(lambda item:(item[1],item[0]),dic.items())
# print(dict(res))












































