#1.定义函数  moreThan(num)，判断输入的数字是否大于1500\
#，打印输出"大于1500"或"不大于1500"
# def moreThan(num):
#     if num>1500:
#         print("大于15000")
#     elif num<1500:
#         print("小于1500")

# moreThan(1501)



#2.定义函数：max(x, y)，返回两个整数的输入的最大值
# def max1(x,y):
#     if x>y:
#         return x
#     elif x<y:
#         return y

# a = max(5,7)
# print(a)



#3.定义函数，max2(x,y,z)，返回求三个整数的最大值
# def max2(x,y,z):
#     if x >y and x>z:
#         return x
#     elif y>z and y>x:
#         return y
#     elif z>y and z>x:
#         return z
# a = max2(5,6,-4)
# print(a)

#函数的复用           与以写过的函数联系 以简化代码
# def max2(x,y,z):
#     temp = max1(x,y)
#     return max1(temp,z)

# print(max2(5,8,9))



#4.定义函数 generateNum( ) 返回从0~9的十个数字中随机取出4个不重复的数字组成一个字符串
# import random
# def generateNum():
#     a = []
    
#     while True:
#         if len(a)==4:
#             break
#         else:           
#             b = str(random.randint(0,9))
#             if b in a:
#                 continue
#             else:
#                 a.append(b)   
#     print("".join(a))

# generateNum()



# 5.定义函数：taxRate(income)  ，根据收入的不同，显示输出不同的税率和税金。

# > 个人所得税采用速算扣除数法计算超额累进税率的所得税时的计税公式是：
# >
# > 应纳税额=应纳税所得额×适用税率-速算扣除数
# >
# > | 个人所得税                      | 税率 | 速算扣除数 |
# > | ------------------------------- | ---- | ---------- |
# > | 个税所得额<=5000                | 0    | 0          |
# > | 超过5000，个税区间在0-3000      | 3%   | 0          |
# > | 超过5000，个税区间在3000-12000  | 10%  | 210        |
# > | 超过5000，个税区间在12000-25000 | 20%  | 1410       |
# > | 超过5000，个税区间在25000-35000 | 25%  | 2660       |
# > | 超过5000，个税区间在35000-55000 | 30%  | 4410       |
# > | 超过5000，个税区间在55000-80000 | 35%  | 7160       |
# > | 超过5000，个税区间在80000以上   | 45%  | 15160      |


# def taxRate(income):
#     if income<=5000:
#         return 0
#     elif income<=8000:
#         return (income-5000)*0.03
#     elif income<=17000:
#         return (income-5000)*0.1-210
#     elif income<=30000:
#         return (income-5000)*0.2-1410
#     elif income<=40000:
#         return (income-5000)*0.25-2660
#     elif income<=60000:
#             return (income-5000)*0.25-4410
#     elif income<=85000:
#         return (income-5000)*0.3-7160
#     elif income>85000:
#         return (income-5000)*0.45-15160

# print(taxRate(100000))


#6.定义函数 getLength，打印用户传入的容器类型数据长度
# def getLength():
#     pass

#跳过 看不懂



#7.定义函数 getType，参数为容器类型数据,打印所有奇数位索引对应的元素


# def getType():
#    pass



#8.定义函数 connect ,接收一个参数(可迭代性数据),用 _ 让元素相连成字符串,打印出来
# def connect(*list1):
#     return "-".join(str(j) for j in list(list1))

# # list3 = "afeaggca"
# list2=[1,2,3,4,5,]
# print(connect(*list2))


#9.定义函数 getMin，接收任意参数,打印最小值

#> 提示：可能为不同的数据类型
# def getMin(*args):
#     a = list(args)
#     a.sort()
#     return a[0]

# print(getMin(*[5,2,4,3,1,6]))



# 10.定义函数 getPoker( )，返回一个扑克牌列表，里面有52项，每一项是一个元组

# > 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]
# list = []
# def getPocker():
#     list1 =["A",2,3,4,5,6,7,8,9,10,"j","Q","K"]
#     list2 =["黑桃","梅花","红桃","方块"]
#     for i in list2:
#         for j in list1:
#             list.append((i,j))
#     return list

# print(getPocker())


#11.定义函数 count( ) ,统计一个字符串中大写字母、小写字母、数字的个数，并以字典为结果返回给调用者

# def count(str1):
#     a = 0
#     b = 0
#     c = 0
#     for i in str1:
#         if i.isupper():
#             a +=1
#         elif i.isnumeric():
#             b += 1
#         elif i.islower():
#             c += 1
#     return a,b,c
# word = "AadfERS1265d8"
# print(count(word))















