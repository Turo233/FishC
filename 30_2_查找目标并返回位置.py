'''
def search(file_path, file_replace):
    import os
    import os.path

    os.chdir(file_path)

    for root, dirs, files in os.walk(file_path):
        for name in files:
            if name == file_replace:
                print(os.path.join(root, name))
        for name in dirs:
            if name == file_replace:
                print(os.path.join(root, name))

file_path = input('请输入待查找的初始目录 : ')
file_replace = input('请输入需要查找的目标文件 : ')
search(file_path, file_replace)
'''

#使用递归实现目标函数

import os
import os.path

def search_file(file_path, target):
    os.chdir(file_path)

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            search_file(each_file, target)
            os.chdir(os.pardir)
            
file_path = input('请输入目标位置 : ')
target = input('输入目标文件 : ')
search_file(file_path, target)
