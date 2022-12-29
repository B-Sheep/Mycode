#1.列表的创建与元素访问

#方法一：直接赋值
# namelist = []       #定义一个空列表
# print(namelist,type(namelist))

# namelist = ["小爱","小心","小吴"]
# print(namelist)

# testlist = [11,22,33,0,True,"aa",22]   ##下标 ，索引[0,2]
# print(testlist)

# print(testlist[0],type(testlist[0]))
# print(testlist[3],type(testlist[3]))
# print(testlist[5],type(testlist[5]))


#字符串和列表都属于序列的概念，所以很多方法都是类似的
#列表的切片，可以参考字符串的相关操作

# list1 = [10,20,30,40,50,60,70]
# print(list1[0:3])
# print(list1[0:5:2])      #[2,5) 左闭右开，[起始索引：结束索引：步进值]



#方法二：通list()方法创建或强制类型转化为列表   str()   int()
# a = list()  #创建一个空的列表对象
# print(a)

# a = list("IT私塾")
# print(a)

# a = list(range(10))
# print(a)
# b = list(range(2,-3,-1))
# print(b)



# #方法三：通过列表推导式创建列表  （了解）
# a = [x*2 for x in range(5)]
# print(a)




#2.常用操作 len()、max()、min()、sum()
#(1)列表的循环遍历
# namelist = ["小爱","小心","小吴"]
# for name in namelist:
#     print(name)

# print(len(namelist))


# i = 0
# while i < len(namelist):
#     print(namelist[i])
#     i += 1


#(3)max()和min() 获取列表中最大和最小的元素
#list1 = [3,2,1]
#list1 = ["aa","bb","cc"]
#list1 = [False,2.0,30,0]
#list1 = [2.0,30,False,"aa"]    #报错，字符串和数值无法比较
# print(max(list1))
# print(min(list1))


#(4)sum()对全部为数值类型元素的列表求和
# list1 = [10,20,30]
# print(sum(list))



#3.常用数据操作
#基本的数据操作：增、删、改、查

#增:    [append]追加
# namelist = ["小爱","小心","小吴"]

# print("--------增加前，名单列表的数据---------")
# for name in namelist:
#     print(name,end=",")

# nametemp = input("\n请输入学生姓名：")
# namelist.append(nametemp)     #在末尾追加一个元素

# print()

# print("--------增加后，名单列表的数据---------")
# for name in namelist:
#     print(name,end=",")


#增：      [extend]扩展
# a = [1,2]
# b = [3,4]
# a.append(b)          #将列表当作一个元素，加入到a列表中
# print(a)

# a.extend(b)          #将b列表中的每个元素，注意追加到a列表中
# print(a)


#增：    [+]操作
# list1 = [10,20,30]
# list2 = [40,50]
# res = list1+list2
# print(res,id(res))            #[10,20,30,40,50,]
# print(list1)

# list1.extend(list2)
# print(list1,id(list1))


#增：  [*]操作（了解）
# list1 = [1,2,3]
# list2 = list1*3
# print(list2)


#增:   [insert]插入
# a = [0,1,2]
# a.insert(2,3)     #第一个变量表示下标，第二个表示元素(对象)
# print(a)          #指定下表位置插入元素


#删    【del】 【pop】 【remove】
#       删除    弹出    移除
'''
movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','速度与激情']

print("----------删除前，电影列表的数据----------")
for name in movieName:
    print(name,end=",")

print()

# del movieName[1]      #在指定位置删除一个元素，没有返回值

# movie = movieName.pop()          #默认弹出末尾最后一个元素，有返回值（被弹出的那个元素）
# print("被pop弹出的元素:",movie)

# movie = movieName.pop(-2)
# print("被pop弹出的元素:",movie)

movieName.remove("指环王")         #直接删除指定"内容“的元素，但只删除匹配到的第一个





print("----------删除后，电影列表的数据----------")
for name in movieName:
    print(name,end=",")
'''



#改：
# print("--------增加前，名单列表的数据---------")
# for name in namelist:
#     print(name)


# namelist[2] = "小红"

# print("--------增加后，名单列表的数据---------")
# for name in namelist:
#     print(name)



#查：
# [in,  not in]
# findName = input("请输入你要查找的学生姓名：")

# if findName in namelist:
#     print("在学员名单中找到了相同的名字")
# else:
#     print("没有找到")

##【index】
# mylist = ["a","b","c","a","b"]

# print(mylist.index("b",1,4))     #可以查找指定下标范围的元素，并返回找到对应数据的下标
# #                                #例如在(1,4)区间内查找

# print(mylist.index("a",1,3))        #范围区间， 左闭右开  [1,3)
# #                                   #找不到会报错


#【count】
# mylist = ["a","b","c","a","b"]
# print(mylist.count("a"))
   


# #排列和反转
# a = [1,4,2,3]
# print(a,id(a))

# a.reverse()        #将列表所有元素反转
# print(a,id(a))     #a的地址没有改变

# a.sort()           #升序排列
# print(a,id(a))    #a的地址没有改变

# a.sort(reverse=True)           #降序排列
# print(a,id(a))  