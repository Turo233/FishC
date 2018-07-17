# 闰年判断

Year = input('想看看哪年是不是闰年啊：')
while not Year.isdigit():
    print('别瞎输入了，',end='')
    Year = input('请重新输入年份：')
Year = int(Year)
if Year%4 == 0 and Year%100 != 0:
    print('%d'%Year+'是闰年。')
elif Year%400 == 0:
    print('%d'%Year+'是闰年。')
else:
    print('不是闰年。')
