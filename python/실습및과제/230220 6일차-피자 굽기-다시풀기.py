# N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.
# 1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.
# 주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.

# - 피자는 1번위치에서 넣거나 뺄 수 있다.
# - 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
# - M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
# - 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.
# 3<=N<=20, N<=M<=100, 1<=Ci<=20

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.

import sys
sys.stdin = open('230220 6일차-피자 굽기-다시풀기.txt','r')


T = int(input())                
for testcase in range(1,T+1):
    N, M = map(int, input().split())                # 화덕의 갯수 N, 피자갯수 M 입력받음
    # current = 0                                 
    Ci = list(map(int, input().split()))            # Ci 피자마다 치즈 양
    queue = [None]*2984520                          # 선형 큐로 이용하기 위해서
    front = rear = -1                               # front와 rear를 -1로 설정
    for i in range(N):                              # i를 인자로 N만큼 반복
        rear += 1                                   # rear를 1, 한칸 뒤로 보내고
        queue[rear] = [i+1, Ci[i]]                  # queue[rear]에 [i+1, Ci[i]]를 넣음으로 피자번호와 피자치즈를 기입
        idx = i                                     # 피자 치즈가 다 녹았을 때 사용할 idx = i로 설정
    
    # 화덕에 넣고 확인하면서 피자 치즈 녹이기
    while front != rear:                            # 프론트가 rear와 만나지 않는다면, 즉 값이 떨어지지 않는다면
        front += 1                                  # front를 1, 한칸 뒤로 보내고
        if queue[front][1] == 0:                    # queue[front]의 피자 치즈양이 0이라면
            continue                                # 다시 while문으로 가자
        
        # 피자 치즈를 화덕에서 반쯤 녹이고, 다 녹았다고 확인되면, 해당 피자 빼고, 새 피자 넣어주기
        rear += 1                                   # rear를 뒤로 한 칸 보내고
        queue[rear] = [queue[front][0], queue[front][1] // 2]       # queue[rear]에 queue[front]의 번호와 반이녹은 치즈를 기입
        if queue[rear][1] == 0:                     # 만약 queue[rear]의 치즈가 다 녹았으면
            idx += 1                                # idx에 +1을 해주고
            if idx < M:                             # idx가 M보다 작다면
                rear += 1                           # rear에 +1을 해주자.
                queue[rear] = [idx+1, Ci[idx]]      # queue[rear]에 대기하고 있던 피자를 넣어주자.
    print(f'#{testcase} {queue[rear][0]}')
