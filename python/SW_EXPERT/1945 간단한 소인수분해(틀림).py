# [문제]
# 숫자 N은 아래와 같다.
# N=2^a x 3^b x 5^c x 7^d x 11^e
# N이 주어질 때 a, b, c, d, e 를 출력하라.

# [제약 사항]
# N은 2 이상 10,000,000 이하이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 입력
# 10  
# 6791400
# 1646400
# 1425600
# 8575
# 185625
# 6480
# 1185408
# 6561
# 25
# 330750

# 출력
# #1 3 2 2 3 1
# #2 6 1 2 3 0
# #3 6 4 2 0 1
# #4 0 0 2 3 0
# #5 0 3 4 0 1
# #6 4 4 1 0 0
# #7 7 3 0 3 0
# #8 0 8 0 0 0
# #9 0 0 2 0 0
# #10 1 3 3 2 0


#[문제풀이]
# 1. 숫자 N에 대한 소인수 분해로 2, 3, 5, 7, 11의 소수로만 이루어진 N을 준다.
# 1-1. 따라서 모든 N은 2, 3, 5, 7, 11중 하나에는 해당하는 배수임을 알 수 있다.
# 2. 각 2, 3, 5, 6, 11의 몇 제곱이 들어갔는지 확인하면 되므로 2의 몇 제곱으로만 이루어진 배수라면 2로 몇 번을 나눴는지를 계산하면 된다.


from collections import *                           # collections 모듈을 불러와 그 안의 Counter 함수를 이용해서 각 2,3,5,7,11이 몇 번 들어갔는지 확인

T = int(input())    #T가 최초 입력받을 테스트 개수이므로 최초에 T=int(input())으로 작성해준다.
# arr = [] 
for i in range(1,T+1):                              # 1~T만큼 반복
    N = int(input())                                # N에 입력값을 int로 할당(이 때 N은 2,3,5,7,11의 배수가 될 것이다.)
    primefactor_list = []                           # 소인수분해로 나오게 될 2, 3, 5, 7, 11을 집어넣은 리스트
    while N % 2 == 0:                               # N/2의 나머지가 0이 아닐때까지 while문을 실행
        if N % 2 == 0:                              # N/2의 나머지가 0이라면    
            primefactor_list.append(2)              # primefacotr_list에 2를 추가
            N = N/2                                 # N을 N/2로 할당
    while N % 3 == 0:                               # N/3의 나머지가 0이 아닐때까지 while문을 실행
        if N % 3 == 0:                              # N/3의 나머지가 0이라면    
            primefactor_list.append(3)              # primefacotr_list에 3를 추가
            N = N/3                                 # N을 N/3로 할당
    while N % 5 == 0:                               # N/5의 나머지가 0이 아닐때까지 while문을 실행
        if N % 5 == 0:                              # N/5의 나머지가 0이라면    
            primefactor_list.append(5)              # primefacotr_list에 5를 추가
            N = N/5                                 # N을 N/5로 할당
    while N % 7 == 0:                               # N/7의 나머지가 0이 아닐때까지 while문을 실행
        if N % 7 == 0:                              # N/7의 나머지가 0이라면    
            primefactor_list.append(7)              # primefacotr_list에 7를 추가
            N = N/7                                 # N을 N/7로 할당
    while N % 11 == 0:                              # N/11의 나머지가 0이 아닐때까지 while문을 실행
        if N % 11 == 0:                             # N/11의 나머지가 0이라면    
            primefactor_list.append(11)             # primefacotr_list에 11를 추가
            N = N/11                                # N을 N/11로 할당
# 여기까지 각 소인수 분해를 실행해본 결과이니 이제 각 2,3,5,7,11이 몇 번 들어갔는지를 확인해서 a,b,c,d,e를 파악

use_times_primefactordicd = list(dict(Counter(primefactor_list)).items())       # 리스트 내 인덱스가 몇 번 쓰였는지 2:?의 딕셔너리로 나올 것을 [(2,?)]로 만들어냄
use_times_primefactordict = dict(Counter(primefactor_list).items())
u_t_primefacot = list(map(str, use_times_primefactordict.values()))
submit_u_t_pf = ' '.join(u_t_primefacot)
print(f'#{i}', submit_u_t_pf)