#1~2练习

#1
#(1)
# print("莫道谗言如浪深,\n莫言迁客似沙尘。\n千淘万漉虽辛苦,\n吹尽狂沙始到金。")


#(2)

# a = "莫道谗言如浪深,\n"
# b = "莫言迁客似沙尘.\n"
# c = "千淘万漉虽辛苦,\n"
# d = "吹尽狂沙始到金."
# print(f"{a}{b}{c}{d}")


#(3)

# poem = "{a}\n{b}\n{c}\n{d}".format(a="莫道谗言如浪深,",\
# b="莫言迁客似沙尘.",c="千淘万漉虽辛苦,",d="吹尽狂沙始到金.")
# print(poem)

#(4)
# poem1="{0}{1}{2}{3}".format("莫道谗言如浪深,\n","莫言迁客似沙尘.\n",\
#     "千淘万漉虽辛苦,\n","吹尽狂沙始到金.")
# print(poem1)



#2
#(1)
# digit = int(input('请输入数字'))
# if digit>68:
#     print("猜测结果大了")
# elif digit <68:
#     print("猜测结果小了")
# else:
#     print("猜测结果正确")




#3
#(1)
# username = input("请输入用户名：")
# if username == "管理员":
#     print("admin")
# else:
#     print("输入有误")


#4
#(1)

# b = int(input("请输入一位整数:"))
# if b%2==0:
#     print("偶数")
# else:
#     print("奇数")


#5
#(1)
# weight = float(input('请输入体重--kg:'))
# height = float(input('请输入身高--m:'))
# BMI = weight/(height**2)
# if 28<=BMI<32 :                #注意边界值
#     print("肥胖")
# elif 25<=BMI<28:
#     print('过重')
# elif 18.5<=BMI<25:
#     print('正常')
# elif BMI<18.5:
#     print('过轻')
# else:
#     print("输入错误")


#(2)
# weight = float(input('请输入体重--kg:'))
# height = float(input('请输入身高--m:'))
# BMI = weight/(height**2)
# if BMI<18.5:
#     print("过轻")
# elif BMI<24.99:
#     print("正常")
# elif BMI<=28:
#     print("过重")
# elif BMI<32:
#     print("肥胖")
# else:
#     print("请重新上称")




#6
#(1)
# x = float(input("请输入数字"))
# y = float(input("请输入数字"))
# if x>0 :
#     if y>0:
#         print("第一象限")
#     elif y<0:
#         print("第四象限")
#     elif y==0:
#         print("在x轴上")
# elif x<0:
#     if y>0:
#         print("第二象限")
#     elif y<0:
#         print("第三象限")
#     elif y==0:
#         print("在x轴上")
# elif x==0:
#     if y==0:
#         print("在原点上")
#     elif y>0 :    
#         print("在y轴上")
#     elif y<0 :    
#         print("在y轴上")
# else:
#     print("输入错误")


                                 
#(2)                                也可以用 and  or !=(不等于)  的写法
# x = float(input("请输入数字："))
# y = float(input("请输入数字："))
# if x>0 and y>0:
#     print("第一象限")
# elif x>0 and y<0:
#     print("第四象限")
# elif x<0 and y>0:
#     print("第二象限")
# elif x<0 and y<0:
#     print("第三象限")
# elif x==0 or y==0:
#     if x==0 and y!=0:
#         print("在y轴上")
#     elif x!=0 and y==0:
#         print("在x轴上")
#     elif x==0 and y==0:
#         print("在原点上")
# else:
#     print("输入错误")




#7
#(1)
# a = [3,4,5]
# b = [6,7,8]
# c = [9,10,11]
# d = [12,1,2]
# 月份 = int(input("请输入月份:"))
# if 月份 in a:
#     print("春季")
# elif 月份 in b:
#     print("夏季")
# elif 月份 in c:
#     print("秋季")
# elif 月份 in d:
#     print("冬季")
# else:
#     print("输入有误")      


#(2)
# month = int(input("请输入月份："))
# if month ==3 or 4 or 5:
#     print("春季")
# elif month ==6 or 7 or 8:
#     print("夏季")
# elif month ==9 or 10 or 11:
#     print("秋季")
# elif month ==12 or 1 or 2:
#     print("冬季")
# else:
#     print("输入有误")



#8
#（1）

# a = [1,3,5,7,8,10,12]
# b = [2]
# c = [4,6,9,11]
# year = int(input("请输入年份："))
# month = int(input("请输入月份："))
# if month in a:
#     print("本月有31天")
# elif month in b:
#     print("本月有28天")
# elif month in c:
#     print("本月有30天")
# else:
#     print("输入有误")


#(2)                             #正确做法
year = int(input("请输入年份："))
month = int(input("请输入月份："))
if month ==2:
    if year%4==0 and year%100!=0 or year%400==0:
        print("本月有29天")
    else:
        print("本月有28天")
elif month in [4,6,9,11]:
    print("本月有30天")
elif month in [1,3,5,7,8,10,12]:
    print("本月有31天")
else:
    print("输入有误")



#9
#(1)
# year = int(input("请输入年份:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("闰年")
# else:
#     print("不是闰年")