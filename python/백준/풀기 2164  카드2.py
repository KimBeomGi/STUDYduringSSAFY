# 문제
# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

# 출력
# 첫째 줄에 남게 되는 카드의 번호를 출력한다.

# ###########################
# # 큐 사용해야함
# import sys
# N  = int(sys.stdin.readline().strip())

# cards = [x for x in range(1,N+1)]       # 1~ N까지의 카드

# while len(cards) != 1:
#     cards.pop(0)
#     cards.append(cards.pop(0))
# print(cards[0])


# import sys
# N  = int(sys.stdin.readline().strip())

# cards = [x for x in range(1,N+1)]       # 1~ N까지의 카드, 길이
# Q = [0]*0xffffffff                  # 큐 생성 인덱스로 0~
# for i in range(N):
#     Q[i] = cards[i]

# front = 0
# rear = N-1

# while front < rear:
#     # 카드 버리기
#     front += 1
    
#     # 카드 이동시키기
#     rear +=1
#     Q[rear] = Q[front]
#     front += 1                  # front의 위치를 뒤로 한칸 조정

# print(Q[front])


# import sys

# # T= int(sys.stdin.readline().strip())
# # for testcase in range(1, T+1):
# N = int(sys.stdin.readline().strip())

# cards = [x for x in range(1,N+1)] + [0]     # cards에 0을 더함으로 원형큐로 만듬

# front = 0                               # 빼내려는 위치
# front_a = 0
# rear = N                                # 기입하려는 위치
# rear_a = N

# while front_a <= rear_a:                 # front가 rear-1이 어야 1개 남음
#     if N ==1 :
#         break
#     # 앞에 있는 카드 버리기
#     cards[front] = 0
#     front += 1
#     if front > N :
#         front = 0
#     front_a += 1
#     if front_a == (rear_a -1):
#         break
#     # 앞에 있는 카드 제일 뒤로 보내기
#     cards[rear] = cards[front]
#     rear +=1
#     rear_a += 1
#     if rear > N :
#         rear = 0
#     cards[front] = 0
#     front += 1
#     if front > N :
#         front = 0
#     front_a += 1
# print(f'{cards[front]}')


##########
# 이 방법으로도 푼다고????
import sys

N = int(sys.stdin.readline().strip())
i=0

if N==1:
    print(1)
else:
    while True:
        if 2**i < N <= 2**(i+1):
            break
        i += 1
    print(2*(N-(2**i)))