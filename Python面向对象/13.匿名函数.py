#语法： 
#       lambda 参数 ：表达式
#（1）无参数的lambda表达式
# func = lambda:"这是一条消息"
# print(func())           #有返回值



#不推荐
# func = lambda:print("这是一条消息")
# print(func())           #没有返回值


#(2)有参的lambda表达式
#定义
# func = lambda x,y: x+y
# print(func)


#lambda表达式可以使用可变参数

# func = lambda *args: sum(args)
# print(func(1,2,3))



#lambda表达式可以使用关键字参数
func = lambda *args,**kwargs :f"{args},{kwargs}"
print( func(1,2,3,id =1,city = "北京"))



#(3)有条件判断的lanmbda

#三目表达式



#输出较大值
a = 1
b = 5

res = a if a>b else b          # 条件成立时的结果   if  条件表达式  else  条件不成立时的结果
print(res)


#判断是否为偶数
func = lambda x: f"{x}是偶数" if x%2 == 0 else f"{x}不是偶数"
print(func(21))







































































