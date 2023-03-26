N = int(input())
stars = []
space = []
for i in range(N):
    space.append(' '*(N-i-1))
    if i == 0:
        stars.append('*')
    else:
        stars.append('*'*(i*2+1))
# print(stars)
# print(space)
for i in range(N):
    print(space[i],end='')
    print(stars[i])