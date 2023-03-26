# yeon_name = input()         # 연두이름
# N = int(input())            # 팀명 갯수
# names = [list(map(str, input())) for _ in range(N)]     # 이름 N개를 입력받음

# num = [0]*N                 # 각 팀명마다의 점수를 기입할 num 리스트
# for i in range(N):          # N번 반복
#     A = []                  # A라는 리스트로 각 단어의 철자에 대한 이름 철자와 팀명 철자의 합을 넣을 리스트
#     for j in range(len(yeon_name)):                 # 연두의 이름의 철자를 돌림
#         for k in range(len(names[i])):              # 팀명의 철자를 돌림
#             A.append(yeon_name[j]+names[i][k])      # A에 넣기
        
#     score=1
#     for o in A:
#         socre = score * o                           # 현재 score에 * O인자를 해주고
#     num[i] = score%100

# max_num = 0
# what_num = 0
# for i in range(N):
#     if max_num < num[i]:
#         max_num = num[i]
#         what_num = i

# print(''.join(names[what_num]))

##########################################
yeondu = input()         # 연두이름
yeondu_set = set(yeondu)
yeondu_set = sorted(list(yeondu_set))
y_n = len(yeondu_set)
N = int(input())            # 팀명 갯수
names = sorted([list(map(str, input())) for _ in range(N)])     # 이름 N개를 입력받음
# print(yeondu_set)
# print(names)

# num = [0]*N               # 각 팀명마다의 점수를 기입할 num 리스트
B = []                      # A를 기입할 B
if N >1:
    for i in range(N):          # N번 반복
        A = []                  # A라는 리스트로 각 단어의 철자에 대한 이름 철자와 팀명 철자의 합을 넣을 리스트
        for j in range(y_n-1):  # 연두의 이름길이만큼 반복문을 돌리기(0~y_n-2까지 반복(첫요소))
                                # 연두 이름의 해당 철자의 개수를 각 더하기
            # A.append((yeondu.count(yeondu_set[j]) + names[i].count(yeondu_set[j]))+(yeondu.count(yeondu_set[j+1]) + names[i].count(yeondu_set[j+1])))
            for k in range(j+1, y_n):   # j+1~ y_n-1까지 반복(다음요소)
                A.append((yeondu.count(yeondu_set[j]) + names[i].count(yeondu_set[j]))+(yeondu.count(yeondu_set[k]) + names[i].count(yeondu_set[k])))
    #     print(A)
        B.append(A)
    # print(B)
elif N == 1:
    for i in range(N):
        A=[]
        A.append((1)+names[i].count(yeondu))
        B.append(A)

max_num = 0
max_i = 0
for ct in range(N):                 # 
    count = 1                       #
    for m in range(len(B[0])):      #
        count = count * B[ct][m]    #
    count = count % 100             #
    if max_num < count:             #
        max_num = count             #
        max_i = ct                  #
    # print(count)
print(''.join(names[max_i]))




# yeondu = 'strongbaby'
# yeondu_set= set(yeondu)
# yeondu_set = list(yeondu_set)
# print(yeondu_set)
# yeondu_set_n = len(yeondu_set)
# for i in range(yeondu_set_n):
#     print(yeondu_set[i])
