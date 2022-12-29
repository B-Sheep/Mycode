#递归函数 （进阶）
#基本概念
#打印从100到1的整数

# for i in range(100,0,-1):
#     print(i)



# def printNum(n):
#     print(n)           #执行的运算
#     if n == 1:         #最终结束的条件
#         return         #返回的数值
#     printNum(n-1)      #printNum(99)    #调用自身函数

# printNum(100)





#分析为函数表达式：
#f(1) = 1
#f(n) = f(n-1)*n

# def dec(n):
#     if n <= 1:
#         return 1
#     return dec(n-1)*n

# print(dec(5))        #5*4*3*2*1



#斐波那契数列
#0 1 1 2 3 5 8 13 21 34 55 889 144..........

#f(n)=n                  n<=1
#f(n)=f(n-1) + f(n-2)    n>1 

# def feb(n):
#     # if n<=1:
#     #     return n
#     # else:
#     #     return feb(n-1) + feb(n-2)
    
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return feb(n-1) + feb(n-2) 

# print(feb(10))


def feb(n):
    if n <= 1:
        return n
    res = 0           #始终存储的和
    feb0 = 0          #用于存储下一次运算的内容
    feb1 = 1          #用于下一次运算的和
    for i in range(2,n+1):
        print(f"res:{res},feb0:{feb0},feb1:{feb1}")
        res = feb0 + feb1
        feb0 = feb1
        feb1 = res
    return res

print(feb(10))

























































