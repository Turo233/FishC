#密码锁2018/2/26

Bingo = 'FishC.com'

string = str(input('请输入密码:'))
chance = 3

while chance > 1:
    if '*' in string:
        print('密码中不能含有\"*\"号！您还有',chance,'次机会！', end = '')
        string = str(input('请输入密码：'))
        continue
    elif string == Bingo:
        print('密码正确，进入程序......')
        break
    else:
        print('密码输入错误！您还有',chance-1,'次机会！',end = '')
        string = str(input('请输入密码：'))
        chance -= 1
        continue

'''
0.将第五行代码写到while循环中，可减少代码量。
1.程序while循环中最后的语句看来并不需要加continue
2.可以把循环中判定为正确的放在循环第一次
'''
