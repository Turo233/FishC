'''
def file_size(file_name):
    import os
    import os.path

    os.chdir(file_name)

    list_file = os.listdir()

    length = len(list_file)

    prompt = '%s 【%dBytes】'

    for i in range(length):
        print(prompt % (list_file[i], os.path.getsize(list_file[i])))
        
file_name = input('请输入需要查看数据大小的文件夹: ')
file_size(file_name)


'''
#使用字典的方法

import os
import os.path

file_name = input('请输入目录:')

os.chdir(file_name)
file_list = os.listdir()

file_size = dict()

for each in file_list:
    if not os.path.isdir(each):
        file_size.setdefault(each)
        file_size[each] = os.path.getsize(each)
        
for each in file_size.keys():
    print('%s 【%d Bytes】' % (each, file_size[each]))
