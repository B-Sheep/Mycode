#1.类和对象的定义与调用

#定义“车”类

#定义“车”类

class Car:
    energy = "电动"

    def move(self):
        print("在移动")

#定义一辆车
c = Car()
print("能源类型：",c.energy)
c.move()

























