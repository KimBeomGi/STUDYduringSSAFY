# 이건 중복체크 안된거
# N = 3
# arr = [1,2,3]
# perm_arr = [0]*N
# # idx 번째에 넣을 수 있는 수자 다 넣기
# def perm(idx):
#     if idx==N:
#         print(perm_arr)
#         return
#     for i in range(N):
#         perm_arr[idx] = arr[i]
#         perm(idx+1)
# perm(0)


# N = 3
# arr = [1,2,3]
# perm_arr = [0]*N
# used = [0]*N
# # idx 번째에 넣을 수 있는 수자 다 넣기
# def perm(idx):
#     if idx==N:
#         print(perm_arr)
#         return
#     for i in range(N):
#         if not used[i]:                 # used[i]가 0일때
#             perm_arr[idx] = arr[i]
#             used[i] = 1
#             perm(idx+1)
#             used[i] = 0                 # i번째 사용하고나서 사용완료했으니 이제 다른 값 찾아야해서 반납(?)
# perm(0)


# N = 3
# arr[1,2,3]
# perm_arr = [0]*N
# used = [0]*N

# def perm(idx):
#     if idx == N:
#         print(perm_arr)
#         return
#     for i in range(N):
#         if not used[i]:
#             perm_arr[idx] = arr[i]
#             used[i] = 1
#             perm(idx+1)
#             used[i] = 0
# perm(0)


# N = 3
# arr=[1,2,3]
# perm_arr = [0]*N
# used = [0]*N

# def perm(idx):
#     if idx == N:
#         print(perm_arr)
#         return
#     for i in range(N):
#         if not used[i]:
#             perm_arr[idx] = arr[i]
#             used[i] = 1
#             perm(idx+1)
#             used[i] = 0
# perm(0)


# N = 3
# arr=[1,2,3]
# perm_arr = [0]*N
# used = [0]*N

# def perm(idx):
#     if idx == N:
#         print(perm_arr)
#         return
#     for i in range(N):
#         if used[i] == 0:
#             perm_arr[idx] = arr[i]
#             used[i] = 1
#             perm(idx+1)
#             used[i] = 0
# print(perm(0))

# N = 3
# arr=[1,2,3]
# perm_arr = [0]*N
# used = [0]*N

# def perm(idx):
#     if idx == N:
#         print(perm_arr)
#         return
#     for i in range(N):
#         if not used[i]:
#             perm_arr[idx] = arr[i]
#             used[i] = 1
#             perm(idx+1)
#             used[i] = 0
# perm(0)

N = 3
arr=[1,2,3]
perm_arr = [0]*N
used = [0]*N

def perm(idx):
    if idx == N:
        print(perm_arr)
        return
    for i in range(N):
        if used[i] == 0:
            perm_arr[idx] = arr[i]
            used[i] = 1
            perm(idx + 1)
            used[i] = 0
perm(0)