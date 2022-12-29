# #对象实例化（初始化）

# class Dog:

#     def bark(self):      #实例方法  |   成员方法
#         print(id(self))   
#         print("汪汪！")

# c = Dog()
# c.bark()


# #对象的属性
# #（1）在类的外部，添加对象属性
# #（2）在类的内部，添加对象属性

# class Dog:

#     def bark(self):      #实例方法  |   成员方法  
#         print(f"{self.name}:汪汪！")

# c = Dog()       #初始化一个对象，就会分配一个新的内存空间
# c.name = "晕晕"
# d = Dog()
# d.name = "氲氲"
# # print(f"{c.name}:",end="")
# c.bark()
# # print(f"{d.name}:",end="")
# d.bark()


#魔法方法：前后用两个下划线包裹的，具有特殊功能对的方法
#魔法方法：__init__方法

# class Dog:

#     def __init__(self):     #初始化对象的时候，默认被调用
#         print("__init__",id(self))
#         print("一只小狗诞生了")

#     def bark(self):
#         print(id(self),"bark.....")

# c = Dog()
# print(id(c))
# c.bark()

#(2)在类的__init__方法中，添加对象属性
#如何让每只小狗出生时必须有名字
# class Dog:

#     def __init__(self,name):     #初始化对象的时候，默认被调用
#         self.name = name         #成员属性，每个对象特有的属性；也称作“实例属性”
#         print(f"一只名叫{name}小狗诞生了")

#     def bark(self):
#         print(f"{self.name}:汪汪！")


# c = Dog("晕晕")
# c.bark()
# d = Dog("氲氲")
# d.bark()

















