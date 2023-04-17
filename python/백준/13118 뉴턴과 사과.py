# p1, p2, p3, p4 = map(int, input().split())
a = list(map(int, input().split()))
x, y, r = map(int, input().split())

answer = 0
for i in range(len(a)):
    if a[i] == x:
        answer = i+1
        break
print(answer)