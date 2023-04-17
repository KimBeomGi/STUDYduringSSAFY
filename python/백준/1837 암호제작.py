# 문제
# 원룡이는 한 컴퓨터 보안 회사에서 일을 하고 있다. 그러던 도중, 원룡이는 YESWOA.COM 으로부터 홈페이지 유저들의 비밀키를 만들라는 지시를 받았다. 원룡이는 비밀 키를 다음과 같은 방법으로 만들었다.

# 개인마다 어떤 특정한 소수 p와 q를 주어 두 소수의 곱 pq를 비밀 키로 두었다. 이렇게 해 주면 두 소수 p,q를 알지 못하는 이상, 비밀 키를 알 수 없다는 장점을 가지고 있다.

# 하지만 원룡이는 한 가지 사실을 잊고 말았다. 최근 컴퓨터 기술이 발달함에 따라, 소수가 작은 경우에는 컴퓨터로 모든 경우의 수를 돌려보아 비밀 키를 쉽게 알 수 있다는 것이다.

# 원룡이는 주성조교님께 비밀 키를 제출하려던 바로 직전에 이 사실을 알아냈다. 그래서 두 소수 p, q 중 하나라도 K보다 작은 암호는 좋지 않은 암호로 간주하여 제출하지 않기로 하였다. 이것을 손으로 직접 구해보는 일은 매우 힘들 것이다. 당신은 원룡이를 도와 두 소수의 곱으로 이루어진 암호와 K가 주어져 있을 때, 그 암호가 좋은 암호인지 좋지 않은 암호인지 구하는 프로그램을 작성하여야 한다.

# 입력
# 암호 P(4 ≤ P ≤ 10100)와 K (2 ≤ K ≤ 106) 이 주어진다.

# 출력
# 만약에 그 암호가 좋은 암호이면 첫째 줄에 GOOD을 출력하고, 만약에 좋지 않은 암호이면 BAD와 소수 r을 공백으로 구분하여 출력하는데 r은 암호를 이루는 두 소수 중 작은 소수를 의미한다.
# import sys
# P, K = map(int, sys.stdin.readline().strip().split())

# sosu = []                           # 소수를 담아놓을 리스트
# for i in range(2,P):                # 2부터 P-1까지를 확인함.
#     for j in range(2,i):            # 2부터 i-1까지 확인하면서 소수인지 확인하기
#         if i%j == 0:                # i를 j로 나눴을 때 떨어지면
#             break                   # 소수가 아니니 그만 확인
#     else:                           # break에 안걸렸으면
#         sosu.append(i)              # sosu니까 리스트에 담아놓기
# # print(sosu)
# N =  len(sosu)
# result = []                         # 값이 P가 되는 소수
# for i in range(N-1):                # [-2]까지
#     for j in range(i+1, N):         # i+1 ~[-1]까지
#         if i*j == P:                # i*j가 P인지 확인하고
#             result.append([i,j])    # result에 [i,j]를 추가한다.
#             break                   # i에선 j를 더 확인할 필요가 없으니 break

# M = len(result)                     # reuslt의 길이
# for i in range(M):                  # result안의 소수를 돌리면서
#     if result[i][0] < K or result[i][1] < K:                # K보다 작으면
#         print('BAD', min(result[i][0], result[i][1]))       # 출력값을 출력
#         break
# else:                               # 문제가 없었으면
#     print('GOOD')                   # GOOD을 출력





import sys
p, k = map(int, sys.stdin.readline().rsplit())
n = [1]*k 
for i in range(2, int(k**0.5)+1):               #에라토스테네스의 체
    if n[i] == 1:                               # n[i]가 1 이면
        for j in range(i+i, k, i):              # 2*i~ k-1까지 확인하며, i간격만큼 확인
            n[j] = 0                            # n[j]는 0으로 하기
prime = [i for i in range(2, k) if n[i] == 1]   # prime 리스트에 소숫값 넣기
good, bad = 1, 0                                # good과 bad에 각각 분별값 부여
for i in prime:                                 # prime에 있는 것을 인자로 하기
    if p % i == 0:                              # p가 소숫값으로 나누어질 때
        good, bad = 0, i                        #good은 0 bad에는 i값 넣어줌
        break
if good:                                        #리스트의 길이가 0보다 클 때 즉, 리스트의 인덱스가 존재할 때
    print("GOOD")
else:
    print("BAD", i)