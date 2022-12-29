#5.多继承
#子类可以多个父类
#例如： 狗是  脊椎动物   哺乳动物   宠物


# class Father: 
#     caihua="有才"

# class Mother: 
#     yanzhi="有貌"

# class Child(Father,Mother):
#     pass 


# c=Child() 
# print(c.caihua,c.yanzhi)


# print(Child.__bases__)                #可以通过类名。__bases__查看继承的类



#6.访问子类的属性或方法时，解析的路径（顺序）
#深度优先：Child -》 Father ——》GrandFather ——》Mother

# class GrandFather: 
#     def getMoney(self): 
#         print("爷爷给了零花钱...")
 
# class Father: 
#     def getMoney(self): 
#         print("父亲给了零花钱...")

# class Mother: 
#     def getMoney(self): 
#         print("母亲给了零花钱...") 

# class Child(Father,Mother):
#     def getMoney(self):
#         super().getMoney()                #按照继承顺序查找父类中的方法，先找Father
#         print("孩子有了零花钱")


# c = Child()
# c.getMoney()



#7.菱形继承（了解）
#       Human
#         |
#   |--------------|
#Father          Mother
#   |--------------|
#          |
#       Child

#广度优先： Child ——> Father  -----> Mother ----->  Human 

class Human:
    def __init__(self):
        print("人类...")

class Father(Human):
    def __init__(self): 
        print("父亲初始化...") 
        super().__init__() 
        print("父亲初始化结束..." )

class Mother(Human): 
    def __init__(self): 
        print("母亲初始化...") 
        super().__init__() 
        print("母亲初始化结束...")

class Child(Father,Mother): 
    def __init__(self): 
        print("孩子初始化...") 
        super().__init__( )
        print("孩子初始化结束...")


c = Child()

print(Child.mro())

# 孩子初始化.. 
# 父亲初始化.. 
#母亲初始化.. #人类...
#母亲初始化结束.. 
# 父亲初始化结束.. 
# 孩子初始化结束...




























































