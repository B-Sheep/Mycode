#普通方法（实例方法）：默认有个self参数，且只能被对象调用。
#类方法：默认有个cls参数，可以被类和对象调用，需要加上_@classmethod_装饰器。 

class Dog:
    legs = 4
    teeth = 42
    # def printInfo(self):
    #     print(f"狗有{self.legs}条腿，{self.teeth}颗牙齿")
    @classmethod
    def printInfo(cls):
        print(f"狗有{cls.legs}条腿，{cls.teeth}颗牙齿")

# d = Dog()
# d.printInfo()
Dog.printInfo()           #默认会补充（传入）参数：cls 表示当前 类



#静态方法：用@staticmethod.装饰的不带_self参数的方法叫做静态方法，\
# 类的静态方法可以没有参数，可以直接使用类名调用。

# class Dog:

#     @staticmethod
#     def bark():
#         print("wangwang")

# d = Dog()
# d.bark()
# Dog.bark()         #静态方法，类和对象均可以调用









