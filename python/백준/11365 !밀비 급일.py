secrets = []
while True:
    A = input()

    if A =='END':
        break
    secrets.append(A)

N = len(secrets)
for i in range(N):
    for j in range(len(secrets[i])-1,-1,-1):
        print(secrets[i][j], end='')
    print()