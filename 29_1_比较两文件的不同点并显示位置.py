def compare():
    file_name_1 = input('请输入需要比较的头一个文件名 : ')
    file_name_2 = input('请输入需要比较的另一个文件名 : ')

    file_1 = open('F:/编程/'+file_name_1)
    file_2 = open('F:/编程/'+file_name_2)

    file_1_1 = []
    file_2_1 = []

    differ = []

    count_1 = 1
    count_2 = 1
    
    for each in file_1:
        file_1_1.append([each, count_1])
        count_1 += 1
        
    for each in file_2:
        file_2_1.append([each, count_2])
        count_2 += 1
       
    times = min(count_1, count_2)-1

    for i in range(times):
        if file_1_1[i] != file_2_1[i]:
            differ.append('第 %d 行不一样'%(i+1))
    if count_1 > count_2:
        num = count_1-count_2
        for i in range(num):
            differ.append('第 %d 行不一样'%(i+count_2))
    if count_1 < count_2:
        num = count_2-count_1
        for i in range(num):
            differ.append('第 %d 行不一样'%(i+count_1))

    times_1 = len(differ)
    print('两个文件共有【%d】处不同:'%times_1)
    for each in differ:
        print(each)
compare()

