# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

N = int(input())
for i in range(1,N+1):
    print('*'*i, end='')
    print(' '*(N-i)*2, end='')
    print('*'*i,)

for i in range(N-1,0,-1):
    print('*'*i, end='')
    print(' '*(N-i)*2, end='')
    print('*'*i,)