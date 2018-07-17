#整数进制转换

key = 'a'
quitw = 'Qq'

while key not in quitw:
    digit = input('请输入一个整数(输入Q结束程序) : ')

    while not digit.isdigit():
        if digit in 'Qq':
            key = digit
            break
        print('请输入正确的整数', end = '')
        digit = input('(输入Q结束程序) : ')
            
    while not key in quitw:
        digit = int(digit)
        print('十进制 -> 十六进制 : %d -> 0x%x' %(digit, digit))
        print('十进制 -> 八进制 : %d -> 0x%o' %(digit, digit))
        print('十进制 -> 二进制 : %d ->  ' %digit, bin(digit))
        break
    
