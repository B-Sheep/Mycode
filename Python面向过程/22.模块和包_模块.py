#1.模块的导入

#导入模块(import)

# import math

# print(math.pi)
# print(type(math))


# #导入自己定义的模块
# import myModule1
# myModule1.add(3,2)  #使用  模块名.函数名  进行调用



#2.模块的运行

#脚本方式


#模块方式
# import myModule2           #导入自定义模块是，被导入模块的“可执行语句”会立即执行
# import myModule2           #你执行多次import，一个模块只会被导入一次




#3.模块搜索路径

#（1）内置模块（例如math）
#（2）当前模块所在的目录
#（3）环境变量 PYTHONPATH (默认包含python的安装路径)
#（4）Python安装路径下的lib文件夹
#（5）lib文件夹下的site-packages文件夹（第三方模块）
#（6）实验室.path.append()追加的目录

# import myModule3

# import sys
# print(sys.path)




#【扩展】指定搜索路径

#以后代码需要放到其他电脑上运行，如何保证仍然能够找到这个文件夹呢

#绝对路径：  从盘符出发的路径
#相对路径    不是从盘符出发的路径

# import os

# print(__file__)

# print(os.path.dirname(__file__))      #获取指定文件所在的目录（文件夹）



# #4.其他导入模块的方式
# #（1）从模块中引入指定的函数       （from...import...）

# from myModule1 import add,divid
# print(add(3,2))  #直接使用  函数名（）  进行调用
# print(divid(3,2))



#(2)一次性引入模块中全部函数
from myModule1 import *
print(add(3,2)) 
print(divid(3,2))
print(multiply(3,2))


#(3)import 和  from.... import.....的区别 

from myModule1 import *

def add(x,y):
    return f'10*{x}+10{y}={10*(x+y)}'

#from myModule1 import *

print(add(3,2))


#(4)使用别名，解决变量或函数重名问题

from myModule1 import add as m1add

def add(x,y):
    return f'10*{x}+10{y}={10*(x+y)}'


print(add(3,2))
print(m1add(3,2))


#给模块起别名。简化书写
import myModule1 as m
print(m.add(3,2))












































