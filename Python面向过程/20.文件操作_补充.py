#4.访问模式

#当文件不存在时，w和a会新建文件夹
#r会报错
# f = open("test4.txt","a",encoding="UTF-8")
# f.write("IT私塾")
# f.close()


# #r+   可读可写
# f = open("test4.txt","r+",encoding="UTF-8")
# f.seek(0,2)
# # data = f.read()
# # print(data)

# # f.seek(0)
# f.write(" 学以致用")

# f.close()


# #5.二进制文件操作    (图片、音乐、视频)

# fin = open("123.jpg",mode="rb")
# fout = open("123_copy2.jpg",mode="wb")

# data = fin.read(100)
# print(data,type(data))

# while True:
#     data = fin.read(100)
#     if data != b"":
#         fout.write(data)
#     else:
#         break
# fin.close()



#6文件写入过程：
#数据-->  缓冲区(内存中)-->  文件中（硬盘上） 

# f.open("test5.txt",mode="w+",encoding="utf-8")
# f.write("IT私塾")
# f.flush()
# while True:
#     pass

# f.close


# #truncate  截断
# f = open("test5.txt",mode="w+",encoding="utf-8")
# for i in range(5):
#     f.write("IT私塾"+str(i)+"\n")
# f.close()


# f = open("test5.txt",mode="r+",encoding="utf-8")
# # f.seek(24)
# # f.truncate()
# f.truncate(8)
# f.seek(0)
# print(f.read())
# f.close()



#文件对象，是一个可迭代对象
f = open("test5.txt","r",encoding="utf-8")

for line in f:
    print(line)

f.close()


# #文件对象属性和状态
# f = open("test5.txt","r")
# print("文件名：",f.name)
# print("文件打开的模式：",f.mode)
# print("文件可写：",f.writable())
# print("文件可读：",f.readable())











