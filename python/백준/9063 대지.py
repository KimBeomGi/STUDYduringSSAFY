# import sys

# N = int(sys.stdin.readline().strip())
# rectang = []
# for i in range(N):
#     rectang.append(list(map(int, sys.stdin.readline().strip().split())))
# rectang.sort()
# min_x = rectang[0][0]
# max_x = rectang[-1][0]
# # strings_s = sorted(strings, key=lambda x:(len(x),x))
# rectang = sorted(rectang, key=lambda x:x[1],)
# print(rectang)
# min_y = rectang[0][1]
# max_y = rectang[-1][1]

# A = max_x-min_x
# B = max_y-min_y
# print(A*B)



# 따로따로
import sys

N = int(sys.stdin.readline().strip())
rectang_x = []
rectang_y = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    rectang_x.append(x)
    rectang_y.append(y)
min_x = min(rectang_x)
max_x = max(rectang_x)
min_y = min(rectang_y)
max_y = max(rectang_y)

A = max_x-min_x
B = max_y-min_y
print(A*B)