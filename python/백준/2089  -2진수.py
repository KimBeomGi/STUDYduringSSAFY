# A_tmp= input()
# A = A_tmp[1:]
# A_bin = int(A,2)
# print(A_bin[2:])

# A = input()
# B = int(A,2)
# print(B)

'''
def check(A, check_bin):
    global value
    N = len(check_bin)
    value = 0
    for i in range(N):          # -2진법으로 확인하기 위해서
        if  N % 2 == 0:                                 # 제곱수 가 짝수면 양수,
            value += 2**(N-1-i)*check_bin[i]
        elif  N % 2 == 1:                               # 제곱수가 홀수면 음수,
            value += -1*(2**(N-1-i)*check_bin[i])
    if value == A:
        return
    if value != A:
        if check_bin[-1] == 0:
            check_bin[-1] = 1
            check(A, check_bin)                      # 마지막 인자를 1로 만들기
            check_bin[-1] = 0
        check(A, check_bin+[0])                  # check_bin에 인자 0을 더하기
        
        return
    

A = int(input())
value = 0
# 1 -2 4 -8 16 -32 64 -128

# if  N % 2 == 0:
#     (-2)**N*a = 2**N*a
# if  N % 2 == 1:
#     (-2)**N*a = -(2**N)*a
check_bin = [0]
check(A, check_bin)
print(check_bin)
'''
n = int(input())
value =''
if n == 0:
    print(0)
    exit()
while n:
    if n % (-2):
        value = '1' + value
        # -2로 나누어 떨어지지 않는 경우 몫을 구하기 위해 1을 더함
        n = n//-2 + 1
    else:
        value = '0' + value
        n = n//-2

print(value)