# #类属性和成员属性
# class Dog:

#     legs = 4

#     def __init__(self,name):     #初始化对象的时候，默认被调用
#         self.name = name         #成员属性，每个对象特有的属性；也称作“实例属性”      
#         #self.legs = 4
#         print(f"一只名叫{name}小狗诞生了")


#     def bark(self):
#         print(f"{self.name}:汪汪！")


# c = Dog("饱饱")
# d = Dog("氲氲")
# print("狗狗c的腿数:",c.legs) #访问类属性：对象.属性
# print("狗狗d的腿数:",d.legs)

# print(Dog.legs)              #访问类属性：类名.属性



#对象间的互动
class Dog:

    def __init__(self,name):
        self.name = name
        
    def bite(self,target):
        
        print(f"{self.name}咬了{target.name}")

class Person:

    def __init__(self,name):
        self.name = name
        self.pet = None
        
    def turf_out(self,dog):
        print(f"{self.name}驱赶了{dog.name}")

    def adopt(self,dog):
        self.pet = dog
        print(f"{self.name}收留了{dog.name}")

    def getInfo(self):
        if self.pet:          #可以逐层访问对象及其属性值
            print(f"{self.name}有一只宠物，他的名字是：{self.pet.name}")
        else:
            print(f"{self.name}没有宠物")
            





baobao = Dog("饱饱")
yunyun = Dog("氲氲")
laofanqie = Person("老番茄")


baobao.bite(yunyun)
laofanqie.turf_out(baobao)
baobao.bite(laofanqie)
yunyun.bite(baobao)
# laofanqie.adopt(yunyun)
laofanqie.getInfo()




