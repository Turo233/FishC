def change_item(file_name, old_str, new_str):
    file = open(file_name)
    print('\n')

    alpha = file.read()
    
    count = alpha.count(old_str)
    str1 = alpha.replace(old_str, new_str)
    
    print('文件 '+file_name+' 共有%d个【'%count+old_str+'】')
    print('您确定要把所有的【'+old_str+'】替换为【'+new_str+'】吗?')

    choice = input('【YES/NO】: ')

    if choice == 'YES' or 'yes':
        file_1 = open(file_name, 'w')
        file_1.write(str1)
        file_1.close()

    file.close()
    
file_name = input('请输入文件名 : ')
old_str = input('请输入要替换的单词或字符 : ')
new_str = input('请输入新的单词或字符 : ')

change_item(file_name, old_str, new_str)

            

