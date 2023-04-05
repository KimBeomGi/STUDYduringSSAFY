problem = list(map(int,input().split()))

answer = ''
for i in range(8):
    if i == 0:
        if problem[0] == 1:
            answer = 'ascending'
        elif problem[0] == 8:
            answer = 'descending'
        else:
            answer = 'mixed'
            break
    if i>0 and answer == 'ascending':
        if problem[i] - problem[i-1] != 1 :
            answer = 'mixed'
            break
    elif i>0 and answer == 'descending':
        if problem[i-1] - problem[i] != 1 :
            answer = 'mixed'
            break
print(answer)