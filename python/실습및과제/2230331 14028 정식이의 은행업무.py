import sys
sys.stdin=open('2230331 14028 정식이의 은행업무.txt','r')


# [문제]
# 삼성은행의 신입사원 정식이는 실수를 저질렀다.
# 은행 업무가 마감되기 직전인 지금, 송금할 금액을 까먹고 말았다.
# 하지만 다행스럽게도 정식이는 평소 금액을 2진수와 3진수의 두 가지 형태로 기억하고 다니며, 기억이 명확하지 않은 지금조차 2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다는 것만은 알고 있다. 
# 예를 들어 현재 기억이 2진수 1010과 3진수 212을 말해주고 있다면 이는 14의 2진수인 1110와 14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있다.
# 정식이는 실수를 바로잡기 위해 당신에게 부탁을 하였다.
# 정식이가 송금액을 추측하는 프로그램을 만들어주자.
# ( 단, 2진수와 3진수의 값은 무조건 1자리씩 틀리다.  추측할 수 없는 경우는 주어지지 않는다. )

#               2진수     3진수
# 현재 기억     1010      212

# 정확한 송금액 1110      112

# 2**3*N 2**2*N 2**1*N 2**0*N
# 3**2*N 3**1*N 3**0*N

# [입력]
# 10개 이하의 테스트 케이스가 주어진다.
# 첫 번째 줄에는 테스트케이스의 개수가 주어진다.
# 하나의 케이스는 두 줄로 되어있다.
# 각 케이스의 첫 번째 줄은 정식이가 기억하는 송금액의 2진수 표현, 두 번째 줄은 송금액의 3진수 표현이 주어진다.  
# (3 ≤ 2진수, 3진수의 자릿수 <40)

# [출력]
# 원래 송금하기로 하였던 금액을 케이스마다 한 줄에 하나씩 출력한다.

# [문제풀이]
# 0. 삼성은행의 신입사원 정식이는 실수를왜저질러!!!!
# 0-1. 3진수의 자릿수가 40이하이고, 2진수는 3보단 크므로 값은 기본 최저값은 3이상이다.
# 1. 3진수와 2진수 1자리씩만 틀리므로 주어지는 2진수는 각 자리별 0 1 둘씩 바꾸면서 확인해보고
# 1-1. 3진수는 각 자리별 0,1,2로 세개씩 바꾸면서 확인을 해본다.
# 1-2. 그리고 이 바궈진 2진수와 3진수가 같은 값이 나오면 출력을 멈춘다.

def bin_cal(position, number, value):  # 2진수 계산, 최초 입력은 빈곳을 받을 것임
    global used_b
    if position == N:
        bin_tmp.append(value)
        return
    
    for _ in range(2):
        # 0일때 1로 바꿔서 해보기
        if number == 0 and not used_b:
            used_b = True
            value += 2**position
            bin_cal(position, 1, value)
            value -= 2**position
            used_b = False
        # 1일때 0으로 바꿔서 해보기
        if number == 1 and not used_b:
            used_b = True
            value -= 2**position
            bin_cal(position, 0, value)
            value += 2**position
            used_b = False
    if position != N-1:
        bin_cal(position+1, binary[position+1], value+2**(position+1)*binary[position+1])
    elif position == N-1:
        bin_cal(position+1, 0, value)

def ter_cal(position, number, value):  # 3진수 계산
    global used_t
    if position == M:
        ter_tmp.append(value)
        return

    for _ in range(3):
        # 0일때
        # 0일때 1로 바꿔서 해보기
        if number == 0 and not used_t:
            used_t = True
            value += 3**position*1
            ter_cal(position, 1, value)
            value -= 3**position
            used_t = False
        # 0일때 2로 바꿔서 해보기
        if number == 0 and not used_t:
            used_t = True
            value += 3**position*2
            ter_cal(position, 2, value)
            value -= 3**position*2
            used_t = False
        # 1일때
        # 1일때 0으로 바꿔서 해보기
        if number == 1 and not used_t:
            used_t = True
            value -= 3**position*1
            ter_cal(position, 0, value)
            value += 3**position*1
            used_t = False
        # 1일때 2로 바꿔서 해보기
        if number == 1 and not used_t:
            used_t = True
            value += 3**position*1
            ter_cal(position, 2, value)
            value -= 3**position*1
            used_t = False
        # 2일때
        # 2일때 0으로 바꿔서 해보기
        if number == 2 and not used_t:
            used_t = True
            value -= 3**position*2
            ter_cal(position, 0, value)
            value += 3**position*2
            used_t = False
        # 2일때 1로 바꿔서 해보기
        if number == 2 and not used_t:
            used_t = True
            value -= 3**position*1
            ter_cal(position, 1, value)
            value += 3**position*1
            used_t = False
    if position != M-1:
        ter_cal(position+1, ternary[position+1], value+3**(position+1)*ternary[position+1])
    elif position == M-1:
        ter_cal(position+1, 0, value)

T = int(input())
for testcase in range(1, T+1):
    # 거꾸로 입력받아야함 1010 이면 0101로 그래야 컴퓨터가 읽지 2^0, 2^1으로
    binary_tmp = list(map(int,input()))
    binary = []
    for i in range(len(binary_tmp)-1, -1, -1):
        binary.append(binary_tmp[i])
    N = len(binary)

    ternary_tmp = list(map(int,input()))
    ternary = []
    for i in range(len(ternary_tmp)-1, -1, -1):
        ternary.append(ternary_tmp[i])
    M = len(ternary)

    used_b = False          # binary의 자리값이 사용중인지 아닌지 확인
    used_t = False          # ternary의 자리값이 사용중인지 아닌지 확인
    bin_tmp = []
    ter_tmp = []

    bin_cal(0,binary[0],2**0*binary[0])
    ter_cal(0,ternary[0],3**0*ternary[0])
    ####    # 컴퓨터가 읽을수 있게 완성
    # print(bin_tmp)
    # print(ter_tmp)
    answer = 0
    for bi_v in bin_tmp:
        if bi_v in ter_tmp:
            answer = bi_v
            break
    print(f'#{testcase} {answer}')