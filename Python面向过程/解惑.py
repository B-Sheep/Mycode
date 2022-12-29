# def dump(dndex,default=0,*args,**kw):
#     print('打印函数')
#     print('----')
#     print('index:',dndex)
#     print('default:',default)
#     for i,arg in enumerate(args):
#         print(f'arg[{i}]:',arg)
#     for key,value in kw.items():
#         print(f'keyword_argument {key}:{value}')
#     print('')

# if __name__ == '__main__':
#     # dump(0)
#     # dump(0,2)
#     # dump(0,2,"Hello","World")
#     dump(0,2,"Hello","World",install='Python',run='Python Program')


# res ={"tt":"yiyi","xx":"uu","cc":"jj"}
# for i,x in enumerate(res.values()):
#     print(i,end="")
#     print(x)

list3 = "abcferta"
list1 ={"tt":"1","ww":"2","ii":"3"}
list2 = ["4","5","6"]

print(*list2)
print(*list3)