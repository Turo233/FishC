print('|--- 欢迎进入通讯录程序 ---|')
print('|---  1 : 查询联系人资料  ---|')
print('|---  2 : 插入新的联系人  ---|')
print('|---  3 : 删除已有联系人  ---|')
print('|---  4 : 退出通讯录程序  ---|')

phone = {}

while True:
    num = input('\n请输入相关的指令代码 : ')
    while not num.isdigit():
        num = input('请输入正确的代码 : ')
    num = int(num)
    
    if num == 1:
        name = input('请输入联系人姓名 : ')
        if name in phone:
            print(name + ' : ' + phone[name])
        else:
            print('查无此人!')
            
    elif num == 2:
        name_1 = input('请输入联系人姓名 : ')
        if name_1 in phone:
            print('您输入的姓名已在通讯录中存在 -->'+ name_1 + ' : ' + phone[name_1] )
            judge = input('是否修改用户资料 (YES/NO) : ')
            if judge == 'yes' or 'YES':
                phone[name_1] = input('请输入用户联系电话 : ')
        else:
            phone[name_1]  = input('请输入用户联系电话 : ')

    elif num == 3:
        name_2 = input('请输入联系人姓名 : ')
        if name_2 in phone:
            judge_1 = input('是否要删除该联系人 (YES/NO) : ')
            if judge_1 == 'yes' or 'YES':
                del dict['name_2']
        else:
            print('查无此人!')

    elif num == 4:
        print('|--- 感谢使用通讯录程序 ---|')
        break
#2018.03.08
