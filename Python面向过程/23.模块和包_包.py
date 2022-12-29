#包
#1.包的概念
#2.包和模块
#3.包内模块间导入


#1.包的概念 
#__init__.py  包的标识，不能删除

# import my_package.packageA.moduleA
# #应用时，必须使用全名
# print(my_package.packageA.moduleA.info)
# my_package.packageA.moduleA.testA()


# from my_package.packageA import moduleA
# print(moduleA.info)
# moduleA.testA()


# #也可以直接导入变量或函数
# from my_package.packageA.moduleA import testA,info
# print(info)
# testA()



# 2.包和模块的导入
# (1)本质上就是引入了__init__.py文件

# import my_package.packageA

# #可以通过引入包，一次性引入包下面的所有模块
# my_package.packageA.moduleA.testA()
# my_package.packageA.moduleAA.testAA()



# from my_package.packageB.moduleBB import *
# print(a)
# print(b)
# #print(c)       #访问c报错，因为__all__中不允许访问

# #注意，只对from...import* 这种引入形式有效


#3.包内模块间导入
#使用 .  .. 导入项目下的模块
#在执行相对导入之前，父模块必须显示地绝对导入


#绝对导入
import my_package.packageC.moduleC


















