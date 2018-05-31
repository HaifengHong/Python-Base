# -*- coding: utf-8 -*-

# 若文件路径直接复制而来，则需要将最后一级的\再加一个\，即\\；或r''；或将\全部改为/
with open(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\FileIO\fortune500.csv', 'r') as f:
# with open('D:\PyCharmCommunityEdition2017.2.4\PyTests\FileIO\\fortune500.csv', 'r') as f:
    Firstline = f.readline()
    Secondline = f.readline()
    Thirdline = f.readline()
    print(Firstline, Secondline, Thirdline, f.closed)

    # 读取多行
    # Multilines = f.readlines()[0:4]
    # print(Multilines) # 输出在同一行，带'\n'
    for i in f.readlines()[0:4]:
        print(i) # 输出在多行，每行之间空一行