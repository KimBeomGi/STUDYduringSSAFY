
# [문제]
# 사칙연산으로 구성되어 있는 식은 이진 트리로 표현할 수 있다. 아래는 식 “(9/(6-4))*3”을 이진 트리로 표현한 것이다.
# 임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의 결과에 해당 연산자를 적용한다.

# 사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진 트리가 주어질 때, 이를 계산한 결과를 출력하는 프로그램을 작성하라.
# 계산 중간 과정에서의 연산은 모두 실수 연산으로 한다.

# [입력]
# 총 10개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 줄에는 정점의 개수 N(1≤N≤1000)이 주어진다. 그다음 N 줄에 걸쳐 각 정점의 정보가 주어진다.
# 정점이 정수면 정점 번호와 양의 정수가 주어지고, 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호가 차례대로 주어진다.
# 정점 번호는 1부터 N까지의 정수로 구분된고 루트 정점의 번호는 항상 1이다.
# 위의 예시에서, 숫자 4가 7번 정점에 해당하면 “7 4”으로 주어지고, 연산자 ‘/’가 2번 정점에 해당하면 두 자식이 각각 숫자 9인 4번 정점과 연산자 ‘-’인 5번 정점이므로 “2 / 4 5”로 주어진다.

# [출력]
# 각 테스트케이스마다 '#t'(t는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 사칙연산을 계산한 결과값을 출력한다.
# 결과값은 소수점 아래는 버리고 정수로 출력한다.

import sys
sys.stdin = open('230223 9일차-사칙연산.txt','r')

# [문제풀이]
# 0. 후위 순회로 풀어보도록 하자.
# 1. 후위순회로 읽어서 리스트에 넣어준 후,
# 1-1. 스택을 이용해 풀어주었다.

# 후위 순회로 읽어내는 함수
def cal_postorder(A):
    if A == 0:                                  # 노드가 없으면(가리키는 값이 0이 되면) 볼필요가 없으니까 돌아가기
        return

    cal_postorder(tree[1][A])                   # 왼쪽 노드
    cal_postorder(tree[2][A])                   # 오른쪽 노드
    preorder_list.append(tree[0][A])            # 후위 순회를 읽어내어 preorder_list에 값 추가하기

# 입력값 받기
T = 10
for testcase in range(1,T+1):
    N = int(input())                            # 노드의 개수 N
    # 노드 번호와 양의 정수. 또는 노드 번호, 연산자, 노드의 왼쪽, 오른쪽자식 번호
    tree = [[0]*(N+1) for _ in range(3)]        # 노드 번호는 인덱스로 사용하고 나머지 내부 값 또는 연산자, 왼쪽 자식, 오른쪽 자식 번호에 대한 곳
    # 각 노드에 대한 값 입력받기
    for i in range(N):                          # N의 크기만큼 입력 받음
        temp = list(map(str, input().split()))  # 임시로 입력값을 받아 놓을 리스트
        M = len(temp)                           # 임시리스트의 길이 M
        temp[0] = int(temp[0])
        for j in range(M-1):                    # temp[0]는 인덱스로만 사용할 것이 기 때문에 M-번 반복
            tree[j][temp[0]] = temp[j+1]        # 내부 값 또는 연산자, 왼쪽, 오른쪽을 입력받는 행에 기입
    # str로 받은 것들 숫자로 바꿔주기
    for i in range(N+1):
        tree[1][i] = int(tree[1][i])
        tree[2][i] = int(tree[2][i])
        if tree[0][i] not in ['+', '-', '/', '*']:
            tree[0][i] = int(tree[0][i])
    # print(tree)
    preorder_list = []
    cal_postorder(1)
    # print(tree[0])
    # print(preorder_list)

# 스택으로 연산하기
    stack = [0]*(N)                                         # 스택생성
    top = -1                                                # 스택에 이용될 top 초기화
    for i in range(N):                                      # preorder_list에 있는 내용을 연산해주기 위한 반복문
        # 숫자
        if preorder_list[i] not in ['+', '-', '*', '/']:    # 숫자면
            top += 1                                        # top +1하고
            stack[top] = preorder_list[i]                   # 스택에 집어넣기
        # 연산자{(스택에 먼저들어간 값 (연산자) 나중에 들어간값)을 해줘야함}
        if preorder_list[i] == '+':                         # + 연산자면 더해주기
            stack[top-1] = stack[top-1] + stack[top]
            top -= 1
        elif preorder_list[i] == '-':                       # - 연산자면 빼주기
            stack[top-1] = stack[top-1] - stack[top]
            top -= 1
        elif preorder_list[i] == '*':                       # * 연산자면 빼주기
            stack[top-1] = stack[top-1] * stack[top]
            top -= 1
        elif preorder_list[i] == '/':                       # / 연산자면 빼주기
            stack[top-1] = stack[top-1] / stack[top]
            top -= 1
    print(f'#{testcase} {int(stack[top])}')                 # 실수가 아닌 정수로 출력해야하므로 int()이용