# #1.求1-100所有数的和
# #(1)
# a = 0
# for i in range(101):
#     a += i 
# print(a)    

# #(2)
# i = 1
# z = 0
# while i<101:
#     z += i
#     i += 1
# print(z)



# #2.输出1-100内所有的奇数/偶数（循环+条件语句）
# #(1)
# for i in range(1,101):
#     if i%2==0:
#         print(f"{i}是偶数")
#     else:
#         print(f"{i}是奇数")

# #(2)
# i = 1
# while i <100:
#     if i%2==0:
#         print(f"{i}是偶数")
#     else:
#         print(f"{i}是奇数")
#     i += 1



# #3.for循环打印金字塔
# #(1)
# for j in range(5):
#     for i in range(j+1):
#         print("*",end="")
#     print()

# #(2)
# for i in range(5):
#     for j in range(i*2+1):
#         print('*',end="")
#     print()

# #(3)
# for i in range(5):
#     p = "*"*(i*2+1)
#     print(p.center(11," "))


# #4.for 循环打印99乘法表
# for j in range(1,10):
#     for i in range(1,j+1):
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()



# #5.完成猜字游戏
# import random
# num = random.randint(1,101)

# for i in range(10):
#     a = float(input("请输入一个数字"))
#     if a>num:
#         print("大了")
#         continue
#     elif a<num:
#         print("小了")
#         continue
#     elif a==num:
#         print("恭喜中奖")
#         break
# else:
#     print("猜测结束")



# #6.用户输入一个整形数，求该数的阶乘
# n = int(input("请输入一个自然数："))
# z = 1

# if n>=1:
#     for i in range(1,n):
#         z = z *i  
#     print(z)
# elif n<1:
#     print("该数不是自然数")
    
        
        
# #7.求1-2+3-4+5 ……99的所有数的和
# a=0
# b=0
# for i in range(1,100):
#     if i%2==0:
#         i = -i
#         a += i
#     else:
#         b += i
# print(a+b)     




# #【拓展练习】
# #(1)猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃\
# #了一个，第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天\
# #早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# a = 1
# for i in range(1,10):
#     a = (a+1)*2
# print(a)


# #(2)一球从100米高度自由落下，每次落地后反跳回原高度的一半；\
# #再落下,求它在第10次落地时，共经过多少米？第10次反弹多高？
# a = 100
# b = 100
# for i in range(10):
#     a = a/2
#     b = b+a
# print(a,b)



# #(3)有1、2、3、4个数字，能组成多少个\
# # 互不相同且无重复数字的三位数？都是多少？

# for i in range(1,5):
#     for j in range(1,5):
#         for h in range(1,5):           
#             if (i != j and h != j and i != h):
#                 print(f'{i}{j}{h}')


# #(4)一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.\
# # 编程找出1000以内的所有完数。
# a = 0
# for j in range(1,1000):
#     for i in range(1,j):
#         if j%i==0 :
#             a += i
#     if j==a:
#         print(j)
#     a = 0            


 
    
# # （5）输入两个数值：
# # 		求两个数的s和最小公倍数
# # 		最小公倍数=(num1 * num2) / 最大公约数   
            
# num1 = int(input("请输入一个整数:"))            
# num2 = int(input("请输入一个整数:"))
# a = num1           #修改后
# b = num2           #修改后
# while 1>0:
#     c = a%b          #修改后      
#     if c == 0:
#        print("最大公约数为：",b)
#        break
#     elif c != 0:
#         a = b 
#         b = c

        

# （8）用户登录需求：

# - 输入用户名和密码；

# - 判断用户名和密码是否正确（name=‘root’,passwd=‘123456’）,密码输入错误三次则会报错

# - 登录仅有三次机会，超过3次会报错
i = 0
while i <3:
    name = str(input("请输入用户名:"))
    if name == "root":
        j=0
        while j <3:          
            password = str(input("请输入密码:"))
            if password == "123456":
                print("登入成功")   
                break      
            else:
                print("密码错误")
                j += 1
        else:
            print("密码错误，账户已被锁定")
            break                 
    else:
        print("用户名输入错误")
        i+=1
else:
    print("用户输入三次机会已用完")












