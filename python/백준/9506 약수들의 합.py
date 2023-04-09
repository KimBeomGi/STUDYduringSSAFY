# 문제
# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

# 입력
# 입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)

# 입력의 마지막엔 -1이 주어진다.

# 출력
# 테스트케이스 마다 한줄에 하나씩 출력해야 한다.

# n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).

# 이때, 약수들은 오름차순으로 나열해야 한다.

# n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.


##############
# # 시간 초과 남
# import sys

# N = int(sys.stdin.readline().strip())
# while N != -1:
#     # tmp = set()
#     # tmp.add(1)
#     tmp = [1]
#     for i in range(1, (N//2)+1):
#         for j in range(2, (N//2)+1):
#             if i*j == N:
#                 tmp.append(i)
#     # tmp = list(tmp)
#     # tmp.sort()
#     # print(tmp)
#     if sum(tmp) != N:
#         print(f'{N} is NOT perfect.')
#     else:
#         print(f'N =', end = ' ')
#         for i in range(len(tmp)):
#             if i == len(tmp)-1:
#                 print(f'{tmp[i]}')
#             else:
#                 print(f'{tmp[i]} +', end = ' ')
#     N = int(sys.stdin.readline().strip())



#######
import sys

N = int(sys.stdin.readline().strip())
while N != -1:
    # tmp = set()
    # tmp.add(1)
    tmp = [1]
    for i in range(2, (N//2)+1):
        if N % i == 0:
            tmp.append(i)
    # tmp = list(tmp)
    # tmp.sort()
    # print(tmp)
    if sum(tmp) != N:
        print(f'{N} is NOT perfect.')
    else:
        print(f'{N} =', end = ' ')
        answer = ' + '.join(map(str, tmp))
        print(f'{answer}')
    # print('--------------------')
    N = int(sys.stdin.readline().strip())