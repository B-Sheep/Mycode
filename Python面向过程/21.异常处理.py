#1.发生异常
#print(a)    #语法错误

#运行时的错误，称为“异常”
# a = input("请输入一个整数")
# print(int(a))






# #2.捕获异常
# try:
#     n = input("请输入被除数")
#     m = input("请输入除数")
#     res = float(n)/float(m)
#     print("res:",res)            #这句代码不会被执行
# except:
#     print("出错了")
# print("程序继续运行并正常结束")


# #（1）指定要捕获的异常类型
# try:
#     print(num)
# except ValueError:            #异常错误类型想要被捕获，需要一致
# # except NameError:
#     print("发生了",NameError,"错误")



# #（2）如何针对不同的错误，进行不同的处理呢
# try:
#     n = input("请输入被除数")
#     m = input("请输入除数")
#     res = float(n)/float(m)
#     print("res:",res)     
# except ValueError:
#     print("请输入数字")
# except ZeroDivisionError:
#     print("除数不能为零")


#（3）捕获所有异常
# try:
#     n = input("请输入被除数")
#     m = input("请输入除数")
#     res = float(n)/float(m)
#     print("res:",res) 
# except BaseException:          #注意：错误类型，子类在前，父类在后 （范围小的在后面）
#     print("出错了")
# except ValueError:
#     print("请输入数字")
# except ZeroDivisionError:
#     print("除数不能为零")

# print("程序继续运行并正常结束")



# try:
#     n = input("请输入被除数")
#     m = input("请输入除数")
#     res = float(n)/float(m)
#     print("res:",res) 
# except Exception as a:
#     print(a,type(a))
#     print('str(Exception):\t',str(Exception))
#     print('str(a):\t\t',str(a))  #根据错误对象不同，显示其中的错误信息
#     print('repr(a):\t',repr(a))  #内置函数repr：返回一个对象的string格式



# #（5）try。。。。。。。except。。。。。。else。。。。。finally

# try:
#     n = input("请输入被除数")
#     m = input("请输入除数")
#     res = float(n)/float(m)
#     print("res:",res) 
# except Exception as a:
#     print("出错了")
# else:
#     print("res:",res)
# finally:
#     print("用户输入完毕，计算结束")    #不论程序是否正常运行，finally中的代码都会执行



# #3.嵌套的异常处理
# try:
#     f = open("test.txt","r",encoding="utf-8")
#     for line in f:
#         try:
#             3/0
#         except ZeroDivisionError:
#             print("计算错误")
#         print(line,end="")    
# except ZeroDivisionError:
#     print("除数不能为0")
# finally:
#     if f:
#         f.close() 


#（7）【with】上下文管理器(进阶)
#省略f.close()代码，实现自动关闭

# with open("test.txt",'r',encoding="utf-8") as f:
#     for line in f:
#         print(line,end="i")


#【with语句】通过“上下文管理器”实现文件操作的简化
#图片的复制

# with open("123.jpg","rb")as fin:
#     with open("123_copy3.jpg","wb")as fout:
#         for data in fin:
#             fout.write(data)

#简单写法：open之间可以用逗号 ，隔开
# with open("123.jpg","rb")as fin,open("123_copy3.jpg","wb")as fout:
#     for data in fin:
#             fout.write(data)


#4.自定义异常（拓展）
#【raise】抛出异常，抛出异常后，所在函数后面的代码不再执行

# x = 10
# if x > 5:
#     raise Exception(f'x不能大于5, x的值为{x}')



# #5.代码调试debug    （进阶）

# #（1）错误追踪

# def a():
#     return 1/0

# def b():
#     a()

# def c():
#     b()

# c()


#(2)debug调试

# def add(a,b):
#     c = a+b
#     return a+b

# def divid(a,b):
#     d = float(a)/b 
#     #f = open("test6.txt","r")
#     return d

# def test():
#     i = 10
#     j = 5
#     sum = add(i,j)
#     div = divid(i,j)
#     print(sum,div)

# test()





