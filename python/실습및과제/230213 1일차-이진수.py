# def Bbit_print(i):
#     output = ''
#     for j in range(7,-1,-1):
#         output += "1" if i&(1<<j)else '0'
#     print(output)

# for i in range(-5, 6):
#     print("%3d = " % i, end = '')
#     Bbit_print(i)

# print("%3d = " % 5, end = '')
# Bbit_print(4)


import sys
sys.stdin = open('230213 1일차-이진수.txt', 'r')


# [문제풀이]
# 0. 주는 문자를 16진수로 변환해서 출력하라고한다. 싫은뎁
# 1. 아스키코드상 65~70의 번호에 해당하는 A,B,C,D,E,F를 A부터 65-7을 해줘 58~~~로 바꾸고
# 1.1 48번으로 되어있는 0을 숫자 0으로 바꾸어 주도록 하기 위해 -48를 해주고 하자. 

def Bbit_print(i):                                              # 주어지는 숫자를 2진수로 바꾸어주는 마법의 식이다.
    output = ''                                                 # 출력해주기 위한 output을 정해주고
    for j in range(3,-1,-1):                                    # 몇개의 0 구간을 만들것인지 제안하고
        output += '1' if i&(1<<j) else '0'                      # 각 자리의 숫자가 기계어로 1이 맞을때만 1을 표현하도록 만들어주고
    return output                                               # output을 출력

def hexa(string_input):                                         # 16진수에서 10~ 15에 해당하는 A~F까지의 문자를 숫자로 변환시켜줄것임
    if string_input in ["A", "B", "C", "D", "E", "F"]:          # A~F라면
        string_input = ord(string_input) - 7 -48                # 아스키코드를 이용해 숫자 10~16으로 바꿔주고
        return string_input                                     # 숫자 10~16으로 내놓기
    else:                                                       # 숫잔데 다만 str로 받은 거라면
        string_input = ord(string_input) -48                    # 아스키코드 숫자로 바꿔주기
        return string_input                                     # 그리고 숫자로 내놓기

T = int(input())
for testcase in range(1, T+1):
    N, N_string = map(str, input().split())                     # 우선 자릿수 N과 문자를 그대로 str로 받고
    N = int(N)                                                  # 자릿수는 int로 변경해주기
    N_string = list(N_string)                                   # 받은 문자는 리스트화해서 문자를 분리
    # print(N_string)
    hexa_change_num = []                                        # 숫자화 진행할 문자를 담아둘 그릇 생성
    for string_i in N_string:                                   # 숫자화 진행하는 반복문
        hexa_change_num.append(hexa(string_i))                  # hex_change_num에 hexa한 것을 넣어두기

    print(f'#{testcase}', end = ' ')                            # 출력해야하니까 우선 #testcase 하고 이어서
    for hexa_num in hexa_change_num:                            # 숫자화 진행한 녀석들 하나하나 16진수화
        print(Bbit_print(hexa_num), end = '')                   # 16진수화 하고 출력
    print()                                                     # 출력 끝~