#字典的定义   dictionary =》dict

# info = {}    #定义一个空字典
# info = {"name":'小爱同学',"age":18,"age":1,"gender":0,("aa",):[1,2]}
# print(info,type(info))


# #字典的访问
# info = {"name":'小爱同学',"age":18}
# print(info["name"])
# print(info["age"])

# print(info["gender"])   #直接访问，会报错：keyerror
# print(info.get("gender"))    #使用get方法，没有找到对应的键，默认返回：None

# print(info.get("gender","m"))    #没有找到的时候，可以设定默认值
# print(info.get("age","20"))      #已有的键的值不可以再设定默认值



# #使用列表创建字典【fromkeys】

# namelist = ["小爱","小心","小吴"]

# dic1 = {}.fromkeys(namelist)
# dic1 = {}.fromkeys(namelist,"pretty")
# dic1 = {}.fromkeys(namelist,["pretty","beautiful","gorgeous"])


# print(id(dic1["小爱"]),id(dic1["小心"]),id(dic1["小吴"]))
# print(dic1)



#增

# info = {"name":'小爱同学',"age":18}
# newID = input("请输入新的学号：")
# info["id"] = newID
# print(info["id"])
# print(info)


#删
#【del】
# info = {"name":'小爱同学',"age":18}
# del info["name"]
# print(info)

# info = {"name":'小爱同学',"age":18}
# del info      #删除字典对象
# print(info)


# #【clear】
# info = {"name":'小爱同学',"age":18}
# info.clear()
# print(info)


#【pop】  【popitem】
#info = {"name":'小爱同学',"age":18,"gender":"男"}
# 性别 = info.pop("gender")           #通过键，删除指定的键值对；会返回删除的键值对的值
# gender = info.pop("性别")          #删除一个不存在的键，会报错：keyerror
# gender = info.pop("性别","不存在")    #删除一个不存在的值，会报错：没有找到指定的值，可以返回默认值

# 性别 = info.popitem()     #删除最后一个键值对，返回的是：元组类型
# 性别 = info.popitem()     
# print(性别,info)


#改
#info = {"name":'小爱同学',"age":18}
#info.update({"id":1,"age":20})      #指定的键存在，更新；指定的键不存在，新增
#info.update(age=20,id=1)             #另一种写法，注意：键没有双引号，赋值用等号

#print(info)



#查
# info = {"name":'小爱同学',"age":18}

# for i in info:
#     print(i)

# print(info.keys(),type(info.keys()))       #得到所有的键(可迭代对象)，可以理解为：列表
# print(info.values(),type(info.values()))   #得到所有的值(可迭代对象),可以理解为：列表
# print(info.items(),type(info.items()))       #得到所有的项(可迭代对象)，可以理解为：每个键值对是一个元组

#遍历所有的键
# for key in info.keys():
#     print(key)

# for value in info.values():
#     print(value)


#遍历所有的键值对
# for key,value in info.items():
#     print(f"key={key},value={value}") 


#拓展：使用枚举函数，同时拿到列表中的下标和元素内容
# mylist = ["a","b","c","d"]    
# for i,x in enumerate(mylist):
#     print(i,x)