#多态
#想要解决的问题：
#1.让程序能够有更强的灵活性
#2.让程序能够有更好的适应性


#概念：一个类的多种形态

class Animal:
    def eating(self):
        print("动物在吃东西...")


class Pet(Animal):
    def eating(self):
        print("宠物在吃东西...")

class Dog(Pet):
    def eating(self):
        print("狗在啃骨头...")

class Cat(Pet):
    def eating(self):
        print("猫在吃鱼...")

class Zoo:

    def animalEating(self,animal):
        if isinstance(animal,Animal):
            print("这是展示动物吃东西的地方")
        else:
            print("这是展示非动物吃东西的地方")
        animal.eating()

z = Zoo()
a = Animal()
d = Dog()
c = Cat()



#Dog 和 Cat作为Animal的不同形态
#都可以直接调用animal所具有的属性或方法
z.animalEating(a)
z.animalEating(d)
z.animalEating(c)


#情况二：Python特有
#没有继承关系，但是具备相同特征/方法，也可以直接使用

class VenusFlytrap:
    def eating(self):
        print("捕蝇草在吃小虫子...")

v = VenusFlytrap()

z.animalEating(v)


#判断类型时，只看直接类型
print(type(c) is Cat)           #True
print(type(c) is Animal)        #False
print(type(c) is Pet)           #False


#isinstance  判断对象是否为一个类型地实例
#判断实例类型时，涵盖父爱的类型
print("*"*30)
print(isinstance(c,Cat))      #True
print(isinstance(c,Pet))      #True
print(isinstance(c,Animal))   #True
print(isinstance(v,Animal))   #False     








