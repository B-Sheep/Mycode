#(2)reduce
#语法：reduce(function,sequence [,initial])
#功能：给定序列，依次取出1个元素作为参数，与前一次函数结果进行运算。最后返回运算结果


#将列表中每个元素相乘
# 

# obj = [1,2,3,4]
# def multi(x,y):
#     return x*y

# res = reduce(multi,obj)
# print(res,type(res))



#应用案例

# def getRes(x):
#     if x == 1:
#         return 1
#     return getRes(x-1)*x+1
# print(getRes)

# from functools import reduce
# lst = [1,2,3,4]

# # res = reduce(lambda x,y:x*y+1,lst)

# #如果初始值不是1，怎么传递这个数值呢
# res = reduce(lambda x,y:x+y,range(1,5),100)
# print(res)



#(3)sorted
#语法：sorted(iterable,reverse=False,key=函数)
#功能：排序

#lst = [1,3,2,5,8,-2]
# lst = "helloworld"
# print(sorted(lst))

#按绝对值排序
# lst = [1,3,-2,5,8,2]
# print(sorted(lst,key=abs))


# dic = {3:"A",2:'C',-1:"B"}
# print(sorted(dic))


# lst = [20,31,47,19,15]
# res = sorted(lst,key=lambda x:x%3)
# print(res)



#sort()和sorted()的区别

# lst = [1,3,2,5,8,-2]
# lst.sort()
# print(lst)            #改变了原有的序列
# lst2 = sorted(lst)    #产生写列表
# print(lst2)
# print(lst)



#(4)filter
#语法：filter（func,iterable)
#功能：过滤数据

# lst = [1,3,2,5,8,-2]

# def getEven(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False

# print(filter(getEven,lst))

# res = filter(lambda x:True if x%2==0 else False,lst)
# # res = filter(getEven,lst)
# print(list(res))















