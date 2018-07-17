#check.py  

nums = '1234567890'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '~!@#$%^&*()_=+-/,.?<>;:[]{}|\\'
way = '''请按以下方式提升您的密码安全级别：
                                                1.密码必须由数字、字母及特殊字符三种组合
                                                2.密码只能由字母开头
                                                3.密码长度不能低于16位
                                '''
i, j, k = 0, 0, 0

key = str(input('请输入需要检查的密码组合：'))
print('您的密码安全级别评定为 : ', end = '')

length = len(key)

while (key.isspace() or length == 0):
    key = input('您输入的密码为空(或空格),请重新输入 : ')
    length = len(key)

for each in key:
        if each in nums:
            i = 1
            break #判定是否有数字
for each in key:
        if each in alpha:
            j = 1
            break #判定是否有字母
for each in key:
        if each in special:
            k = 3 
            break #判定是否有特殊字符
        
degree = i + j + k

if length <= 8 or degree == 1:
    print('低')
    print(way)
elif length > 16 and degree == 5 and (key[0] in alpha):
    print('高')
    print('请继续保持')
else:
    print('中')
    print(way)
    
'''
2018年2月27日
===================== RESTART: E:\1编程\2Python\密码安全性检查.py =====================
请输入需要检查的密码组合：WS{ABCBA}SB
您的密码安全级别评定为 : 中
请按以下方式提升您的密码安全级别：
                                                1.密码必须由数字、字母及特殊字符三种组合
                                                2.密码只能由字母开头
                                                3.密码长度不能低于16位
'''
