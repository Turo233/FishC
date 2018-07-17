def Designated_line():
    text_path = input('请输入要打开的文件(c:/test.txt) : ')
    text_file = open(text_path)

    text_rows = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21:】 : ')
    print('\n', end = '')
    (begin, end) = text_rows.split(':', 1)

    all_row = len(text_file.readline())

    if begin == '':
        begin = 0
    else:
        begin = int(begin)

    if end == '':
        end = all_row
    else:
        end = int(end)

    data = text_file.readlines()

    if begin == 0:
        if end == all_row:
            print('文件'+text_path+'的全文内容如下\n')
            for each in data[:]:
                print(each)
        else:
            print('文件'+text_path+'从开始到第%d行的内容如下\n'%end)
            for each in data[:end]:
                print(each)
    else:
        if end == all_row:
            print('文件'+text_path+'从第%d行到末尾的内容如下\n'%begin)
            for each in data[begin-1:]:
                print(each)
        else:
            print('文件'+text_path+'从第%d行到第%d行的内容如下\n'%(begin, end))
            for each in data[begin-1:end]:
                print(each)

Designated_line()
