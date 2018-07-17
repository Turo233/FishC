def rows_output():
    text_path = input('请输入要打开的文件(c:/test.txt) : ')
    text_file = open(text_path)

    text_rows = int(input('请输入需要显示该文件的前几行 : '))

    print('\n文件'+text_path+'的前%d行内容如下\n'%text_rows)
    for i in range(int(text_rows)):
        print(text_file.readline(), end = '')

    text_file.close()

rows_output()
