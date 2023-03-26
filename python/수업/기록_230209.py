p = 'ab'                # 찾을 패턴
t = 'aaaab'   # 전체 문장
M = len(p)              # 찾을 패턴의 길이
N = len(t)              # 전체 문장의 길이

# def bf(p, t, N, M):
#     i = 0       # t에서의 위치
#     j = 0       # p에서의 위치
#     while i < N and j < M:  # 비교할 문장이 남아있고, 패턴을 찾기 전이면
#         if t[i] == p[j]:
#             i += 1
#             j += 1
#         else:
#             i = i-j+1
#             j =0
#         # if t[i] != p[j]:    # 서로 다른 글자를 만나면
#         #     i = i-j         # 비교를 시작한 위치로
#         #     j = -1          # 패턴의 시작 전으로
#         # i += 1
#         # j += 1
#     if j == M:              # 패턴을 찾은 경우
#         return i - M
#     else:
#         return -1
# print(bf(p, t, N ,M))

def bf2(p, t, N, M):
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return -1

print(bf2(p, t, N ,M))