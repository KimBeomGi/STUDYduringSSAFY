N = 5

agents = [input() for _ in range(N)]

A = []
for i in range(N):
    for j in range(len(agents[i])-2):
        if agents[i][j] == 'F':
            if agents[i][j+1] =='B':
                if agents[i][j+2] == 'I':
                    A.append(str(i+1))
                    break                   # FBI가 여러번 나오게된다면 중복해서 확인하니까 그럴필요 없으므로 break
if not A:
    print("HE GOT AWAY!")
if A:
    print(' '.join(A))