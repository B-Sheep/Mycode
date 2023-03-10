#1.算术运算符

# #(1)整数+ - * /
# print("10 + 23 =",10+23)
# print("10 + 23 =",10-23)
# print("10 + 23 =",10*23)
# print("10 + 23 =",10/23)


# #(2)浮点数+ - * /
# #对大多数实数，计算机都无法精确存储。 这造成误差。
# #在用计算机解决实际问题时，要考虑上述误差的积累


# print("0.1+0.1=", 0.1+0.1 )
# print("0.1-0.1=", 0.1-0.1 )
# print("0.1*0.1=", 0.1*0.1 )    #计算机无法精确存储0.01，存储了它的近似值。
# print("0.1/0.1=", 0.1/0.1 )

# print("0.3 == 3*0.1\t",0.3 == 3*0.1)

# a = 0.2
# b = 0.1
# print("a+b=",a+b) #计算机无法精确存储0.3。  存储了它的近似值。


# #(3)幂运算 **
# c = 2 ** 10
# print("2**10=",2**10)

# #(4)整数除法//
# a = 4/2          #除法，默认是小数
# print(a,type(4/2))


# a = 7//2       #取整，向下取最接近的整数
# print(a,type(7//2))

# print("7//2=",7//2)
# print("-7//2=",-7//2)



# #(5)模运算 %

# b = 7%2       #取余数
# print(b,type(b))



# #(6)divmod() 同时获得商和余数

# d,e = divmod(7,2)
# print(d)    #商
# print(e)    #余数




#2.比较运算符
# a = 3
# b = 4

# print(a == b)     #表示a和b的值是否相等，用两个等号
# print(a != b)
# print(a > b)
# print(a > b)
# print(a >= b)
# print(a <= b)




#3.赋值运算符
a = 3
b = 4
a = a + b
#a += b    #注意：+= 是一个符号，中间没有空格
print(a)




#4.位运算符

a = 60
b = 13

print(bin(a))
print(bin(b))


a = 0b111100
b = 0b1101

#按位与
print("a & b",a&b)   #12,1100
'''
a      00111100
b      00001101
RESULT 00001100
'''

#按位或
print("a | b",a|b)    #61,00111101
'''
a      00111100
b      00001101
RESULT 00111101
'''

#按位异或
print("a ^ b",a^b)  #49,  00110001
'''
a      00111100
b      00001101
RESULT 00110001
'''


#按位非~n, 结果为-(n + 1)
print("~a",~a)      #-61, 11000011
'''
a      00111100
RESULT 11000011
'''


#向左位移 n<<m  ,表示n乘以2的m次幂
print("a<<2",a<<2)   #240,   11110000
'''
a      00111100
RESULT 11110000
'''
#向右位移 n<<m  ,表示n除以2的m次幂
print("a >> 2",a >> 2) #15, 00001111
'''
a      00111100
RESULT 00001111
'''





