##2021041035 조민규##

import random

#함수 선언#
def getNum(strData):
    numStr = ''
    for ch in strData:
        if ch.isdigit():
            numStr += ch

    return int(numStr)

#전역 변수#
data = []
i, k = 0, 0

#메인 코드#
for i in range(0, 10):
    temp = hex(random.randrange(0, 100000))
    temp = temp[2:]
    data.append(temp)

print('정렬 전 데이터 : ', end = '')
[print(num, end = ' ') for num in data]

for i in range(0, len(data) - 1):
    for k in range(i + 1, len(data)):
        if getNum(data[i]) > getNum(data[k]):
            temp = data[i]
            data[i] = data[k]
            data[k] = temp

print('\n정렬 후 데이터 : ', end = '')
[print(num, end = ' ') for num in data]
