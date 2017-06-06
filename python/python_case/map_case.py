# coding:utf-8
def normalize(name):
    # 定义的函数需要有返回值，否则会出现None值
    return name[0].upper()+name[1:].lower()

L1 = ['admin', 'LISA', 'bat']
L2 = map(normalize, L1)
print(list(L2))
