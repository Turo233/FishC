'''
def get_digits(n):
    str1 = list()
    while n:
        str1.append(n%10)
        n //= 10
    str1.sort()
    return str1
        
'''
def get_digits(n, str1 = list()):
    if n // 10:
        str1.append(n%10)
        return get_digits(n%10, str1)
    else:
        str1.append(n)
        str1.sort()
        return print(str1)
