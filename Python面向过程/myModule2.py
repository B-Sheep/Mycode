#脚本方式

# print("myModule2...")

# m=10
# print(f'myModule2...m={m}')


def add(a,b):
    print('myModule1:add.....')
    return f'{a}+{b}={add}'



print(__name__,type(__name__))


def main():
    print("myModule2...")
    m = 10
    print(f"myModule2...m = {m}")




#模块方式：myModule2

if __name__ == '__main__':
    main()

















