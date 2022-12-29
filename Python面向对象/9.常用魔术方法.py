#魔术方法|特殊方法（拓展）
#在Python中，所有以“__”双下划线包起来的方法，都统称为“Magic Method”（魔术方法）

#1.__init__

class Pig:

    def __init__(self):
        print("一只小猪出生了")

p = Pig()

#2.__new__
#对象初始化：
#    先执行__new__:分配内存空间，并返回构建好的对象
#    在执行__init__:为构建好的对象赋予初始值

class Pig:
    
    def __new__(cls):
        print("分配空间...")
        obj = object.__new__(cls)
        print(obj)
        return obj
        # return None     #如果返回为None,__init__方法将不会被调用

    #__new_返回的对象（地址）就是__init__方法中的self所指向的对象
    def __init__(self):
        print(self)
        print("一只小猪诞生了")

p = Pig()        

class Pig:
    #__new__方法中的*args，**kwargs会将接收到的函数自动传递到__init__方法中
    def __new__(cls,*args,**kwargs):
         print(f"args:{args},kwargs:{kwargs}")
         return object.__new__(cls)
    
    def __init__(self):
            print(self)
            print("一只小猪诞生了")

p = Pig("佩奇",brother="乔治")

#3.__del__
#从内存中清除对象的时候，对象会默认执行的方法 
#（1）.程序执行完毕后，释放内存时 
#(2).执行deL指令时



#删除了p1 为什么没有释放内存呢
#只有当指向对象的所有变量都被删除的时候，对象空间才会被释放
class Pig:
     
    def __init__(self):
        print("++对象被初始化了++")

    def __del__(self):
        print("--对象被删除了--")

p1= Pig()
p2 = p1
del p1                    #手动删除对象，释放内存
#print(p1)
del p2
print("[程序执行完毕了]")



#4.__call__
#将对象当作函数执行的时候会被默认调用

#(1)概念
class Flight:

    def __call__(self,*args,**kwargs):
        print("__call__方法被调用了")

f = Flight()
f()

#(2)应用
class Flight: 
    def __init__(self,number): 
        self.number=number 
        print(f"{number}号航班") 
        #办理登机手续 
        def checkIn(self): 
            print("办理登机手续") 
        #安全检查   
        def securityCheck(self): 
            print("安全检查") 
        #登机,起飞 
        def bording(self):
            print("登机,起飞")

        def __call__(self,state): 
            #print("__call__方法被调用了")
            print("飞机当前状态：",state)
            self.checkIn()
            self.securityCheck()
            self.bording()
f = Flight("CA1426")
f()
# f.checkIn()
# f.securityCheck()
# f.bording()
# f()



#_5.__str 
#（1）打印一个对象的时候，默认会被调用 
#（2）使用str(）对对象进行强制转化后，输出结果时会被调用 
class Dog: 
    def __init__(self,name): 
        self.name=name

    def __str__(self):
        #return 123 
        print(super().__str__())          #还可以通过调用父类对象的__str__方法，打印原有结果
        return f"这是一只名字叫{self.name}的狗 "
    
d = Dog("yunyun")
print(d)

res = str(d)
#print(res)



#6.__repr__
class Dog:
    
    def __init__(self,name):
        self.name = name

    def __str__(self):
        print("__str__")
        return f"这是一只名字叫{self.name}的狗 "

    def __repr__(self):
        print("__repr__")
        return f"dog:{self.name}"

d = Dog("yunyun")
print(d)

x = [d]
print(x)



