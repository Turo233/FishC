def file_research(file_name):
    import os
    import os.path

    os.chdir(file_name)

    file_txt = open(file_name+r'/vedioList.txt', 'w')

    for root, dirs, files in os.walk('F:/编程/python'):
        for name in files:
            type_file = os.path.splitext(name)[1]
            if type_file in [.mp4, .rmvb.avi':
                str1 = os.path.join(root, name) + '\n'  #此处需要记录在笔记上
                file_txt.write(str1)
                
    file_txt.close()

file_name = input('请输入待查找的初始目录 : ')
file_research(file_name)

