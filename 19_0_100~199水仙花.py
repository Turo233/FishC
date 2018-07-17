#100-999水仙花数


num = 100
while num < 1000:
    if (num%10) ** 3 + ((num//10)%10) ** 3 + ((num//100)%10) ** 3 == num:
        print('厉害了',num,'是水仙花数！')
    num += 1
   
'''
0.代码偏冗长，不宜他人观看

1.参考代码
for i in range(100,1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10
    if sum ==i:
        print(i)
'''
