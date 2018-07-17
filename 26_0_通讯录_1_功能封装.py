Account = {}

def new_user():
    prompt = '请输入用户名:'
    while True:
        name = input(prompt)
        if name in Account:
            prompt = '此用户名已被使用,请重新输入 : '
            continue
        else:
            break 
    passwd = input('请输入密码 : ')
    Account[name] = passwd 
    print('注册成功,赶紧试试登录吧^_^\n')

def old_user():
    prompt = '请输入用户名 : '
    while True:
        name = input(prompt)
        if name not in Account:
            prompt = '您输入的用户名不存在,请重新输入 : '
            continue
        else:
            break
    psw = Account[name]
    for i in range(3):
        passwd = input('请输入密码 : ')
        if passwd == psw:
            print('欢迎进入XXOO系统,请点右上角的X结束程序!')
            break
        else:
            print('密码错误! 还有%d次机会' % (2-i), end = '')
    
def XXOO():
    print('|--- 新建用户 : N/n ---|')
    print('|--- 登录帐号 : E/e  ---|')
    print('|--- 退出程序 : Q/q ---|')
    
    while True:
        key = input('|--- 请输入指令代码 : ')
        while key not in 'NnEeQq':
            key = input('请输入正确指令 : ')
        
        if key in 'Qq':
            print('感谢使用XXOO系统,现在正在退出...')
            break
            
        if key in 'Nn':
            new_user()
            
        if key in 'Ee':
            old_user()
            
XXOO()
