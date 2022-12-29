# #1.读取一个python源码文件，显示除了以#号开头的行以外的所有行。并打印输出#号开头的行数。

# num = 0
# f = open("text6.py","r",encoding="utf-8")

# for line in f.readlines():
#     if line.startswith("#"):
#         num += 1
#     else:
#         print(line,end="")  
# print(num)
# f.close()



# 2.写一个加法计算器。提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获异常，并打印一条友好的错误消息。应用异常处理和循环语句，直到用户输入”N“结束程序。

# > 对编写的程序测试：先输入两个数字，再输入一些文本而不是数字。
# while True:
#     try:
#         a = int(input("请输入数字"))
#         b = int(input("请输入数字"))
#         c = a + b
#         # if a == "N" or b == "N":
#         #     break
#     except ValueError:
#         print("输入错误，请输入数字")

#     else:
#         if a == "N" or b == "N":
#             break


# while True:
#     try:
#         a = int(input("请输入数字"))
#         b = int(input("请输入数字"))
#         c = a + b 
#         print(c)
#     except ValueError:
#         print("输入错误，请输入数字")
#     flag = input("是否还要继续")
#     if flag == "n" or "N":
#         break    



# 3.有文件 t1.txt 里面的内容为

# >   1,吴彦祖,22,13812346543,警察
# >
# >   2,金城武,23,13698763214,学生
# >
# >   3,彭于晏,18,13565478921,运动员



# 利用文件操作，将其构造成如下数据类型。输出到文件t2.txt中。

# [

# ​    {'id':'1','name':'吴彦祖','age':'22','phone':'13812346543','job':'警察'},

# ​    {'id':'2','name':'金城武','age':'23','phone':'13698763214','job':'学生'},

# ​    ... ...

# ]

# f = open("text7.txt","r",encoding="utf-8")
# list2 = ["id","name","age","phone","job"]
# list1 = []

# a = f.readlines()
# for i in a:
#     i = i.strip("\n")
#     word = i.split(",")
#     dict1 = {}  
#     for num,j in enumerate(word):        
#         dict1[list2[num]]=j
#     list1.append(dict1)   
# print(list1)         
# f.close()



#【综合练习】
print("*"*20)
print("操作编码\t","操作")
print("[0]\t","注册")
print("[1]\t","登录")
print("*"*20)
initial = input("请输入你要进行的操作编码：")
if int(initial) == 0:
    str1 = "注册"
    print(f"{str1:-^20}")
    i = 0
    while i<2:
        username = input("请输入用户名:")
        if username != "abc":
            i=2
        elif username.isalnum() and ("-" in username):
            print("用户名只能为字母、下划线和数字")        
        elif username=="abc":
            print("用户名已注册")
            continue
        

    a = 0
    while a <1:
        password = input("请输入密码:")
        if len(password)>=8:
            continue
        elif password.isalnum():
            b=0
            while b<1:
                password2 = input("请再次输入你的密码")
                if password != password2:
                    print("密码不一致")
                else:
                    print("注册成功")  
                    b=1  
            a=1
        else:
            print("密码不能超过8位，密码只能为数字或大小写字母")
    f = open("user.txt","w",encoding="utf-8")
    f.write(f"{username}:{password}")
    f.close()
    


elif int(initial) == 1:
    list=[]
    str = "登录"
    print(f"{str:-^30}")
    userName = input("请输入用户名:")
    file = open("blacklist.txt","r",encoding="utf-8")
    a=file.readlines()
    for k in a:
        k = k.strip("\n")
        list.append(k)

    if userName in list:
        print("黑名单用户，禁止登陆")
    else:
        n = 0
        while n<3:
            passWord = input("请输入密码:")       
            if passWord=="5004":
                break
            else:
                print("密码不正确")           
                n +=1
        else:
            print("禁止登陆，请联系管理员")
            file = open("blacklist.txt","a+",encoding="utf-8")
            file.write(f"{userName}\n")
            file.close()        
else:
    print("请输入0或1")








