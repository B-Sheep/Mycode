#【局部变量】  函数内部定义的变量

# def test1():
#     a = 100          #局部变量
#     print("test1---------",a,id(a))

# def test2():
#     a = 200          #不同的函数可以定义相同名字的变量，彼此无关
#     print("test2---------",a,id(a))


# test1()
# test2()
# #print(a)         #报错   局部变量只在函数内部有效


# #【全局变量】在文件内有效，能在多个函数中使用的变量

# a = 100       #定义全局变量

# def test1():
#     print(a)    #获取全局变量a

# def test2():
#     print(a)

# test1()
# test2()
# print(a)


# #全局变量和局部变量相同名字

# a = 100

# def test1():
#     a = 300        #局部变量优先使用
#     print("修改前,获取到全局的a:",a)
#     a = 500
#     print("修改后,获取到局部的a:",a)
    
    
# def test2():
#     # a = 1000
#     print("获取局部的a:",a)          #没有局部变量，默认使用全局变量

# print("全局的a:",a)
#test1()
#test2()
# print("test2执行后的全局的a:",a)


# #在函数中修改全局变量

# a = 100

# def test1():
#     global a
#     a = 200
#     print("test1-------",a)

# def test2():
#     print("test2中的全局变量：",a)



# print("全局的：",a)
# test1()
# print("test1执行后全局的：",a)
# test2()


# #可以通过local()和global()打印局部和全局变量

# a = 100
# #b = 500
# def test1():
#     a = 200
#     global b
#     b = 500
#     print(locals())
#     print(globals())


# test1()
# print(b)
# print(locals())
# print(globals())


#形式参数和局部变量

#对于不可变参数，在函数内，每次都是让局部变量指向新的地址值
#所以a = 10，是局部变量a 指向了新数值的新地址，不影响外部的x

#对于可变参数，在函数内，是传递进来的（原有的）地址值上修改数据内容
#所以b.append("bbb"),是修改了（和y相同）地址空间的列表内容，所以外部参数内容会受影响。

def test(a,b):
    print(f"test函数中的变量值,初始,a={a},b={b}")
    a = 10
    b.append("bbb")
    print(f"test函数中的变量值，修改后，a={a},b={b}")


x = 20
y = ["aaa"]
print(f"调用函数前,x={x},y={y}")
test(x,y)
print(f"调用函数后,x={x},y={y}")











































