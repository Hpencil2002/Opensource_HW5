#2021041035 조민규#

#전역 변수#
inStr, outStr = '', ''
ch = ''
count, i = 0, 0

##메인 코드##
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for i in range(0, count):
    ch = inStr[i]
    if (ch.isupper()):
        newCh = ch.lower()
    elif (ch.islower()):
        newCh = ch.upper()
    else:
        newCh = ch
    outStr += newCh

print("대소문자 변환 결과 --> %s" %outStr)
