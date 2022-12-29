#python的数据类型
#1.基本数据类型  2.字符串类型  3.列表类型  4.元组类型  5.集合类型  6.字典类型



#1.基本数据类型(整型、浮点型、布尔型、复数型)

#(1)整型（int）
#type()查看数值类型

# a10=100
# print(type(a10))

#二进制、八进制和十六进制表示法

# #十进制转为二进制
# print(bin(a10))
# #十进制转为八进制
# print(oct(a10))
# #十进制转为十六进制
# print(hex(a10))


#二进制转为十进制
# a2 = 0b1100100
# print(a2,type(a2))
# #八进制转为十进制
# a8 = 0o144
# print(a8,type(a8))
# 十六进制转为十进制
# a16 = 0x64
# print(a16,type(a16))



#(2)浮点型(float)

# a = 3.1415926
# print(a,type(a))

# a = 2.1e-2
# b = 5.67e3
# print(a,type(a))
# print(b,type(b))


#(3)布尔类型(bool)
# state = True    #True,表示“真”，“成立”，“正确”，“对的”
# state = False   #False，表示“假”，“不成立”，“不正确”，“错误的”
# print(state,type(state))


#state = True     #True在底层存储，本质是数字1；False在底层存储，本质是数字0.
#print(state+3)


#(4)复数类型（complex）
#复数 = 实数+虚数
#j：如果一个数的平方是-1，那么这个数就是j
# c = 3+4j
# print(c,type(c))

# c = complex(3,4)
# print(c,type(c))



#(5)自动类型转换
#不同数据类型进行运算时，结果默认更高精度类型
#精度从低到高
# bool→ int→ float→ complex


##(a)bool + int
# state = False
# print("bool+flaot:",state+3)

# #(b)bool+float
# print("bool+int:",True+3.2)    #结果默认为浮点型

# #(c)bool+complex
# print("bool+complex:",False + 2+3j)

# #(d)int + float
# print("int + float:",10+20.0)

# #(e)int+complex
# print("int+complex:",10 + 5+6j)

# #(f)float+complex
# print("float + complex:",3.14 + 5+6j)


# #(6)强制类型转换
num1 = 10
num2 = 22.99
num3 = True
num4 = 4+5j
num5 = "567"
num6 = "a78"



# #int()
# res = int(num2)   #22
# print(res)
# res = int(num3)   #True为1 False为0
# res = int(num5)   #567
# print(res,type(num5))
# #res = int(num6)     #：报错
# print(res)

# #float()
# res = float(num1)    #10.0
# res = float(num3)    #0.0
# res = float(num5)    #567.0
# print(res)

# #complex
# res = complex(num1)  #10+0j
# res = complex(num2)  #22.22+0j
# res = complex(num3)  #1+0j
# print(res)




# #bool
# res = bool(num4)
# print(res)
# res = bool(num6)
# print(res)


#什么时候bool类型是false？(共10种)

a = 0
print(a,bool(a))

# a = 0.0            #浮点0
# a = 0j             #复数0
# a = False          #布尔False
# a = ''             #空字符串
# a = ()             #空元组
# a = []             #空列表
# a = set()          #空集合
# a = dict()         #空字典
# a = None           #空对象
print(a,bool(a))   