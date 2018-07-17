def index_key(source, key):
    key_index = []
    s_index = 0
    e_index = len(source)
    while s_index < e_index:
        try:
            temp = source.index(key, s_index, e_index)
            key_index.append(temp+1)
            s_index = temp + 1
        except ValueError:
            break
    return key_index  #笔记记录!

def research_context(key_word, choice):
    import os
    import os.path

    if choice.upper() == 'YES':
        #选择判定
        for root, dirs, files in os.walk(os.getcwd()):
            for name in files:
                #遍历文件
                name_type = os.path.splitext(name)[1]
                if name_type == '.txt':
                    #判定.txt
                    file = open(root+'\\'+name)
                    #打开文件进行读取
                    length = len(file.readline())
                    count = 1
                    file_context = file.read()
                    if key_word in file_context:
                        print('在文件【'+root+'\\'+name+'】中找到关键字【'+key_word+'】')
                        file.seek(0, 0)
                        for i in range(length):
                            count += 1
                            a = file.readline()
                            if key_word in a:
                                print('关键字出现在第 %d 行, 第 ' %count, end = '')
                                print(index_key(a, key_word), end = '')
                                print(' 个位置 。')
                        print('========================================')
                    file.close()
key_word = input('请讲该脚本放于待查找的文件夹内,请输入关键字 : ')
choice = input('请问是否需要打印关键字【%s】在文件中的具体位置(YES/NO) : '%key_word)
print('========================================')
research_context(key_word, choice)
