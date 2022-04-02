##2021041035 조민규##

import string

#함수 선언#
def base2(n, base = 2):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(n, base)
    return base2(q, base) + number[r] if q else number[r]

def base8(n, base = 8):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(n, base)
    return base2(q, base) + number[r] if q else number[r]

def base16(n, base = 16):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(n, base)
    return base2(q, base) + number[r] if q else number[r]

#메인 코드#
num = int(input('10진수 입력 --> '))

num_2 = base2(num)
num_8 = base8(num)
num_16 = base16(num)

print('2진수 : %s' %num_2)
print('8진수 : %s' %num_8)
print('16진수 : %s' %num_16)
