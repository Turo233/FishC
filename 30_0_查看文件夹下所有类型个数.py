'''
def typenum(file_name):
    import os

    os.chdir(file_name)

    list_file = os.listdir()

    length = len(list_file)
    type_list = []
    temp = []

    for i in range(length):
        type_list.append(os.path.splitext(list_file[i])[1])

    for i in range(length):
        if type_list[i] == '':
            type_list[i] = '文件夹'
        
    for each in type_list:
        if each not in temp:
            temp.append(each)
            
    length_1 = len(temp)

    prompt = '该文件下共有类型为【%s】的文件 %d 个'

    for i in range(length_1):
        print(prompt %(temp[i], type_list.count(temp[i])))

file_name = input('请输入要查看的文件夹的路径 : ')
typenum(file_name)
'''
'''
尝试用字典修改以上程序, 所学如下:
0.isdir/isfile的用法以及exists/isabs/islink/ismount/samefile/的拓展:os.path.isdir:判断是否为目录,其他详见os/os.path模块
1.dict.setdefault()的使用方法, 效果如同get()
2.修改和引用字典中键的值需要用[]而非()
'''
def typenum(file_name):
    import os
    import os.path

    os.chdir(file_name)

    list_file = os.listdir()

    type_list = dict()
    
    for each in list_file:
        if os.path.isdir(each):
            type_list.setdefault('文件夹', 0)
            type_list['文件夹'] += 1
            
        else:
            type_name = os.path.splitext(each)[1]
            type_list.setdefault(type_name, 0)
            type_list[type_name] += 1
            
            
    for each in type_list.keys():
        prompt = '该文件下共有类型为【%s】的文件 %d 个'
        print(prompt %(each, type_list[each]))
        
file_name = input('请输入要查看的文件夹的路径 : ')
typenum(file_name)
