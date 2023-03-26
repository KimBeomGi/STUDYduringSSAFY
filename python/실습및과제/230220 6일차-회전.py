import sys
sys.stdin = open('230220 6일차-회전.txt', 'r')


# N개의 숫자로 이루어진 수열이 주어진다. 
# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=20, N<=M<=1000,

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.

# [문제풀이]
# 0. '큐'를 이용해보자.
# 1. 그 중 선형큐 대신 원형큐를 이용해보자.
# 2. 주어진 값 그대로 원형큐를 사용할 수는 없으니, 주어진 값으로 리스트를 만들고, 해당 리스트에 값 1개를 추가해주자.
# 3. 반복을 해줘야하는데 아무래도 재귀함수가 적절할 듯하니 재귀함수를 이용해보자.

def rotation(M):                            # def
    global front                            # global에서 front를 가져오기
    global rear                             # global에서 rear를 가져오기
    
    if M == 0:                              # M이 0이 되면, 즉 문제에서 주어진 M번 이동이 끝나면
        return                              # 나를 호출한 값으로 돌아가자.
    
    # 값 넣기
    rear = (rear+1)%(N+1)                   # rear의 위치, 원형큐여서 계속 위치가 돌아가니까 %를 이용. (N+1)은 요소 1개가 추가됐으니까
    perm[rear] = perm[front]                # 문제의 내용에 따라 제일 앞의 값을 제일 뒤에 추가해야 되니까.
    front = (front+1)%(N+1)                 # front의 위치, 원형큐여서 계속 위치가 돌아가니까 %를 이용. (N+1)은 요소 1개가 추가됐으니까
    rotation(M-1)                           # M번 반복해야하니까 M-1일때로 들어가보자.
    return perm[front]                      # rotation함수를 M번 반복했으면 제일 앞의 값을 출력해야하니까 perm[front]를 출력하자.


T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())        # 숫자갯수 N과 작업횟수 M을 받음
    perm = list(map(int, input().split()))  # 입력값 받기
    perm.append(0)                          # 원형큐로 이용할 것이기 때문에 요소가 하나 더 필요해서 0을 추가
    front = 0                               # 데이터의 첫 지점을 나타내는 front
    rear = N-1                              # 데이터의 끝 지점을 나타내는 rear

    print(f'#{testcase} {rotation(M)}')     # 출력