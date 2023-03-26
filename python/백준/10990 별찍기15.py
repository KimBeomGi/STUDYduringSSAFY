# 4
#    *
#   * *
#  *   *
# *     *

N = int(input())

for i in range(N):
    print(' '*(N-i-1),end='')
    print('*', end='')
    print(' '*(2*i-1), end='')
    if i !=0:
        print('*')
    else:
        print()