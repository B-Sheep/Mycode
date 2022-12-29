
#只可以运行一个表达式
# x = 10
# def func():        
#     y = 20
#     c = eval("x+y",{"x":1,"y":2},{"y":3,"z":4})     #先执行局部变量，如果没有再执行全局变量

#     print("c:",c)

# func()




#exec可以运行一个对象
# x = 10

# expr = """
# z = 30
# sum = x + y + z
# print(sum)
# """

# def func():
#     y = 20
#     exec(expr)
#     exec(expr,{'x':1,'y':2})
#     exec(expr,{'x':1,'y':2},{'y':3,'z':4})      #先执行局部变量，如果没有再执行全局变量


# func()


#import math      具体用法查文档
#ceil() 向上取整  例如：4.01 = 5
#floor() 向上取整
#sqrt()  开方
#modf()  将一个数值拆分为整数和小数两部分组成元组





#chice()  随机获取序列中的值(多选一)[返回列表]
#sample(容器类型,选几个)  随机获取序列中的值(多选多)[返回列表]


import calendar
#w日期间的宽度，l日期间的高度，c月份间的间距，m一行显示几个月
# res = calendar.calendar(2022,w=2,l=2,c=20,m=3)
# print(res)

#month() (年份，月份，w日期间的宽度，l日期间的高度)
# res = calendar.month(2022,12,w=2,l=2)
# print(res)

#isleap()检查是否是闰年
# res = calendar.isleap(2022)
# print(res)          #输出：False

#monthrange()   获取某年某月的信息  返回：(第一是星期几，共多少天)其中周一是0
#res = calendar.monthrange(2022,12)

#weekday() 某年某月某日是星期几
#res = calendar.weekday(2022,12,6)

#timegm()   将时间元组转化为时间戳 
#ttp = (2022,12,25,125,45,35,0,0,0)
#res = calendar.weekday(ttp)




