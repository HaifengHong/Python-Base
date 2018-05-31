# -*- coding: utf-8 -*-



# 用逗号或加号连接
print('a', 'b')  # a b
print('a' + 'b')  # ab




# 不带end=' '
print('These items are:')
for item in range(5):
    print(item)
# These items are:
# 0
# 1
# 2
# 3
# 4


# 带end=' '（引号中可以是任意）
print('These items are:', end=' ')
for item in range(5):
    print(item, end=' ')
# These items are: 0 1 2 3 4




# 一行写不下
print('abc'\
'def')  # 第二行要定格写，\加不加结果都一样
print('abc\
def')
print('abc'
'def')
# 输出结果都是abcdef




print('\n') # 输出两行空格（因为print会默认加个'\n'做结尾）