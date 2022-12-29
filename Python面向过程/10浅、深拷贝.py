# num1 = [1,2,3]
# num2 = num1
# num1.append(4)
# print(num1,id(num1))
# print(num2,id(num2))



#浅拷贝
num1 = [10,[2,3]]
num2 = num1.copy()
num1.append(4)
# num1[0] = 8
num1[1].append(100)
print(num1,id(num1))
print(num2,id(num2))
print("num1[0]:",num1[0],id(num1[0]))
print("num2[0]:",num2[0],id(num2[0]))
print("num1[1]:",num1[1],id(num1[1]))
print("num2[1]:",num2[1],id(num2[1]))


#深拷贝
# import copy

# num1 = [10,[2,3]]
# num2 = copy.deepcopy(num1)
# print(num1,id(num1))
# print(num2,id(num2))
# num1.append(4)
# num1[0] = 8
# num1[1].append(100)
# print(num1,id(num1))
# print(num2,id(num2))

#小结:
#浅拷贝：只能copy列表的一级元素，复制了嵌套的可变数据类型的地址
#深拷贝：能够copy列表所有层级的元素，复制了嵌套的可变数据类型元素
