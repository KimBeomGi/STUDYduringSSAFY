# 문제
# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

# 출력
# 예제와 같이 요세푸스 순열을 출력한다.

# 1 → 2 → 3 → 4 → 5 → 6 → 7 → 1
#             ↑         |
#             |_________|
            
# 1. 3번째 점인 3을 선택합니다.
# 2. 3번째 점부터 시계방향으로 2개의 점을 건너뛴 다음, 그 다음에 오는 점인 6을 제외합니다. 남은 점들은 다음과 같습니다.

#    1 → 2 → 3 → 4 → 5 →   → 1
#             ↑         |
#             |_________|

# 3. 6번째 점인 6을 선택합니다.
# 4. 6번째 점부터 시계방향으로 2개의 점을 건너뛴 다음, 그 다음에 오는 점인 2를 제외합니다. 남은 점들은 다음과 같습니다.

#    1 →   → 3 → 4 → 5 →   → 1
#           |           |
#           |___________|

# 5. 2번째 점인 2를 선택합니다.
# 6. 2번째 점부터 시계방향으로 2개의 점을 건너뛴 다음, 그 다음에 오는 점인 5를 제외합니다. 남은 점들은 다음과 같습니다.

#    1 →   → 3 → 4 →     → 1
#                   |
#                   |

# 7. 5번째 점인 5를 선택합니다.
# 8. 5번째 점부터 시계방향으로 2개의 점을 건너뛴 다음, 그 다음에 오는 점인 1을 제외합니다. 남은 점들은 다음과 같습니다.

#    1 →   → 3 → 4 →     → 1
#                           |

# 따라서, 마지막으로 남는 병사는 4번째 병사입니다.


########
# 이거 틀림.
# import sys

# N, K = map(int, sys.stdin.readline().strip().split())

# array = [(x+1) for x in range(N)]
# value = []
# front = K-1

# print('<', end=' ')
# while array:
#     answer = array.pop(front)
#     if len(array) != 0:
#         print(f'{answer},', end=' ')
#     else:
#         print(f'{answer}', end=' ')
#     front = front + (K-1)
#     while array and front > len(array)-1:
#         front -= len(array)
# print('>')



#############################
#꼭 다시 풀것!!!!


# N, K = map(int, input().split())

# # 1부터 N까지의 수를 리스트에 담음
# arr = [i for i in range(1, N+1)]

# # 결과를 담을 리스트
# result = []

# # 삭제할 인덱스를 가리키는 변수 idx
# idx = K-1

# # arr에서 수가 모두 삭제될 때까지 반복
# while arr:
#     # idx가 arr의 범위를 벗어나면 idx를 arr의 길이로 나눈 나머지로 초기화
#     if idx >= len(arr):
#         idx %= len(arr)
#     # idx에 해당하는 수를 result 리스트에 추가하고 arr에서 삭제
#     result.append(str(arr.pop(idx)))
#     # idx에 K를 더함
#     idx += K-1

# # 결과 리스트를 문자열로 변환하여 출력
# print("<" + ", ".join(result) + ">")




from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n+1))
ans = []

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())

print("<" + ", ".join(map(str, ans)) + ">")
