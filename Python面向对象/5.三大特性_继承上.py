#继承

#面临的问题
#相似类型的定义过程中，大量重复性的代码
#让类的定义具有更好的扩展性
#解决的方法：定义类型之间的关系，子类 拥有 父类的全部属性和方法

# class Dog:

#     def __init__(self,name):
#         self.name = name
#         print(f"一个名叫{self.name}的宠物出生了")

#     def eat(self):
#         print(f"{self.name}在吃东西...")

#     def sleep(self):
#         print(f"{self.name}在睡觉...")

        
# class Cat:

#     def __init__(self,name):
#         self.name = name
#         print(f"一个名叫{self.name}的宠物出生了")

#     def eat(self):
#         print(f"{self.name}在吃东西...")

#     def sleep(self):
#         print(f"{self.name}在睡觉...")


# d = Dog("氲氲")
# d.eat()
# c = Cat("晕晕")
# c.sleep()



# class Pet:
#
#     master = True
#
#     def __init__(self,name):
#         self.name = name
#         print(f"一个名叫{self.name}的宠物出生了")
#
#     def eat(self):
#         print(f"{self.name}在吃东西...")
#
#     def sleep(self):
#         print(f"{self.name}在睡觉...")
#
#
#
# class Dog(Pet):          #class 类名(父类名)：
#     pass
#
#
# class Cat(Pet):
#     pass
#
#
# #1.继承的概念
# #Dog和Cat继承了Pet类
# #Dog和Cat称为Pet的子类，派生类
# #Pet称为Dog和Cat的父类/超类/基类
#
# d = Dog("氲氲")
# d.eat()
# c = Cat("晕晕")
# c.sleep()

#子类默认拥有父类公有的属性和方法的定义

# #2.子类调用方法顺序
# #工子类中有，调用子类的
# #子类中没有，调用父类的
# #一旦在子类中找到，.就不在父类中查找了


# #每个对象修改类属性的值，仅在对象内部有效
# # c.master = False
# # print(d.master)
# # print(c.master)
# # print(Pet.master)
#
# #如果类属性做了修改，所有对象的值都会跟着改变
# Pet.master = False
# print(d.master)
# print(c.master)
# print(Pet.master)



#子类不能继承父亲的私有属性或方法

# class Father:
#
#     __secret = "XXXX"
#     story = "从前有座山..."
#
#     def tellstory(self):
#         print("我的故事：",self.story)
#
#     def __tellstory(self):
#         print("我的秘密：",Father.__secret)


# class Son(Father):
#
#     def tell(self):
#         self.tellstory()
#
# s = Son()
# s.tell()



#3.覆盖/重写
# #子类和父类有相同名称的方法
# #可以理解为子类对于父类行为的扩展或补充

class Pet:

    def __init__(self,name):
        self.name = name
        print(f"一个名叫{self.name}的宠物出生了")

    def eat(self):
        print(f"{self.name}在吃东西...")



# class Dog:
#
#     def lookAfter(self):              #重写父类的eat方法，重新定义父类的方法
#         print(f"{self.name}在看门")
#
#     def eat(self):
#         print(f"{self.name}在啃骨头...")
#
# d = Dog("云云")
# d.eat()                #当子类和父类方法相同时，只会调用子类方法
# d.lookAfter()










#4.子类可以在类定义时，可以使用super()调用父类的方法

class Cat(Pet):

    #应用2：对象初始化时，简化重复属性的赋值
    def __init__(self,name,age,sex):
        #self.name = name
        #print(f'一个名叫{self.name}的宠物出生了）
        #super(Cat,self).__init__(name)
        super().__init__(name)
        self.age = age
        self.sex = sex


    #应用1：在重写方法时，通过super()调用父类方法后，拓展功能
    def eat(self):
        print(f"{self.name}伸个懒腰")
        super().eat()
        #self.eat()  #不可行,默认死循环
        print(f"{self.name}吃完东西后。用唾液洗洗脸....")

c = Cat("晕晕",3,"雌性")
c.eat()




























































