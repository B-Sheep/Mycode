#作用：简化代码
#1.列表推导式

#（1）循环模式
#语法：[变量表达式 或 有返回值的函数 for 变量 in iterable

#变量表达式
# res = [i*i for i in range(1,11)]
# print(res)


# res = [pow(i,2) for i in range(1,11)]
# print(res)


#自定义函数(需要有返回值)
# def getSquare(x):
#     return f"{x}的平方是{x**2}"

# res = [getSquare(i) for i in range(1,11)]
# print(res)


#构建一个列表

# poker = [i for i in range(2,10)] + list("JQKA")
# print(poker)



#(2)筛选模式

#30以内被3整除的数字

res = [i for i in range(0,31) if i%3 == 0]
print(res)



#(3)多重循环
#会用在矩阵计算，结果筛选与匹配等场合

#打印九九乘法表

# res = [f"{i}*{j} = {i*j}" for i in range(1,10) for j in range(1,i+1)]
# print(res)

def get99(i,j):
    print(f"{i}*{j} = {i*j}",end="")
    if i == j:
        print()

res = [get99(i,j) for i in range(1,10) for j in range(1,i+1)]
print(res)



#2字典推导式

city = ["北京","上海","广东","四川"]
abbr = ["京","泸","粤","川"]

dic = {city[i]:abbr[i] for i in range(len(city))}

print(dic)



#(3)集合推导式
#100以内所有偶数

print(i for i in range(2,101,2))




