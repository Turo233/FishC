def file_name(boy, girl, count):
    file_boy_name = 'F:/编程/boy_'+str(count)+'.txt'
    file_girl_name = 'F:/编程/girl_'+str(count)+'.txt'

    file_boy = open(file_boy_name, 'x')
    file_girl = open(file_girl_name, 'x')

    file_boy.writelines(boy)
    file_girl.writelines(girl)

    file_boy.close()
    file_girl.close()

def split_file(file_name):
    f = open(file_name)

    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1

    save_file(boy, girl, count)

    f.close()

file_1('F:/编程/record.txt')
