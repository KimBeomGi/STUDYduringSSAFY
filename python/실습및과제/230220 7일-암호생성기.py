# 다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.
# - 8개의 숫자를 입력 받는다.
# - 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 
# 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.
# 이와 같은 작업을 한 사이클이라 한다.
# - 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.

# [제약 사항]
# 주어지는 각 수는 integer 범위를 넘지 않는다.
# 마지막 암호 배열은 모두 한 자리 수로 구성되어 있다.
 
# [입력]
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고, 그 다음 줄에는 8개의 데이터가 주어진다.

# [출력]
# #부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.'


import sys
sys.stdin = open('230220 7일-암호생성기.txt','r')
# [문제풀이]

T = 10
for testcase in range(1, T+1):
    testcase = int(input())
    problem = list(map(int, input().split()))       # 8개의 숫자를 입력 받음
    N = len(problem)                                # 입력받은 problem의 길이 N
    problem.append(-1)                              # problem을 원형큐로 이용하기 위해 리스트에 값 추가
    front = 0                                       # 데이터들의 시작을 나타내는 front, 현재 시작 데이터의 위치가 [0]에 위치
    rear = N-1                                      # 데이터들의 끝을 나타내는 rear, 현재 마지막 데이터의 위치가 [N-1]에 위치

    while problem[rear] > 0:                        # problem[rear]가 0 이상일때만 반복문 실시, 즉 마지막 데이터 값이 0 이상이어야함
        for i in range(1,6):                        # 1감소, 2감소, 3감소, 4감소, 5감소 식이기 때문에 1~5를 반복하는 for문 이용
            rear = (rear+1)%(N+1)                   # 원형큐에 이용해야하기에 rear를 +1해주되 인덱스가 이동될 수 있으므로 모듈러 이용. (N+1)은 원형큐로 사용하기 위해 공간 값이 더 있기 때문
            problem[rear] = problem[front] - i      # 마지막데이터 값을 시작 데이터값에서 i를 빼준만큼의 값으로 설정
            front = (front+1)%(N+1)                 # 원형큐에 이용해야하기에 rear를 +1해주되 인덱스가 이동될 수 있으므로 모듈러 이용. (N+1)은 원형큐로 사용하기 위해 공간 값이 더 있기 때문
            if problem[rear] <= 0:                  # 만약 마지막 데이터 값이 0이하라면
                problem[rear] = 0                   # 0으로 만들고 for문 정지
                break
    # print(front)
    # print(rear)
    print(f'#{testcase}', end = ' ')                # 테스트케이스를 출력하고 이어서 출력
    if front < rear:                                # 인덱스값이 front가 rear보다 작다면, 즉 선형으로 있다면
        for i in range(front,rear+1):               # [front]~[rear]까지 출력
            print(f'{problem[i]}', end = ' ')

    elif front > rear:                              # front가 rear보다 크다면, 선형이 아닌 원형으로 눈을 돌려야하니까
        for i in range(front, N+1):                 # front~ 리스트 끝까지
            print(f'{problem[i]}', end = ' ')
        for j in range(rear+1):                     # 앞선 front에 이어서 [0]~[rear]까지 출력
            print(f'{problem[j]}', end = ' ')
    print()                                         # 정답을 출력하는데 end =''로 인해 문제가 생기는 것 방지