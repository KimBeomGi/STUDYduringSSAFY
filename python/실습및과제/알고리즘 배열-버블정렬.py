# 버블 정렬 맨 왼쪽부터 값2개씩(i와 i+1)을 비교하며
# 이를 0~N-1까지 반복하고 총 N-1번 반복함

# testcae = 55 7 19 10 23 512

# testcase = list(map(int, input().split()))     # 테스트케이스 입력값을 리스트로 받아둠
testcase = [55, 7, 19, 10, 23, 512]
lenth_tc = len(testcase)                        # 테스트케이스의 길이를 구함
print(testcase)
# 오름차순 버블정렬
for i in range(lenth_tc-1):                     # lenth_tc-1의 수량만큼 반복
    for j in range(lenth_tc-1):                 # [0] ~ [lenth_tc-2] 까지 실시
        if testcase[j] > testcase[j+1]:         # 만약 현재 값이 다음값보다 크면
            testcase[j], testcase[j+1] = testcase[j+1], testcase[j] # 자리교체(오름차순이니까)

print(testcase)



# 이하는 라이브강의하면서 진행한 예시
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

# 버블정렬을 사용해 맥스값을 구하는 예시
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     maxV = arr[0]                           # 첫 원소를 최대로 가정
#     for i in range(1,N):                    # 나머지 원소와 비교
#         if maxV < arr[i]:
#             maxV = arr[i]
#     print(f'#{tc} {maxV} {arr}')



# 버블 정렬을 만들어보자.
# '''
# 55 7 78 12 42
# for i : 0 →  N-1            # 각 구간의 끝
#     for j : 0 → i-1         # 비교할 왼쪽 원소
#         if arr[j] > arr[j+1]
#             arr[j] <-> arr[j+1]    큰 원소 오른쪽으로
# '''
# N = int(input())
# arr = list(map(int, input().split()))
# for i in range(N-1, 0, -1):    # 각 구간의 끝
#     for j in range(i):         # 비교할 왼쪽 원소
#          if arr[j] > arr[j+1]:
#              arr[j], arr[j+1] = arr[j+1], arr[j]

# print(*arr)