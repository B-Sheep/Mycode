#格式化
#% 操作符       （最原始）
#format()函数   （Python2.6之后）
#f-strings      （Python3.6之后） 推荐



# #%方式 
# #1.顺序填充
# age = 18
# country = "中国" 
# print('我的年龄是%d岁'%age)
# print("我的国籍是%s"%country)

# print("我的年龄是%d岁,我的国籍是%s"%(age,country))


# #2.索引填充
# str = "{0},{1},{0}!".format("你好","世界")


# #3.关键字填充
# str = "姓名:{name},年龄:{age}".format(age=18,name="小爱同学")
# print(str)



# #4.通过字典设置参数，**展开map集合
# info = {"name":"小爱同学","age":18}
# str = "姓名:{name},年龄:{age}".format(**info)
# print(str)


# #5.利用列表的索引设置参数
# list = ["IT私塾","www.itsishu,cn"]
# str = "网站名称:{0[0]},网址:{0[1]},时间:{1}".format(list,2020)
# print(str)

# #数字
# print("圆周率:{:+.2f}".format(3.1415926))
# print("{:,}".format(10000000))
# print("{:.2e}".format(1000000))
# print("{:.2%}".format(0.25))



# str = "jqx"
# print("{:*>10}".format(str))
# print("{:￥<10}".format(str))
# print("{:#^10}".format(str))


# #3.f-strings

# name = "小爱同学"
# age = 3
# print(f"你好，{name}今年{age}岁了")



# str = "jqx"
# print(f"{str:*>10}")
# print(f"{str:￥<10}")
# print(f"{str:#^10}")


# #补充
# #任意表达式

# print(f"{2*10}")
# print(f"{'abc'.upper()}")


# #多行f-string

# teacher = "张老师"
# days = 3
# message = (f"{'请假条':_^15}\n"
#         f"{teacher}您好:\n"
#         f"我想请假{days}天，可以吗"

# )
# print(message)


# print(f"{{11}}")
# print()
# print("aaa","bbb","ccc",200)
# print("www","itsidhu","cn",sep=".")    #sep 可以用任意东西把字符串连接起来
print("hello",end=",")
print("world",end='\t')
# print("python",end="\n")
# print("end")




# #输入

# password = input("请输入您的密码：")
# print("用户输入的密码是：",password)


# a = float(input("输入:"))
# print(type(a))


# #类型转换

# b = "abc:" + str(100)
# print((type(str(100))))
# print(b)


# a =input("输入：")
# print("a的类型:",type(a))
# b = int(a)
# print("b的类型:",type(b))
# print(b+100)


# a = int(input("输入:"))
# print(a+100)