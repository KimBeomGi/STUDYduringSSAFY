# def f(i, k, s,key):
#     global cnt
#     global c
#     c+=1

#     if i==k:
#         if s==key:
#             print(bit)
#             cnt+=1
#     else:
#         bit[i] =0
#         f(i+1, k, s, key)           # A[i] 미포함
#         f(i+1, k, s+A[i], key)      # A[i] 포함

# A= [i for i in range(1, 11)]
# N = 10
# bit = [0]*N
# key = 10
# cnt = 0
# c = 0
# f(0, N, 0, key)
# print(cnt, c)

##############

# def f(i, k, s,key):
#     global cnt
#     global c
#     c+=1
#     if s==key:
#         cnt +=1
#         return
#     elif i ==k or s > key:
#         return
#     else:
#         bit[i] =0
#         f(i+1, k, s, key)           # A[i] 미포함
#         f(i+1, k, s+A[i], key)      # A[i] 포함
#         return

# A= [i for i in range(1, 11)]
# N = 10
# bit = [0]*N
# key = 1
# cnt = 0
# c = 0
# f(0, N, 0, key)
# print(cnt, c)

# ############################

def f(i, k, s,key,rs):
    global cnt
    global c
    c+=1
    if s==key:
        cnt +=1
        return
    elif i ==k or s > key or s+rs<key:
        return
    else:
        bit[i] =0
        f(i+1, k, s, key, rs -A[i])           # A[i] 미포함
        f(i+1, k, s+A[i], key, rs -A[i])      # A[i] 포함
        return

A= [i for i in range(1, 11)]
N = 10
bit = [0]*N
key = 10
cnt = 0
c = 0
f(0, N, 0, key, sum(A))
print(cnt, c)