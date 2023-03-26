N = int(input())
stars = []
space = []
for i in range(N):
    space.append(' '*(N-i-1))
    if i == 0:
        stars.append('*')
    else:
        stars.append('*'*(i*2+1))

stars_r = []
space_r = []
for i in range(0,N-1):
    stars_r.append(stars[N-i-1])
    space_r.append(space[N-i-1])

# print(stars)
# print(space)
# print(stars_r)
# print(space_r)

for i in range(N-1):
    print(space_r[i],end='')
    print(stars_r[i])

for i in range(N):
    print(space[i],end='')
    print(stars[i])