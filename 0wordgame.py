#wordgame

'''
18/2/24 第一次
18/3/20 加入图形界面 title和msg直接在最前端用变量表示,后续直接引用
msgbox里面可以直接加字符串, 如果用关键字参数则都必须用关键字参数
'''
import random
import easygui as g

def int_num():
    #输入数字
    nums = g.enterbox(msg, title)
    while not nums.isdigit():
        g.msgbox('抱歉，输入不合法,')
        nums = g.enterbox(msg, title)
    return int(nums)

times = 3

secret = random.randint(1,10)
title = '猜数字'
msg = '不妨猜一下我心中的数字(1~10)：'

guess = int_num()

i = 0
while i < times and guess != secret:
    if guess >secret:
        g.msgbox('呦呦，大了大了！')
    else:
        g.msgbox('小了小了。。嘿')
    guess = int_num()
    i += 1
    
if guess == secret:
    if i <= 1:
        g.msgbox('我艹，你是我心中的蛔虫吗')
    else:
        g.msgbox('终于猜对了')    
    g.msgbox('不玩啦，被你猜中了')
else:
    g.msgbox('游戏结束不玩啦，没默契')
