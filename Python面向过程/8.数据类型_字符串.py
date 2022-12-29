#1.字符串的定义
#python中没有字符类型，一个字符也是字符串类型
# word = "字符串"
# sentence = "这是一个句子"
# paragraph = """这是一个段落
# 可以写多行

# """
# print(paragraph,type(paragraph))
# print(word,type(word))
# print(sentence,type(sentence))



#2.转义字符
# my_str = "I'm a student"
# my_str = 'I\'m a student'
# print(my_str)



# path = "c:\temp\1.mp3"            #如果路径太长不太方便
# path = r"c:\temp\1.mp3"           #不想让转义字符生效
# print(path)           



#3.字符串切片(字符串的截取)
# str1 = "itsishu"
#正向索引：
#       0123456
#反向索引：
#      -7,...-2,-1
        
# print(len(str1))    #内置函数len()获取字符串长度
# print(str1[2])
# print(str1[2:5])     #截取字符串索引值为2~4的字符，不包括索引值为5的字符[2,5)\左闭右开
# print(str1[2:-1])    #截取字符串重索引值为2开始直到字符串结尾的前一个，-1的索引值表示最后一个
# print(str1[2:len(str1)])
# print(str1[:2])
# print(f"{str1}[:4]",str1[:4])


#[起始位置：结束位置：间隔位置]
# print(f"{str1}[0:7:2]:",str1[0:7:2])
# print(f"{str1}[-1:-6:-1]:",str1[-1:-6:-1])           #反向索引，倒序打印




#4.字符串拼接
# str1 = "ITsishu"
# str1 += "学以致用"
# print(str1 + "高效学习")

# print("_"*30)

# str2 = "这是一个很长的字符串，以至于一行写不完"\
#     "那就第二行接着写"\
#         "可以一直写下去,都算一个字符串"
# print(str2)




#5.字符串常用函数
#(1)字母转换
#capitalize 字符串首字母大写
# str1 = "itsishu"
# res = str1.capitalize()
# print(res)

# #title 每个单词的首字母大写
# str1 = "It si shu"
# res = str1.title()
# print(res)


# res = str1.istitle()      #判断每个单词的首字母是否大写
# print(res)


# #Upper 将所有字母变成大写
# str = "It Si Shu"
# res = str1.upper()
# print(res)


# #lower 将所有字母变成小写
# res= str1.lower()
# print(res)


# #swapcase 大小写互换
# res = str1.swapcase()
# print(res)



# #(2)统计与查找
# #count 统计字符串中某个元素的数量
# str1 = "it si shu"
# res = str1.count("IT")      #s为2;it为1；IT为0


# #find 查找某个字符串第一次出现的索引位置
# #find('字符串'，开始位置，结束位置)结束位置取不到，取到之前的一个值
# str1 = "IT私塾：高效学习，学以致用"
# res = str1.find("学")          #7.标点符号也算字符
# res = str1.find("学",8)        # 10
# res = str1.find("学",1,7)      #-1表示没有匹配到 [1,7)  左闭右开
# res = str1.find("学习")
# print(res)


# #index 与 find 功能相同 find找不到返回-1，index找不到数据直接报错
# res = str1.index("it")    #推荐使用find
# print(res)



# #(3)判断开头，结尾
# #startswith 判断是否是以某个字符或字符串开头
# #startswith('字符串',开始位置，结束位置)

# str1 = "IT私塾：高效学习，学以致用"
# res = str1.startswith("it")
# res = str1.startswith("学",10)
# res = str1.startswith("学以",10,12)
# print(res)


# #endswith  判断是否以某个字符或字符串结尾
# #endswith('字符串'，开始位置，结束位置) 
# res = str1.endswith("用")
# res = str1.endswith("学习",-9,-5)
# print(str1[-9,-5])
# print(res)



# #(4)分割与拼接
#split 按某字符会字符串分割成列表(默认从左到右按空格分割)
#str1 = "IT私塾 高效学习 学以致用"
#res = str1.split()
#str1 = "IT_私塾_高效_学习_学以_致用"
#res = str1.split("_",2)      #第二个参数是分割几次(从左到右)
#
# #rsplit  从右到左分割
# res = str1.rsplit("_",1)  #(从右到左)
# print(res)     #返回列表


# #join 按某字符将列表拼接成字符串(容器都可）
# listvar = ['IT私塾','高效学习','学以致用']
# res = "#".join(listvar)
# print(res)




# #(5)去掉与替换
# #replace 替换字符串(第三个参数选择替换的次数)
# str1 = "IT私塾 高效学习 学以致用"
# res = str1.replace(" ","/")
# print(res)
# #第三个参数为替换的次数
# res = str1.replace("学","练",2)
# print(res)

#strip
# str1 = "\r IT私塾  \t \n"
# print(str1)
# res = str1.strip()
# print(res)
# print("end")


# #lstrip(), 只去掉左侧的空白符
# res = str1.lstrip()
# print(res)
# print("end")

# #rstrip(), 只去掉右侧的空白符
# res = str1.rstrip()
# print(res)
# print("end")



#(6)判断类型
#isspace()字符串中只包含空白，则返回True,否则返回False
# res = "     "
# res = "\t  \r\n"
# print(res.isspace())


# #isalpha 字符串至少有一个字符并且所有字符都是字母则返回True， 否则返回False
# res = "abc"
# res = "123"
# res = "123.0"
# res = "$123"
# print(res.isalpha())


# #isalnum, 字符串至少有一个字符并且所有字符都是字母或数字则返回True， 否则返回False
# res = "abc"
# res = "abc123"
# res = "123.0"
# # res = "$123"
# print(res.isalnum())


#isdecimal()
#isdigit()
#isnumeric()



# #(7)长度、填充
# #len计算容器类型长度
# res = len("IT私塾")
# print(res)


# #center 填充字符串，原字符居中(默认填充空格)
# str1 = "IT私塾"
# res = str1.center(10,"*")    #center(填充个数，填充字符)
# print(res)

# #(8)编码和解码
# #max 返回字符串中编码最大的字母
# #min 返回字符串中编码最小的字母
# str1 = "IT私塾"
# print(max(str1))
# print(min(str1))


# #ord, 内置函数，返回汉字或字母的unicode编码
# print("'I'的编码",ord("I"))
# print("'T'的编码",ord("T"))
# print("'私'的编码",ord("私"))
# print("'塾'的编码",ord("塾"))




