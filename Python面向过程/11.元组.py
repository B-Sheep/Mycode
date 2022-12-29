# tup1 = ()    #创建空的元组
# print(tup1,type(tup1))   

# tup1 = (50)    #<class,'int'>   
# tup1 = (50,)   #<class,'tuple'>     当元组中只有一个元素时，要再加上 ','才可以识别出是元组


# tup1 = (50,60,70,80.0,"abc",True,50)
# print(tup1,type(tup1))

# tup1 = 50,60,70          #小括号可以省略（了解）
# tup1 = 50,               #建议加上括号，以避免和数据混淆
# print(tup1,type(tup1))



#增（连接）
# tup1 = (12,34,56)
# tup2 = ("abc","def")
# # tup1[0] = 1
# print(tup1[0])
# tup = tup1 + tup2
# print(tup,type(tup))


# #删（删除的是元组对象，而不是元素)
# tup1 = (12,34,56)
# print(tup1)
# del tup1 
# print("删除后：")
# print(tup1)


#改（不能改）
# tup1 = (12,34,56)
# tup1[0] = 1
# print(tup1[0])    #报错

# mylist = ['A','B']
# tup1 = (10,20,30,mylist)
# print(tup1)
# tup1[-1].append("C")
# print(tup1)


#查
#切片
# tup1 = ("abc","def",2020,2030,333,444,555,666)
# print(tup1[0])
# print(tup1[-1])     #访问最后一个元素
# print(tup1[1:5])    #左闭右开，进行切片

#tup = (1,2,3,4,5,6,7,3,3)
# for i in tup:
#     print(i)


# #包含 in,not in
# if 3 in tup:
#     print("True")
# else:
#     print("False")


# #计数 count
# print(tup.count(3))


#最大/最小/求和/个数    max、min、sum、len
# print("元组中最大的元素：",max(tup))
# print("元组中最小的元素：",min(tup))
# print("元组中各元素的和：",sum(tup))
# print("元组中元素的个数：",len(tup))


#强制类型转换 tuple()
#字符串
# s = "IT私塾"
# tup = tuple(s)
# print(tup,type(tup))   #('I','T','私','塾')


# #列表
# list1 = ["a","b","c"]
# tup = tuple(list1)
# print(tup,type(tup))


#生成器对象（了解）
# s = (x*2 for x in range(5))
# print(tuple(s))

