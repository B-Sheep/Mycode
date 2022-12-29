# 1.写一个代码片段统计一个字符串中出现、
# 的字符及其个数。（至少2种方式：分别
# 使用列表和字典来实现）

# > 例如对于字符串“abcaaabcd”，、
# 统计的结果是：a（4个）b（2个）c（2个）d（1个）

# list1 = ["abcaaabcd"]
# word = " ".join(list1)
# set1 = set(word)
# for i in set1: 
#     for j in range(len(list1)):
#         a = word.count(i)
#         print(f'{i}({a}个)',end=" ")


# str1 = "abcaaabcd"
# list1 = list(str1)
# set1 = set(list1)
# for i in set1:
#     a = list1.count(i)
#     print(f'{i}({a}个)',end=" ")



# str1 = "abcaaabcd"
# dict1={}
# for i in str1:
#     num1 = str1.count(i)
#     dict1[i] = num1   
# for name,num in dict1.items():
#     print(f"{name}({num}个)",end=" ")



# str1 = "abcaaabcd"
# dict1=dict.fromkeys(str1)

# for i in dict1.keys():
#     dict1[i]=str1.count(i)
# print(dict1)
# for k,v in dict1.items():
#     print(f"{k}({v}个)",end=" ")



# 2.循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环），输入结束打印列表

# 如果用户输入的信息已经存在，则提示用户所输内容已存在，不再重复添加。

# > 提示：对于输入内容，需要考虑大小写和空格的情况


# list1 = []
# while True:
#     word1 = input("请输入:")
#     if word1 == ("n" or "N"):
#         break
#     elif word1 in list1:
#         print("用户所输内容已存在，不再重复添加。")
#         continue
#     else:
#         list1.append(word1)
# print(list1)    



# 3.有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,\
#将所有大于 66 的值保存至字典的第一个key对应的列表中，\
#将小于 66 的值保存至第二个key对应的列表中。打印输出result。

# li = [11,22,33,44,55,66,77,88,99,90]
# result = {"k1":[],"k2":[]}
# for i in li:
#     if i>66:
#         result["k1"].append(i)
#     elif i < 66:
#         result['k2'].append(i)
# print(result)       



# 4.经理：[曹操,刘备,孙权]。 技术员：[曹操,刘备,张飞,关羽]。

#   使用两个列表分别存储经理与技术员。

#   使用集合计算：

# （1） 即是经理也是技术员的有谁？

# （2） 是经理，但不是技术员都有谁？

# （3） 是技术员，但不是经理都有谁？

# （4）张飞是经理吗？

# （5） 身兼一职的都有谁？

# （6） 经理和技术员共有几个人？

# manager = ["曹操","刘备","孙权"]
# technician = ["曹操","刘备","张飞","关羽"]
# set1 = set(manager)
# set2 = set(technician)

# #(1)
# guy1 = set1&set2
# print(guy1)
# print("-"*30)

# #(2)
# guy2 = set1-set2
# print(guy2)
# print("-"*30)

# #(3)
# guy3 = set2-set1
# print(guy3)
# print("-"*30)

# #(4)
# if "张飞" in manager:
#     print("是")
# else:
#     print("不是")    
# print("-"*30)

# print('张飞是经理吗？',technician<=manager)     #用集合的方式（更简便）


# #(5)
# guy5 = set1|set2
# for i in guy5:
#     if i in manager not in technician:
#         print(i,end=" ")
#     elif i in technician not in manager:
#         print(i,end=" ")
    
# print()        
# print("-"*30)

# print('身兼一职的是',set1^set2)   #用集合的方式（更简便）


# #(6)
# guy6 = set1|set2
# print(len(guy6))



# 【综合练习】

# 现有商品列表如下：

#1.products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]，需打印出以下格式：

# ```python
# ------  商品列表 ------
# 0  iphone    6888
# 1  MacPro    14800
# 2  小米6      2499
# 3  Coffee    31
# 4  Book      60
# 5  Nike      699
# ```

# 	2.	提示用户输入预算，并在每次购买时查看余额是否充足。不足时，提示“余额不足”。
#  	3.	根据上面的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表。
#  	4.	购买结束时，输出全部购买产品的编码、名称、单价和数量，并在最后集中显示“总计”和“余额”

# ```
# 例如:
# 请输入您的预算：10000
# ------  商品列表 ------
# 0  iphone    6888
# 1  MacPro    14800
# 2  小米6      2499
# 3  Coffee    31
# 4  Book      60
# 5  Nike      699
# 请选择您要购买的商品编码：1
# 您的余额不足。
# ------  商品列表 ------
# 0  iphone    6888
# 1  MacPro    14800
# 2  小米6      2499
# 3  Coffee    31
# 4  Book      60
# 5  Nike      699
# 请选择您要购买的商品编码：0
# 已将iphone放入购物车。
# ------  商品列表 ------
# 0  iphone    6888
# 1  MacPro    14800
# 2  小米6      2499
# 3  Coffee    31
# 4  Book      60
# 5  Nike      699
# 请选择您要购买的商品编码：q
# ------  购物清单 ------
# 编码	   商品名称   单价   数量	
# 0  		iphone    6888	 1
# ----------------------------
# 总计                   6888元
# 余额                   3112元
# 感谢您的惠顾。
# ```



# > 提示：
# >
# > seq = [1,2,3]
# >
# > for i,x in enumerate(seq):
# >
# > ​		print(i,x)



products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],\
    ["Book",60],["Nike",699]]
dict1 = []
id = []
print("商品列表".center(15,'-'))
for x,i in enumerate(products):   
    print(x,end="\t")
    for j in i:
        print(j,end="\t")
    print()
sum = 0
budget = int(input("请输入你的预算:"))
while True:
    goods = input("请选择您要购买的商品编码：")
    if goods == "q":
        break
    if budget < products[int(goods)][1]:
        print("您的余额不足")
    elif budget >= products[int(goods)][1]:
        id.append(int(goods))
        print(f"已将{products[int(goods)][0]}放入购物车")
        budget -= products[int(goods)][1]
        sum += products[int(goods)][1]       
        dict1.append(products[int(goods)])   #dict1 = [[0,"iphone",6888],[1"MacPro",14800],[0,"iphone",6888],[2,"小米6",2499],.......] 
dict2 = dict(dict1)
list1 = []     
print("购物清单".center(15,'-'))
print("编码\t",'商品名称\t','单价\t','数量\t'  )
for num2 in range(len(id)):
    dict1[num2].insert(0,id[num2])
for num1 in dict1:
    if num1 not in list1:
        list1.append(num1)
for p,length in enumerate(list1):
    print(length[0],length[-2],length[-1],length.count(length[0]),sep="\t")
print("-"*20)
print(f"总计{sum}\n余额{budget}\n感谢您的惠顾。")




     
 





































