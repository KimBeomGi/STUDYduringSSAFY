
# 주어진 트리를 in-order 형식으로 순회해 각 노드를 읽으면 특정 단어를 알 수 있다.
 
#  위 트리를 in-order 형식으로 순회할 경우 SOFTWARE 라는 단어를 읽을 수 있다.
# 주어진 트리를 in-order 형식으로 순회했을때 나오는 단어를 출력하라.

# [제약 사항]
# 트리는 완전 이진 트리 형식으로 주어지며, 노드당 하나의 문자만 저장할 수 있다.
# 노드는 아래 그림과 같은 순서로 주어진다.

# [입력]
# 총 10개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 줄에는 트리가 갖는 정점의 총 수 N(1≤N≤100)이 주어진다. 그 다음 N줄에 걸쳐 각각의 정점 정보가 주어진다.
# 정점 정보는 해당 정점의 문자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호 순서로 주어진다.
# 정점 번호는 1부터 N까지의 정수로 구분된다. 정점 번호를 매기는 규칙은 위 와 같으며, 루트 정점의 번호는 항상 1이다.
# 위의 예시에서,  알파벳 ‘F’가 2번 정점에 해당하고 두 자식이 각각 알파벳 ‘O’인 4번 정점과 알파벳 ‘T’인 5번 정점이므로 “2 F 4 5”로 주어진다.
# 알파벳 S는 8번 정점에 해당하므로 “8 S” 로 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

import sys
sys.stdin = open('230222 9일차-중위순회.txt','r')
# [문제풀이]
# 0. inorder형식으로 순회할 경우 출력해야한다.

# first[i][0] 이건 인덱스
# first[i][1] 이건 문자
# first[i][2] 이건 왼쪽노드 위치
# first[i][3] 이건 오른쪽노드 위치

def inorder(T):                                     # 중위 순회 함수 작성
    if T == 0:                                      # T == 0 이면
        return                                      # 집으로 돌아가.
    
    inorder(tree[1][T])                             # 왼쪽 자식을 찾으러 감
    answer.append(tree[0][T])                       # 중위 순회니까, 왼쪽자식 다 찾아 봤으면 내 할 일 먼저 하자. 그리고 오른쪽 찾으러 가야지.
    inorder(tree[2][T])                             # 오른쪽 자식을 찾으러 감
    return answer

T = 10
for testcase in range(1,T+1):
    # 입력값 받음
    N = int(input())                                # 노드의 갯수 N
    tree = [[0]*(N+1) for _ in range(3)]            # 0~N+1까지의 인덱스가 있는 리스트를 3개 만들고 tree안에 넣음
    for i in range(N):                              # N 횟수만큼 반복해서 입력값을 tree에 집어넣어주기위한 반복문
        temp = list(map(str, input().split()))      # temp라는 임시리스트 생성
        temp[0] = int(temp[0])                      # str로 모든 값을 받았기에 인덱스로 이용하기 위해 temp[0]를 int로 변환
        for j in range(len(temp)-1):                # 맨 앞의 숫자는 열(인덱스)에 활용이라 temp길이 -1만큼만 이용하면 된다.
            tree[j][temp[0]] = temp[j+1]            # 예로 tree[0][1] = temp[1], tree[1][1] = temp[2]과 같은 식임
    
    # tree[1], [2]를 int화 작업
    for i in range(2):                              # 왼쪽노드, 오른쪽노드를 가지는 행만 int로 바꾸면 되므로 2.
        for j in range(N+1):                        # 노드의 갯수+1 만큼 반복
            tree[i+1][j] = int(tree[i+1][j])        # tree[왼쪽 또는 오른쪽][해당노드 번호]를 str로 되어있던 숫자를 int로 바꿈
    answer = []                                     # def inorder에 사용될 answer 리스트
    output_string = inorder(1)                      # inorder(1)을 함으로써 1번 노드로부터 찾은 모든 자식 노드의 값을 기입한 output_string
    output_answer = ''.join(output_string)          # 리스트로 되어있는 output_string을 문자열로 바꿈

    print(f'#{testcase} {output_answer}')