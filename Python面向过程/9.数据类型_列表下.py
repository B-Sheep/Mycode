#4.列表的嵌套（二维列表，三维列表....)
#简单的理解：列表的元素也是列表。
# namelist = []  #一维空列表
# print(len(namelist))

# namelist = [[],[],[]]      #有3个元素的空列表，每个元素都是一个空列表
# print(len(namelist))

# zhangsan = ["张三",18,"男"]
# lisi = ["李四",19,"女"]
# wangwu = ["王五",20,"男"]

# namelist = [zhangsan,lisi,wangwu]
# #print(namelist)

# #二维数据，类似表格的储存形式
# # ["张三",18,"男"]
# # ["李四",19,"女"]
# # ["王五",20,"男"]

# # print(namelist[0])     #通过索引，获取到的第一个元素是一个列表
# # print(namelist[0][0])  #通过第二个中括号中的索引，获取的是第一个列表的第一个元素


# for person in namelist:
#     print(person)
#     for i in person:
#         print(i,end=",")
#     print()



#练习题：
#一个学校，有三个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

#扩展：随机数的生成
# import random
# num = random.randint(0,2)    #随机生成[0,2]区间内的一个整数
# print(num)

offices = [[],[],[]]   #有三个元素的空列表，每个元素都是一个空列表
# #未来可能形成的结果：[["A","D","H"],["B","C"],["E","F","G"]]

names = ["A","B","C","D","E","F","G"]

import random
for name in names:
    num = random.randint(0,2)
    # print(num)
    # print(name,end=",")
    offices[num].append(name)

i = 1
for office in offices:
    print(f"办公室{i}的人数为：{len(office)}")
    i += 1
    for name in office:
        print(name,end=",")
    print()
    print("-"*20)




