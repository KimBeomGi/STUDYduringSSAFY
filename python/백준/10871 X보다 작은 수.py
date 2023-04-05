N, X = map(int, input().split())
problem = list(map(int, input().split()))
for i in problem:
    if i < X:
        print(i, end =' ')
print()