
'''
# 이것은 버블 정렬에 관련한 내용임
# 55 7 78 12 42
# for i : 0 →  N-1            # 각 구간의 끝
#     for j : 0 → i-1         # 비교할 왼쪽 원소
#         if arr[j] > arr[j+1]
#             arr[j] <-> arr[j+1]    큰 원소 오른쪽으로

N = int(input())
arr = list(map(int, input().split()))
for i in range(N-1, 0, -1):    # 각 구간의 끝
    for j in range(i):         # 비교할 왼쪽 원소
         if arr[j] > arr[j+1]:
             arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)
'''

'''
아래는 테스트케이스
3
5
55 7 78 12 42
6
55 7 79 100 42 1
7
7 55 7 79 12 42 2 90
가장 큰 값을 출력
#1 78
#2 100
#3 90
'''
'''
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     maxV = arr[0]                           # 첫 원소를 최대로 가정
#     for i in range(1,N):                    # 나머지 원소와 비교
#         if maxV < arr[i]:
#             maxV = arr[i]
#     print(f'#{tc} {maxV}')

T = int(input())            # 한 줄 입력받아서 숫자로 변경
#T번 만큼의 테스트 케이스를 처리하면서 결과 출력

for testcase in range(1, T+1):

    # 첫줄에는 N
    # 두번째 줄에는 N개의 양의 정수
    N = int(input())
    # 문자열 → 문자열 리스트로 변경 → 각 요소를 숫자로 변경
    # .split()은 각 문자열의 문자를 띄어줌
    # map(func, iterable): iterable의 각 요소에 func 적용
    # '10 13 23 45 789'
    # ['10', '13', '23', '45', '789']
    # [10, 13, 23, 45, 789]
    numbers = list(map(int, input().split()))
    ############
    # N 과 numbers를 이용해서 각 테스트케이스의 정답 출력

    # 가장 큰 값 저장하는 변수 선언

'''

# 9
# 7 4 2 0 0 6 0 7 0
N = int(input())
boxes = list(map(int, input().split()))
# 0번 부터 N-12번까지 오른족에 있는 나보다 높이가 낮은 것의 갯수를 확인 필요.
max_cnt = 0
for i in range(N):
    # i+1번부터 N-1번까지 i번 보다 작은 수의 개수
    cnt = 0 #아무것도 안세면 0이니까
    # i보다 1큰거 부터해서 마지막까지
    # boxes[i] boxes[i+1]
    # boxes[i] boxes[i+2]
    # boxes[i] boxes[i+3]
    # ~~~
    # boxes[i] boxes[N-1]
    for j in range(i+1, N):     # j = i+1 ~ N-1을 의미
        if boxes[i] > boxes[j]:
            cnt += 1
    #########여기가 i번째 요소보다 작은게 몇개인지 확인함. 어디서? cnt에서 확인.
    # 위 반복문을 돌면서 제일 큰 cnt를 찾는게 우리 목표 
    if max_cnt < cnt:       # 내가 알고 있는 최댓값보다 방금 구한 값이 더 크면
        max_cnt = cnt       # 최댓값 바꿔주기
print(max_cnt)