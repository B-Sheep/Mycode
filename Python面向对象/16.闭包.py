#1.返回函数
#返回值也可以是函数

def food(name):

    def prepare():
        print(f"[{name}]制作步骤：备菜....")

    def cook():
        print(f"[{name}]制作步骤：烹饪....")

    def serve():
        prepare()
        cook()
        print(f"[{name}]制作步骤：上菜!")
    
    # return serve
    return (prepare,cook,serve)

m = food("番茄操蛋")
# # m[0]()
m[1]()
# m()
# f = food("小鸡炖蘑菇")
# f()


#2.闭包函数
# def outer():
#     a = 5
#     def inner():
#         print(a)
#     return inner
# func = outer()
# func()



#应用场景
# def test(a,b,c):
#     print(a*b+c)

# test(1,1,3)


# def test(a,b):
#     def test_in(c):
#         print(a*b+c)
#     return test_in


# num = test(1,1)
# num(2)
# num(3)



#3.偏函数

# a = int("1100",base=2)
# print(a)

# def int2(x,base=2):
#     return int(x,base=base)


# x = int2('1100')
# print(x)

# x = int2('1100',base=10)
# print(x)



# import functools

# int2 = functools.partial(int,base=2)
# print(type(int2))


# x = int2('1100')
# print(x)






































