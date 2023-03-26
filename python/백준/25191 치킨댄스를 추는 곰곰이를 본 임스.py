N = int(input())
A, B = map(int, input().split())

count = 0
while N > 0:
    if A >= 2:
        N -= 1
        A -= 2
        count += 1
    elif B >= 1:
        N -= 1
        B -= 1
        count += 1
    else:
        break
print(count)