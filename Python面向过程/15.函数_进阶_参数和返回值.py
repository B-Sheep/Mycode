#函数基本概念进阶
#1.函数概念
#2.参数
#3.返回值


# #1.函数概念
# #函数定义
# def func():              #函数的命名，和变量名规则相同，同样建议：见名知意
#     pass                #pass是空语句，占位作用
#     print("函数被调用")


# #函数调用
# func()

# print(id(func),type(func))



# #函数名也可以作为变量进行赋值\传递\存储

# def func1():
#     print("func1....")

# def func2():
#     print("func2....")

# def func3():
#     print("func3....")


# res = func1

# print(id(res),id(func1))

# res()

# myfuncs = [func1,func2,func3]

# for f in myfuncs:
#     f()



#2.参数

#（1）位置参数 (普通参数)
# def printInfo(a,b):
#     print(a,b)

# printInfo(10,20)
# printInfo(10)          #使用位置参数时，实参、形参数量要一致：否则报错
# printInfo(10,20,30)    #使用位置参数时，实参、形参数量要一致：否则报错


# #(2)默认参数  （有默认值的参数）
# def printInfo(name,age=18):
#     print(f"姓名：{name},年龄：{age}")

# printInfo("吴彦祖",19)
# printInfo("彭于晏")       #调用时，默认参数可以不赋值


# #def printInfo(name="帅哥",age):        #报错：  有默认值的要放在前面
# def printInfo(name,age=18):    
#     print(f"名字：{name},年龄：{age}")

# # printInfo("吴彦祖",19)     #
# # printInfo("彭于晏")        #调用时，默认参数可以不赋值

# printInfo()



# #（3）指定参数名赋值     指的是函数调用时，根据参数名，进行针对性赋值

# def printInfo(name,age=18,gender="男"):    
#     print(f"名字：{name},年龄：{age}，性别：{gender}")

# printInfo(age=20,name="吴彦祖")     #因为制定了形参变量名，所以可以不按照位置循序递进参数 

# printInfo("Samantha",gender="女",age=18)
# #printInfo(gender="女",age=18",Samantha")    #如果关键字实参  和位置参数  混合使用，位置实参在前面。否则报错



#（4）可变参数  （数量）
#*args arguments       可变参数
#**kwargs   keyword arguments  关键字参数    


#在“函数定义”时，*和**作用：将多个变量进行“打包”，变为元组或字典
# def printInfo(name,age,gender,*args):
#     print(f"名字：{name}，年龄：{age}，性别：{gender}")
#     print(args,type(args))      #tuple

# printInfo("彭于晏",28,"男",8.9,8.3,9.0)


# def printInfo(name,age,gender,**kwargs):
#     print(f"名字：{name}，年龄：{age}，性别：{gender}")
#     print(kwargs,type(kwargs))      #dict

# printInfo("Eason",28,"男",身高=1.72,国籍="中国",出身地="香港")



#在函数调用时，*和**的作用是：“解包”
#*将传进来的字符串、元组、列表、集合转为多个标准参数
#**将传进来的字典，转化为多个关键字参数


# def printInfo(name,age,gender,*args):
#     print(f"名字：{name}，年龄：{age}，性别：{gender}")
#     print(args,type(args))   


# rate = [8.3,8.9,8.1]
# # rate = {8.3,8.9,8.1}    #无序
# # rate = (8.3,8.9,8.1)#
# printInfo("Eason",48,"男",*rate)



def printInfo(name,age,gender,**kwargs):
    print(f"名字：{name}，年龄：{age}，性别：{gender}")
    print(kwargs)    
    for key,value in kwargs.items():
        print(f"{key}:{value}",end="\t")  



info = {"身高":1.72,"国籍":"中国","出身地":"香港"}
printInfo("Eason",28,"男",**info)


 
# #函数调用时，参数传递的顺序：
# #      （调用时）实际参数：位置参数、关键字参数
# #       顺序：args  、*args、 **kwargs

# def testArgs(a,b,c=10,d=20,*args,**kwargs):
#     print(f"a={a},b={b},c={c},d={d},args={args},kwargs={kwargs}")

# #testArgs(1,2,3,c=4,5,6,7,x=100,y=200)     #关键字参数之后不能再使用位置参数（只能使用关键字参数）

# def testArgs(*args,a,b,c=10,d=20,**kwargs):
#     print(f"a={a},b={b},c={c},d={d},args={args},kwargs={kwargs}")

# testArgs(1,2,3,4,5,a=6,c=100,b=7,x=100,y=200)


# #【命名关键字参数】
# # *后面的参数，被称为"命名关键字参数"
# def testStar(a,b,c,*,name,age):
#     print(f"a={a},b={b},c={c},name={name},age={age}")

# testStar(1,2,3,"吴彦祖",30)         # * 的作用，表示*后面的参数必须使用命名的方式来进行参数赋值


#3.返回值
#可以返回全部数据类型
# def test():
#     pass
#     return "abc" 
#     # return 2.0 
#     # return True 
#     # return ["200"] 
#     # return {"a":3} 
#     # return (3,5) 
#     # return {1,2,3} 
#     # return None       #没有返回值时，默认返回为None 

# res = test()
# print(res,type(res))


#返回多个值的函数
#将需要返回的多个值，封装在列表、字典、元组在容器中。(set会改变数据的顺序)

# def divid(a,b):
#     shang = a//b
#     yushu = a%b
#     # return [shang,yushu]
#     # return (shang,yushu)
#     return shang,yushu



#res = divid(5,2)
# print(f"商：{res[0]},余数：{res[1]}")
# print(res,type(res))

# sh,yu = divid(5,2)
# print(f"商：{sh},余数：{yu}")
