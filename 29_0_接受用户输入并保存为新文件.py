def recive():
    #创建用户指定名字文件
    file_name = input('请输入文件名 : ')
    f = open('F:/编程/'+file_name, 'w')
    print('请输入内容[单独输入\':w\'保存退出]')
    
    content = []
    while True:
        #获取用户输入
        con = input('')
        if con[-2:] != ':w':
            str1 = con + '\n'
            content.append(str1)
        else:
            break
    #存储用户输入
    f.writelines(content)
    f.close()

recive()

#2018.3.11
'''
line8 - line13

其实可以直接用字符串,并不需要用列表麻烦的操作,
while True:
    write_some = input()
    if write_some != ':w':
        f.write('%s\n' % write_some)
'''
