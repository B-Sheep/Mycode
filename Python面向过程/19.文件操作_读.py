#2.文件操作的基本流程：读（read）           把数据从文件中取到程序中
# f = open("test2.txt","w",encoding="UTF-8")
# #f.write("itsishu\n"*10)
# f.write("IT私塾,高效学习")
# f.close()


# f = open("test2.txt","r",encoding="UTF-8")
# #data = f.read()              #没有指定读取的字符数，表示读取文件中所有的数据
# data = f.read(2)
# print("读取到的文件内容：",data)
# data = f.read(4)             #文件读取过程中的指针的定位会逐步指定字符数
# print("读取到的文件内容：",data)
# f.close()


# #【readline】    读取一行，返回一个字符串

# f = open("test2.txt","r",encoding="utf-8")

# while True:
#     content = f.readline()
#     if content:
#         print(f"{content}",end="")
#     else:
#         print("content:",content,type(content))
#         break

# f.close()



#【readlines】       读取多行，一次性读取全部文件为列表，每行一个字符串元素
# f = open("test2.txt","r",encoding="utf-8")
# i= 1
# for data in content:
#     print(f"{i}:{data}",end="")
#     i += 1


# for i, data in enumerate(content):
#     print(f"{1}:{data}",end="")

# f.close()



#【tell】返回指针当前所在的位置（指针所在位置前面的字节数）

# f = open("test3.txt","w",encoding="gbk")
# f.write("IT私塾，高效学习1")
# f.close()

# f = open("test3.txt","r",encoding="gbk")
# content = f.read(2)
# print(content)
# content = f.read(4)
# print(content)

# print("当前指针所在位置：",f.tell())

# #UTF-8中1个汉字3个字节，GBK中1个汉字为2个字节
# #同样是读取2个字符，UTF-8返回为8，GBK返回为6



# #【seek】定位文件读取的指针所在位置（字节）
# #seek(offset[,whence])
# # offset-------开始的偏移量，也就是代表需要移动偏移的字节数
# # whence：可选，默认值为0
# #         给offset参数一个定义，表示要从哪个位置开始偏移
# #         0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起 

# f = open("test3.txt","w",encoding="gbk")
# f.write("IT私塾，高效学习1")
# f.close()

# f = open("test3.txt","r",encoding="gbk")
# content = f.read(2)
# print(content)
# f.seek(6)           #指定的是字节数
# content = f.read(3)
# print(content)
# print("当前指针所在位置：",f.tell())

