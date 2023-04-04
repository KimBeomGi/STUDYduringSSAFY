# 문제
# N명의 학생들이 모인 초등학교 반에서 학급회장 선거를 하려고 한다. 그 중 3명이 회장후보로 나왔고,
# 이들에 대한 선호도를 N명의 학생들 각각에게 적어내도록 하였다. 세 명의 후보는 후보 1번, 후보 2번, 후보 3번이라 한다.
# 모든 학생은 3명의 후보 중에서 가장 선호하는 후보에게는 3점, 두 번째로 선호하는 후보에게는 2점, 가
# 장 선호하지 않는 후보에게는 1점을 주어야 한다. 3명의 후보에 대한 한 학생의 선호 점수는 모두 다르며, 1점, 2점, 3점이 정확히 한 번씩 나타나야 한다. 
# 후보의 최종 점수는 학생들로부터 받은 자신의 선호도 점수를 모두 더한 값이 된다. 
# 그러면 3명의 후보 중 가장 큰 점수를 받은 후보가 회장으로 결정된다. 
# 단, 점수가 가장 큰 후보가 여러 명인 경우에는 3점을 더 많이 받은 후보를 회장으로 결정하고, 
# 3점을 받은 횟수가 같은 경우에는 2점을 더 많이 받은 후보를 회장으로 결정한다. 
# 그러나 3점과 2점을 받은 횟수가 모두 동일하면, 1점을 받은 횟수도 같을 수밖에 없어 회장을 결정하지 못하게 된다.
# 여러분은 선호도 투표를 통해 얻은 세 후보의 점수를 계산한 후, 
# 유일하게 회장이 결정되는 경우에는 회장으로 결정된 후보의 번호(1, 2, 3 중 한 번호)와 최고 점수를 출력하고, 
# 회장을 결정하지 못하는 경우에는 번호 0과 최고 점수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 반의 학생들의 수 N (3 ≤ N ≤ 1,000)이 주어진다. 
# 다음 N개의 각 줄에는 각 학생이 제출한 회장후보 3명에 대한 선호 점수가 주어지는 데, 
# 첫 번째 점수는 후보 1번에 대한 점수이고 두 번째 점수는 후보 2번에 대한 점수이고 세 번째 점수는 후보 3번에 대한 점수이다. 이 세 점수는 서로 다르며, 1, 2, 3이 정확히 한 번씩 나타난다. 

# 출력
# 학생들의 선호도 투표 결과로부터, 회장이 유일하게 결정되는 경우에는 회장으로 결정된 후보의 번호와 최고 점수를 출력하고, 
# 유일하게 결정할 수 없는 경우에는 0과 최고 점수를 출력한다.

# N = int(input())
# A = []
# B = []
# C = []

# for i in range(N):
#     a,b,c = map(int, input().split())
#     A.append(a)
#     B.append(b)
#     C.append(c)
# A_score = sum(A)
# B_score = sum(B)
# C_score = sum(C)
# scores = [A_score, B_score, C_score]
# A3 = A.count(3)
# A2 = A.count(2)
# B3 = B.count(3)
# B2 = B.count(2)
# C3 = C.count(3)
# C2 = C.count(2)
# three = [A3, B3, C3]
# two = [A2,B2,C2]
# high = max(scores)
# high_count = scores.count(high)
# idx = 0
# if high_count == 1:
#     for i in range(len(scores)):
#         if scores[i] == high:
#             idx == i
# else:
#     for i in range(len(scores)):
#         if scores[i] == high and three.count(max(three)) == 1 and three[i] == max(three):
#             idx = i

# n = int(input())
# score =[0]*3
# check =[0]*3
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     score[0] += a
#     score[1] += b
#     score[2] += c
#     check[0] += a*a
#     check[1] += b*b
#     check[2] += c*c
# m = max(score)
# mc = max(check)
# cnt = 0
# for i in range(3):
#     if mc == check[i]:
#         cnt+=1
# if cnt > 1:
#     print('0 '+ '%d' %m)
#     exit(0)
# if max(check) == check[0]:
#     print('1 '+ '%d' %m)
# elif max(check) == check[1]:
#     print('2 '+ '%d' %m)
# elif max(check) == check[2]:
#     print('3 '+ '%d' %m)


################################
N =int(input())
scores = [0]*3
check = [0]*3
for _ in range(N):
    score = list(map(int,input().split()))
    for i in range(3):
        scores[i] += score[i]
        check[i] += (score[i]**2)
high = max(scores)
high_check = max(check)
count = 0
for i in range(3):
    if high_check == check[i]:
        count+=1

if count > 1:
    print(f'0 {high}')
    exit(0)
if max(check) == check[0]:
    print(f'1 {high}')
elif max(check) == check[1]:
    print(f'2 {high}')
elif max(check) == check[2]:
    print(f'3 {high}')