# s1 = list(input())
# s2 = input()
# print(s1)
# print(s2)
'''
def strlen(a):
    i = 0
    while a[i] != '\0':
        i += 1
    return i

a = ['a', 'b', 'c', '\0']
print(strlen(a))
'''
'''
s = 'abc'
a = list(map(str, s))
a[0] = 'c'
s = ''.join(a)
print(s)
'''
'''
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'
print(s1 == s2)
print(s1 is s2)
print(s1 == s5)
print(s1 is s5)
'''

# itoa, atoi 함수 만들어보기
print(ord('1'))     # 문자를 아스키코드 숫자로
print(chr(49))      # 숫자를 아스키코드의 해당 문자로
# '123' >>> 123
# 숫자로된 문자 받아와서 숫자로 반환하기
def atoi(data):
    result = 0
    # '1' > 1 >> 저장
    # '2' > 2 >> 기존값 *10 + 2 >> 저장
    # '3' > 3 >> 기존값 *10 + 3 >> 저장
    for i in range(len(data)):
        result = result * 10 + (ord(data[i]) - ord('0'))
    return result

# 숫자를 문자열로 만들기
def itoa(data):
    result = ''
    # 123 >> '1' + '2' + '3'
    # 숫자의 각 자리를 떼어내기, 10으로 나눈 나머지 바꾸기
    # data를 10으로 나눈 몫과 나머지로 떼내야함
    # data가 0이 되기전까지 반복
    while data > 0:
        remain = data % 10
        chr(remain + ord('0'))
        result = chr(remain + ord('0')) + result     # 원래있던 문자열 앞쪽에 갖다붙이기 위해.
        data = data // 10
    return result

result = atoi('45421')
result2 = itoa(65231)
print(result, type(result))
print(result2, type(result2))