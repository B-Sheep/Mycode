#Python查找“名称”时，是按照LEGB规则查找的
#local--->Enclosed--->Global--->Built in


#L-----Local  
#E-----Enclosed   (一个函数包裹另一个函数，闭包)
#G-----Global
#B-----Builtin   #内置函数





#nonlocal
# def outer ():
#     a = 5
#     def inner():
#         nonlocal a  #把第一层函数的a的值修改了
#         a = 2
#         print("inner:",a)
#     inner()
#     print("outer:",a)  #2

# outer()    #2




a = 200
def outer ():
    a=50
    def inner():
        # a=80
        def inner_inner():
            nonlocal a                #逐层往上找a的值，但是不会去找全局的a的值
            print("inner_inner:",a)
        inner_inner()
        print("inner:",a)
    inner()
    print("outer:",a)  

outer()    #2




