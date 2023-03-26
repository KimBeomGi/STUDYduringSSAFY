'''
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                print(i, j, ni, nj)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
for i in range(N):
    for j in range(N):
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                print(i, j, ni, nj)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
P = 3
for i in range(N):
    for j in range(N):
        for k in range(4):
            for l in range(1, P+1):
                ni = i + di[k] * l
                ni = j + dj[k] * l
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    print(i, j, ni, nj)
'''
'''
# bit =[0,0,0,0]
# for i in range(2):
#     bit[0] = i                          # 0번째 원소
#     for j in range(2):
#         bit[1] = j                      # 1번째 원소
#         for k in range(2):
#             bit[2] = k                  # 2번째 원소
#             for l in range(2):
#                 bit[3] = l              # 3번째 원소
#                 print_subset(bit)       #생성된 부분집합 출력

A =[1,2,3,4]
bit = [0]*4
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l 
                for p in range(4):
                    print(bit, end= '')
                    if bit[p]:
                        print(A[p], end = '')
                print()

A =[1,2,3,4]
bit = [0]*4
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit, end='')
                s=0
                for p in range(4):
                    if bit[p]:
                        print(A[p], end = '')
                        s += A[p]
                print()
'''
# arr = [3,6,7,1,5,4]
# n = len(arr)            # n: 원소의 개수

# for i in range(1<<n):                   # 1<<n : 부분 집합의 개수
#     for j in range(n):                  # 원소의 수만큼 비트를 비교함
#         if i & (1<<j):                  # i의 j번 비트가 1인 경우
#             print(arr[j], end = ', ')   # j번 원소 출력
#     print()
# print()

# from random import *
# print(randint(1,2))

# a = [1,2,3]
# b = (1,2,3)
# print(a*3)
# print(b*3)


# print(list(x**2 for x in range(5) if 2 < x))

# a, b=1, c=2

# 3 4 5
'''
a = ['april', 'automn', 'winter']
a.extend(['summer'])
a.extend('summer')
print(a)
'''

# arr = [
#     [1,2,3,4,5]
#     [2,3,4,5,6]
#     [3,4,5,6,7]
#     [4,5,6,7,8]
#     [5,6,7,8,9]
# ]
# 리스트 컴프레션???

# arr = [x for x in range(1,6)]
# arr = [x for x in range(2,7)]

# arr = [[x for x in range(a,a+5)] for a in range(1,6)]

# for row in arr:
#     print(row)

'''
arr = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7],
    [4,5,6,7,8],
    [5,6,7,8,9]
]
# 상하좌우
dr = [-1,1,0,0] # 상하좌우 행 변화량
dc = [0,0,-1,1] # 상하좌우 열 변화량

#시계방향 상 우 하 좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]
# 행 열의 변화량 쌍
d = [(-1,0), (1,0), (0,-1), (0,1)]

r, c = 2, 2
for a in range(4):   # 4방향 돌거니까 range(4)
    print(arr[r + dr[a]], [c + dc[a]])    # 현재 위치 + 가야할 곳에 따른 방향

r, c = 2, 2
d = [(-1,0), (1,0), (0,-1), (0,1)]
# for a in range(4):
#     r + d[a][0], c + d[a][1]
for d in [(-1,0), (1,0), (0,-1), (0,1)]:
    r + d[0], c + d[1]

for d in [(-1,0), (1,0), (0,-1), (0,1)]:
    r + dr, c + dc
'''

# a= [1,2,3]
# # 집합 a의 모든 부분집합 출력하기
# # 알고리즘에서 가장 기본적인 방법이 완전 탐색
'''
a = 2
b = 3
c = a & b 
d = a | b
e = a ^ b
print(c)
print(d)
print(e)

a = 2
b = 3
c = a << 2  # 왼쪽으로 2칸 이동
print(c)

'''
'''
arr = ['a','b','c']
# 모든 부분집합을 구하기 위해서 비트를 활용하자
# 요소가 3개니까 부분집합의 개수는 2**3
N = 3    # 0~7을 확인이 가능하겠다.
#for i in range(2**N): ↓ 밑에 녀석이랑 똑같다.
for i in range(1<<N):
 # i: 0~ 2**N-1, i의 비트 모양이 부분집합의 모양이다.
 # i의 모든 비트를 확인하자!!
    for j in range(N):
        if i & (1 << j) != 0:  # j번째 요소가 1이다! → j 번째 요소가 부분집합에 포함된다.
            print(arr[j], end='')
    print()

#    i & (1 << 0)
#    i & (1 << 1)
#    i & (1 << 2)
#    i & (1 << 3)
'''