# 三色球摸出的颜色搭配

for i in range(0,4):
    for j in range(0,4):
        for k in range (2, 7):
            if i + j + k ==8:
                print(i,'红',j,'黄',k,'蓝')
'''
0.忘记算红和黄为0的情况。
1.定义变量最好有意义。
'''
