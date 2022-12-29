#1.for循环
# for i in range(5):
#     print(i)



# for i in range(0,5):
#     print(i)



# for i in range(0,13,3):
#     print(i)


#range()  函数返回一个可迭代的对象
#range(start,stop,step)
'''
start:计数从start开始。默认是从0开始。例如range(5)等价于range(0,5);
stop:计数到stop结束，但不包括stop。例如：range(0,5)是[0,1,2,3,4]没有5
step：步长默认为1.例如range(0,5)等价于range(0,5,1)
'''


# for i in range(-10,-101,-30):
#     print(i)



#字符串

# city = "yunfu"
# for i in city:
#     print(i,end="\t")



#元组
# a = (10,20,30)
# for i in a:
#     print(i)



#列表
# n = ["aa",'bb',"cc"]
# for i in n:
#     print(n)



# m = ['aa','bb','vv','dd']
# print(len(m))
# for i in range(len(m)):
#     print(f"{i}位置，元素{m[i]}")




#2.while循环
# while True:                          #死循环
#     s = input("请输入内容")
#     print("您输入了：",s)


# i=0
# while i<5:
#     print(i)
#     i += i           #i = i+1

#计算1-100自然数相加的和
# total = 0         #保存求和结果
# n=1               #当前循环的数字
# while n<=100:
#     total += n
#     n += 1
# print(total)



#求1-100的偶数和
#循环语句和条件判断语句的综合使用
#写法1：
# total = 0         #保存求和结果
# n=100               #当前循环的数字

# while n>0:
#     if n%2 ==0:
#         total += n
#     n-=1
# print("1-100的偶数和:",total)


#写法2   (更简单)
# total = 0         #保存求和结果
# n=100               #当前循环的数字

# while n>0:
#     total += n
#     n -= 2
# print("1-100的偶数和:",total)



#扩展：使用内置函数，快速实现1....100的和
#print(sum(range(101)))




#3.break,continue,pass

# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         break             #结束整个while循环
#     print(i)



# i=0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue       #结束本次循环
#     print(i)
#     print("*******")


#while和else结合使用(了解)

# for i in range(3):
#     cmd = input("请输入指令:")
#     print("您输入了",cmd)
# print("您输入了3次命名")


# for i in range(3):
#     cmd = input("请输入指令:")
#     if cmd == "exit":
#         break
#     print("您输入了",cmd)
# else:                       #else语句在循环被中断的情况下不执行
#     print("您输入了3次命名")



#4.循环的嵌套
a = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]

# for j in a:
#     print(j,end="、")
# print()


for i in range(4):
    print(f"第{i+1}周:")
    for j in a:
        print(j,end="、")
    #print(i)
    print()

        