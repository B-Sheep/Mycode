#迭代器（扩展）
#为什么学习迭代器？
#作用：对于大数据量的访问，可以节省内存空间。
#原理：迭代器不会一次性都得到所有数据，而是循环一次计算/读取一次，相当于内存中始终只有一份数据
#应用：我们学过的for循环，本质上就是将“可迭代对象”转换为“迭代器”，注意访问元素。

#1.可迭代型对象
#__iter__如果这个对象含有__iter__方法我们就说它是可迭代对象

#dir获取当前数据对象内置的方法和属性

# t1 = [1,2,3,4,5,6,"a","b"]
# print('__iter__' in dir(t1))



# #Python中的可迭代对象有：列表，元组，字典，集合，字符串，文件

# f = open("a.txt","r")
# print("__iter__" in dir(f))

# #可迭代对象，可以遍历数据。 遍历：逐一访问每个元素
# for i in f:
#     print(i,end="")


#2.迭代器
#如果含有__iter__ 和 __next__ 这两个方法，就说它是迭代器
    


#(1)使用iter()将可迭代对象变为迭代器
# t1 = [1,2,3,"a","b","c"]
# it = iter(t1)
# # print(type(it))
# methods = dir(it)
# print("__iter__" in methods and "__next__" in methods)


# t2 = (1,2,3)
# it2 = iter(t2)
# print(type(it2))


# t3 = {1,2,3}
# it3 = iter(t3)
# print(type(it3))

# t4 = {1:"a",2:"b",3:"c"}
# it4 = iter(t4)
# print(type(it4))



#(2)使用next()方法可以遍历迭代器
# t1 = [1,2,3,"a","b","c"]
# it = iter(t1)
# res = next(it)
# print(res)
# res = next(it)        #每执行一次next(),就按照顺序访问下一个元素
# print(res)

# res = next(it)
# print(res)
# res = next(it)
# print(res)
# res = next(it)
# print(res)
# res = next(it)
# print(res)
# res = next(it)
# print(res)


# print("遍历开始")
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("遍历结束")
#         break

# it = iter(t1)   #重置迭代器
# print("遍历开始")
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("遍历结束")
#         break


#定义一个反转字符串的迭代器

class Reverse:

    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        self.index = len(self.data)
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

res = Reverse("abcd")
methods = dir(res)
print("__iter__" in methods and "__next__" in methods)

for char in res:
    print(char,end="")
print()
print("_"*30)
for char in res:
    print(char,end="")


#有其他方法，判断一个对象是否为可迭代对象/迭代器
    
# Iterator  表示迭代器类型
# Iterable  表示可迭代对象    


from collections.abc import Iterator,Iterable

t1 = [1,2,3,"a","b","c"]
res = isinstance(t1,Iterable)          #列表是一个可迭代对象
print(res)
res = isinstance(iter(t1),Iterator)            #列表不是一个迭代器
print(res)




















