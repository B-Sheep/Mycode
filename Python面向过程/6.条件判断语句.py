#1.语法
#(1)单分支结构：  琼剧所有情况，分别执行
# light = "绿灯"

# if light == "绿灯":
#     print("绿灯行")
# if light == "红灯":
#     print("红灯停")



#(2)双分支结构：两种情况互斥。  如果...... 否则......
light = "绿灯"

if light == "绿灯":
    print("绿灯行")
else:
    print("停止，等待。。。")



#多分支结构：多种互斥情况。 如果。。。。：那么如果。。。。。：否则。。。
light = "绿灯"

if light == "绿灯":
    print("绿灯行")
elif light == "黄灯":
    print("黄灯，等待。。。")
else :
    print("停止")

#(4)嵌套分支结构：某情况中，包含更多情况。 条件嵌套

light = "红灯"
pedestrian = 1  
turn_round = 0

if light == "绿灯":
    if pedestrian == 1:
        print("礼让，等待。。。")
    else:
        print("绿灯行")
else:
    if turn_round == 1:
        print("可以调头。。。")
    else:
        print("停止，等待。。。")



