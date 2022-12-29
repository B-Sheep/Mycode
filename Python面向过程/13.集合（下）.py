#3.集合的运算：交，差，并，反交
#在对集合做运算时，不会影响原来的集合，而是返回一个运算结果
#创建两个集合

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

# #交集运算（&或者intersection）
# result = s1 & s2
# result = s1.intersection(s2)
# print("result=",result)
# print("result=",result)


# #并集运算（|或union）
# result = s1 | s2
# result = s1.union(s2)
# print('result=',result)


# #差集（- 或 difference）
# result = s1 - s2             #{1,2}          #保留的是被减数的那部分
# result = s1.difference(s2)    
# result = s2 - s1            #{6，7}
# print('result=',result)


# #异或集 或称作 对称差集   (^ 或 symmetric_difference)
result = s1 ^ s2
# result = s1.symmetric_difference(s2)
print('result=',result)


#子集或超集
#<=检查一个集合是否是另一个集合的子集
#如果a集合中的元素全部都在b集合中出现，那么a集合就是b集合的子集，b集合是a集合的超集

# a = {1,2,3}
# b = {1,2,3,4,5,6}

# result = a<=b
# print(a.issubset(b))
# print(b.issuperset(a))
# reslut = {1,2,3} <= {1,2,3}

# print('result=',reslut)


#<检查一个集合是否是另一个集合的真子集
#如果超集b中含有子集a中所有元素，并且b中还有的元素，则b就是a的真超集，a是b的真子集

# result = {1,2,3} < {1,2,3}     #False
# print('result=',result)
# result = {1,2,3} < {1,2,3,4,5}   #True
# print('result=',result)


# #不相交isdisjoint
# result = a.isdisjoint(b)    #不相交：True；  相交：False


#应用：
#列表去重：
# num = [1,1,2,2,3,3,4,4]
# s = set(num)                    #注意：顺序可能会被打乱
# res = list(s)
# print(res,type(res))
