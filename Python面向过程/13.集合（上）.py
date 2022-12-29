# s1 = set()       #空集合
# print(s1,type(s1))

# s1 = {1,2,3,4}
# print(s1,type(s1))


#集合：无序
# s1 = {1,2,3,4}
# s1 = {4,3,2,1}
# s1 = {"小爱","小心","小吴"}
# print(s1,type(s1))       #小结:集合中存放的数据是“无序”的


# #集合：自动去重(去除重复)

# s1 = {1,2,3,4,4,3}
# print(s1)


# #集合：只能存放不可变元素（key）
# s1 = {2.0,True,1,"abc"}     #字典也可以存放多种数据类型
# s1 = {2.0,True,1,"abc",{"id":1}}     #报错 ：TypeError：unhashable type:'dict'
# s1 = {2.0,True,1,"abc",[3,4]}        #报错 ：TypeError：unhashable type:'list'
# s1 = {2.0,True,1,"abc",(3,4)}

# print(s1)

#小结：集合中只能存放不可变的类型。列表（list）和自带你（dict）不能存放在集合中



#增：add
# s1 = {1,2,3,4}
# print(s1,id(s1))

# s1.add(6)
# print(s1,id(s1))


#将指定的序列，依次加入到集合中

# s1.update("abcd")
# print(s1,id(s1))


# s1 = {1,2,3,4}
# s2 = ["aa","bb","cc"]
# s1.update(s2)
# print(s1,id(s1))


#删：clear remove pop discard
# s1 = ["a","b","c","d"]
# # s1.clear()          #清空集合中的元素
# x = s1.pop()           #pop随机弹出一个元素，每次执行结果不一定相同
# print(x,s1)


# s1.remove("e")       #只能通过元素内容来删除，如果没有找到指定元素，报错：keyerror
# print(s1) 
 

# s1.discard("a")        #如果没有找到指定元素，不做任何操作
# print(s1)


# #改： 变相删除，先删后增
# s1 = ["a","b","c","d"]
# s1.remove("b")
# s1.add("e")
# print(s1)


#查
#遍历
# s1 = ["a","b","c","d"]

# for i in s1:
#     print(i)


#包含in， not in
s1 = ["a","b","c","d"]
res = "a" not in s1
print(res)













