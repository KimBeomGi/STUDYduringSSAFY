dices = list(map(int, input().split()))
A = [0]*7               # 인덱스 0~6까지 생성
for i in range(3):
    A[dices[i]] += 1       # 해당 인덱스 값에 +1
prize = 0
max_same = 0
max_same_num = 0
for i in range(1, 7):
    if max_same <= A[i]:
        max_same = A[i]
        max_same_num = i
if max_same == 3:
    prize = 10000 + max_same_num*1000
elif max_same == 2:
    prize = 1000 + max_same_num*100
elif max_same == 1:
    prize = max_same_num*100
print(prize)