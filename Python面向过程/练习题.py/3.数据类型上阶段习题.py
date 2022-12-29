# 1.实现一个整数加法计算器（多个数相加）：

# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。
# b = 0
# content = input("请输入内容：")
# a = content.split("+")
# print(a)
# for i in a :
#     b += int(i)
# print(b)




# 2.计算用户输入的内容中有几个整数（以个位数为单位），并打印输出。

# > 如：content = input("请输入内容：")   
# >
# > 如：fhdal234slfh98769fjdla
# >
# > 输出：8个数字：23498769

#(1)
# b = list()
# a = ''
# content = input("请输入内容")
# for i in content:
#     if i.isdigit() ==1:
#         a += i 
  
# print(a)     


#(2)
# content = input("请输入内容")
# content = list(content)
# list=[]
# for i in content:
#     if i.isdigit() == 1:
#         list.append(i)

# aa = "".join(list)
# print(aa)



#3.查找列表wordlist 中的元素，移除每个元素的空格\
#，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，\
# 并添加到一个新列表中,最后循环打印这个新列表


# wordlist =  ["IT sishu", "alexC", "Ab C ",\
#      "egon ", " ticToc ", " Angle ", "  aqc"]


# list = []
# for i in wordlist:
#      i = i.replace(" ","")
#      i.startswith("A")
#      #print(c)
#      i.startswith("a")
#      i.endswith("c")
#      if (i.startswith("a") == True or \
#           i.startswith("A") == True)\
#            and (i.endswith("c")) == True:
#          list.append(i)
#          print(list)


#4.循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。

# wordlist = [1, 3, 4, "sishu", ["aa", "bb",\
#       "cc"], 5, "it"]


# for i in wordlist:
#      if type(i) == list:
#       print("")
#       for j in i:
#             print(j,end=",")
#       print("")
#       continue
#      print(i,end=",")
 
          

#5.假设字符串中含有的字母及长度相同就算相等\
# （例如：aba和aab相等），随便输入二组字符串，
# 请编程比较他们看是否相等


# alpha1 = str(input("请输入一组字母"))
# alpha2 = str(input("请输入一组字母"))
# for i in range(len(alpha1)):
#       if alpha2.find(alpha1[i]) == -1:
#             print("不相等...")
#             break     
#       elif alpha1.count(alpha1[i]) != alpha2.count(alpha1[i]):
#             print("不相等")
#             break
#       else:
#             print("相等")
#             break


      
# word1 = input("请输入")  #abb    
# word2 = input("请输入")  #aab
# word3 = word1 + word2   #abbabb
# if len(word1) == len(word2):
#       for i in word3:
#             n1 = word1.count(i)
#             n2 = word2.count(i)
#             if n1 == 0 or n2 == 0:
#                   print("不相等")
#                   break
#             else:
#                   print("相等")
                  
# else:
#       print("不相等")



# 6.从键盘输入字符串，回车后按单词反转

# > 例如输入：Where there is a way
# >
# > 输出：Way a is there where

# word1 =str(input("请输入:"))
# word2 = word1.split(" ")
# word2.reverse()
# for i in word2:
#     word3 = "".join(i)  
#     print(word3,end=" ")



# 7.判断一句话是否是回文. 回文: 正着念和反着念是一样的. 

# > 例如, 上海自来水来自海上

# content = input("请输入")
# if content == content[::-1]:
#     print("回文")
# else:
#     print("不是回文")         



# content = input("请输入:")
# list1 = list(content)
# list2 = list(reversed(list1))
# if list1 == list2:
#     print("回文")
# else:
#     print("不是回文")
















