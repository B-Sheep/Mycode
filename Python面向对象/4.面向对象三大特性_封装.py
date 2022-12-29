#封装

#对外部隐藏信息，不能随意访问/修改对象的数据、方法
#通过限制类的属性和方法的访问方式,实现“封装”效果.

#封装的三个层次:
#类的封装：外部可以任意访问/修改类中的属性和方法
#私有属性：外部不可以任意访问/此改类的属性或方法
#公有方法+私有属性：外部有条件限制的访问/修改属性，调用方法



#封装表现1：
#类的定义：将某些特定属性和方法进行“隔离”
#每个学生都有自己的年龄，外部可以通过对象任意读取或修改

# class Student:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s1 = Student("李白",18)
# s2 = Student("杜甫",20)
# s2.age = 200
# print(s1.name)
# print(s2.name)



#封装表现2
#属性私有：只能在类的内部使用，外部不能使用。
#不让外部读取/修改学生的年龄

# class Student:
    
#     __secret = True

#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age     #使用两个下划线开头的属性,定义为私有属性
#         #print(self.__age)        

# s1 = Student("李白",18)
#print(s1.__age)          #外界无法直接通过属性名称来访问
# print(s1._Student__age)   #虽然语法可以在外部通过_Student__age访问到私有属性

#__dict__
# print(s1.__dict__)           #可以查看s1对象的属性值

# print(Student.__dict__)
# print(Student.__secret)



#封装表现3：
#私有属性 + 共有方法 ：有限制条件的开放给外部
#可以读取年龄，但是不能随意修改年龄
#设定年龄必须在【1，125】之间

# class Student:
    

#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age 

#     def getAge(self):
#         return self.__age
    
#     def setAge(self,age):
#         if 0<age<125:
#             self.__age = age
#         else:
#             print("不能随意修改年龄")
    
# s1 = Student("李白",18)
# print(s1.getAge)
# s1.setAge(200)
# print(s1.getAge)



#封装的常用（简化）写法

#装饰器
#property装饰器：把一个方法伪装成一个属性，在调用这个方法的时候不需要加()就可以直接得到返回值

# class Dog:

#     @property
#     def bark(self):
#         print("wangwang")
#         return "aa"

# d = Dog()
# s = d.bark
# print(s)


# class Student:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age 

#     @property    
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self,age):
#         if 0<age<125:
#             self.__age = age
#         else:
#             print("不能随意修改年龄")
                
# s1 = Student("李白",18)
# print(s1.age)
# s1.age = 200
# print(s1.age)

#总结：

#使用@property 装饰器，方法名不必与属性名相同
#可以更好地防止外部通过猜测私有名称来访问
#凡是赋值语句，就会触发set方法。获取属性值，会触发get方法



#私有方法，可以在类的内部使用
#可以有条件的开放给外部

# class Student:

#     def talk(self,identity):
#         if identity == "死党":
#             self.__tellSecret()
#         else:    
#             print("闲聊...")
        
            
    
#     def __tellSecret(self):
#         print("我有一个秘密...")


# s = Student()
# s.talk("死党")














































