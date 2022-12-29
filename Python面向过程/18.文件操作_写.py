#1.文件操作的基本流程：写（write） 把数据存到文件中

# f = open("test.txt","w")   #打开文件，w模式（写模式），文件找不到就创建
# f.write("Hello World")
# f.close()                 #关闭文件


# #(1)相对路径和绝对路径
# #绝对路径：从盘符开始的路径
# #相对路径：相对当前源码所在的路径

# #绝对路径中为了不让\产生转义效果，需要在路径前面添加字母r
# #否则需要再将每个\进行转义，写为\\
# f = open(r"C:\Users\Palpitation\Desktop\practice\Training\test.txt","w")   
# f.write("IT sishu")
# f.close()


#(2)中文编码问题

#默认使用记事本打开：正常显示  （windows系统默认使用GBK字符集）
# f = open(r"C:\Users\Palpitation\Desktop\practice\Training\test.txt","w")   
# f.write("IT私塾")
# f.close()


# f = open("test.txt","w",encoding="UTF-8")   
# f.write("IT私塾")
# f.close()


#(3)【writelines】一次性写入多行

f = open("test.txt","w",encoding="UTF-8")   
#f.write("IT私塾\n高效学习\n学以致用\n")

# content = ["IT私塾\n","高效学习\n","学以致用\n"]
# f.writelines(content)

content = ["IT私塾","高效学习","学以致用"]
f.write("\n".join(content))

f.close()

























