import sys
sys.stdin = open('230220 6일차-피자굽기.txt.', 'r')

# [문제]
# N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.
# 1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.
# 주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.

# - 피자는 1번위치에서 넣거나 뺄 수 있다.
# - 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
# - M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
# - 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 
# 다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.
# 3<=N<=20, N<=M<=100, 1<=Ci<=20

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.

# [문제풀이]
# 0. 피자를 돌려돌려돌림판 하면서 확인하고, 치즈의 양이 0이 되면 꺼내고 남은 피자를 순서대로 넣는 것이다
# 0-1. 출력은 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 것이다.
# 1. 돌리는 것은 '원형큐'를 이용해보고, 피자먹고싶다. 남은 피자를 순서대로 넣는 것은 .pop()를 하는 것으로 해보자.
# 2. 주어진 피자들 내에서만 돌리면 되니까 뭔가 추가하지말고, front와 rear를 이용해보자.

# T = int(input())
# for testcase in range(1, T+1):
#     N, M = map(int, input().split())
#     pizza_cz = list(map(int,input().split()))   # 화덕에 있는 피자들을 리스트화
    
#     front = 0
#     rear = 0
#     solve = []

#     while pizza_cz:                             # 화덕에 피자가 있을 때만 실행
#         if pizza_cz[rear] != 'No' and pizza_cz[rear]//2 == 0:              # 치즈가 녹아서 없어지면
#             solve.append(rear)                  # 마지막 남은 피자의 위치를 확인하기 위해
#             pizza_cz[rear] = 'No'               # 해당 치즈는 끝났고, 'No'로 만들어서 문제풀기 쉽게 만들어주자.
#         elif pizza_cz[rear] != 'No':            # 완성되어 꺼낸 피자가 아니면
#             pizza_cz[rear] = pizza_cz[rear]//2  # 피자 치즈를 문제 제시대로 반을 녹임
#             rear = (rear+1)%M                   # rear를 한칸 뒤로 보냄
#             front = (front+1)%M
#         for pizza in pizza_cz:                  # 피자가 전부 None인지 확인하는 반복문
#             if pizza != 'No':                   # 피자가 아직 화덕에 남아있으면
#                 break                           # break
#         else:
#             break
#     print(solve)

# T = int(input())
# for testcase in range(1, T+1):
#     N, M = map(int, input().split())                # 화덕의 갯수 N, 피자의 갯수 M
#     ci = list(map(int,input().split()))             
    
#     front = 0
#     rear = 0



T = int(input())                        
for tc in range(1,T+1):                             # 반복값 입력
    N, M = map(int, input().split())                # 화덕의 갯수 N, 피자의 갯수 M
    pizzas = list(map(int, input().split()))        # 각 피자의 치즈양을 입력받아 리스트화
    hwa_duck = [0]*N                                # N개의 화덕을 리스트화
    for i in range(N):                              # 화덕에 0번~N-1번까지 번호 붙여주기
        hwa_duck[i] = i

    num = 0                                         # while문에서 화덕을 돌리기 위해서 사용되는 num
    idx = N                                         # 피자 리스트의 인덱스
    while sum(pizzas):                              # pizzas리스트 즉, 치즈가 완전히 없어지기전까지 실행
        pizzas[hwa_duck[num]] //= 2                 # num 화덕에 올려진 피자의 치즈를 반으로 나눠주기
        if not pizzas[hwa_duck[num]] and idx < M:   # num 화덕에 올려진 피자의 치즈가 0이고 idx < M이면(idx는 인덱스값이므로 M보다 작아야함)
            hwa_duck[num] = idx                     # 피자가 사라졌으니, 해당 num 화덕에 idx에 위치한 피자를 추가
            idx += 1                                # 다음 피자를 준비해야되니까 idx += 1
        num = (num + 1)% N                          # 화덕을 돌리면서 해야하니까
 
    # hwa_duck[num - 1]의 이유는 피자가 다 녹았지만,
    # while문에 의해 (num+1)%N 을 진행한 뒤 탈출했기 때문에 화덕의 번호를 이전의 값으로 당겨
    # 해당화덕의 인덱스 값인 hwa_duck[num - 1]에 +1을 함으로, 인덱스값이 아닌 1부터 시작하는 번호로 만들어서 출력
    print(f'#{tc} {hwa_duck[num - 1] + 1}')         # 출력값 출력