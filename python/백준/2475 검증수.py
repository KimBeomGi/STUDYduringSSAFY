A = list(map(int, input().split()))
B = 0
for i in A:
    B += i**2
B = B % 10
print(B)