#功能：不改变现有函数的前提下，扩展函数功能
#语法：@

# def check(func):

#     def checkAndlog():
#         print("函数运行前：权限校验...")
#         func()
#         print("函数运行后：权限校验...")

#     return checkAndlog

# @check
# def printInfo():
#     print("我是人啊人")


# @check
# def test():
#     print("test...")


# printInfo()
# test()


# newFunc = check(printInfo)
# newFunc()




# #3.装饰器的嵌套
# def zsA(func):
#     def resFunc():
#         print("zsA执行前...")
#         func()
#         print("zsA执行后...")
#     return resFunc


# def zsB(func):
#     def resFunc():
#         print("zsB执行前...")
#         func()
#         print("zsB执行后...")
#     return resFunc

# @zsB
# @zsA
# def test():
#     print("这是人啊人")

# test()





#4.带参数的装饰器
 
      
# def tool(func):
#     def log(*args,**kwargs):
#         print(f"登录日志")
#         state= func(*args,**kwargs)
#         return state
#     return log
# @tool
# def login(name,pwd):
#     print(f"{name}:{pwd}")
#     if name == "admin" and pwd == 123456:
#         return "登录成功"
#     return "登陆失败"

# @tool
# def test():
#     print("test....")


# test()
# login("admin",123456)


#7.使用面向对象的方式定义装饰器
#call

class Mytool:
    def __call__(self,func):
        return self.tool2(func)

    def tool1(func):
        def log():
            print("log...")
            func()
        return log

    def tool2(self,func):
        def check():
            print("check...")
            func()
        return check



#调用方法一
# @Mytool.tool1
# def test():
#     print("test...")

# test()


#调用方法二
@Mytool()
def test():
    print("test....")

test()





























