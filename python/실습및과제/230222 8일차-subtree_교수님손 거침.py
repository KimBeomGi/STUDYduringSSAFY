# [문제]
# 트리의 일부를 서브 트리라고 한다.
# 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
# 주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.
# 이런 경우의 트리는 부모 노드를 인덱스로 다음과 같은 방법으로 나타낼 수 있다. 자식 노드가 0인 경우는 노드가 자식이 없는 경우이다.

# 부모    인덱스
# 왼쪽자식    리스트
# 오른쪽자식    리스트


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
# 노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open('230222 8일차-subtree.txt','r')

# [문제풀이]
# 0. 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 구해야한다.
# 0-1. 간선의 갯수 E, 문제풀이에 사용될 노드 N이 주어진다. E개의 부모-자식 노드 쌍이 다음줄에 주어지며
# 0-2. 노드 번호는 1~ E+1까지 존재, 간선의 갯수는 총 노드의 갯수보다 1개 적게 주어지니까. 노드는 간선 + 1

# def find_child_num(N, family_nodes):                        # 자식 노드를 찾아라!!!!
#     global nodes_family_num                                 # global에 있는 nodes_family_num을 이용
    
#     if family_nodes[0][N] == 0 and family_nodes[1][N] == 0: # 만약 왼쪽도 오른쪽도 자식이 없다면 
#         return nodes_family_num                             # 더 찾지 말고 돌아가자.

#     if family_nodes[0][N] != 0:                             # 해당 부모한테서 왼쪽 자식이 있으면
#         nodes_family_num += 1                               # 가족 수에 +1
#     if family_nodes[1][N] != 0:                             # 해당 부모한테서 오른쪽 자식이 있으면
#         nodes_family_num += 1                               # 가족 수에 +1
    
#     find_child_num(family_nodes[0][N], family_nodes)        # 왼쪽 자식노드에서 다시 자식 찾기
#     find_child_num(family_nodes[1][N], family_nodes)        # 오른쪽 자식노드에서 다시 자식 찾기
#     return nodes_family_num                                 # 세아려진 nodes_family_num를 반환


def find_child_num(N, family_nodes):                        # 자식 노드를 찾아라!!!!
    # global nodes_family_num                                 # global에 있는 nodes_family_num을 이용
    cnt = 1
    if family_nodes[0][N] == 0 and family_nodes[1][N] == 0: # 만약 왼쪽도 오른쪽도 자식이 없다면 
        return 1

    if family_nodes[0][N] != 0:                             # 해당 부모한테서 왼쪽 자식이 있으면
        cnt += find_child_num(family_nodes[0][N], family_nodes)                               # 가족 수에 +1
    if family_nodes[1][N] != 0:                             # 해당 부모한테서 오른쪽 자식이 있으면
        cnt += find_child_num(family_nodes[1][N], family_nodes)                               # 가족 수에 +1
    
    # find_child_num(family_nodes[0][N], family_nodes)        # 왼쪽 자식노드에서 다시 자식 찾기
    # find_child_num(family_nodes[1][N], family_nodes)        # 오른쪽 자식노드에서 다시 자식 찾기
    return cnt 



T = int(input())
for testcase in range(1, T+1):
    E, N = map(int, input().split())                            # 간선의 갯수 E와 문제의 key가 될 노드 번호
    input1 = list(map(int, input().split()))                    # 최초 주어지는 값을 리스트에 입력받아두기
    family_nodes = [[0]*(E+2) for _ in range(2)]                # 노드 번호를 인덱스로 그대로 활용하기 위해서 노드+1개 길이의 리스트를 만들고
                                                                # 왼쪽 오른쪽 자식이 있으므로 2개 만들기
    for i in range(0, E*2, 2):
        if family_nodes[0][input1[i]] == 0:                     # 부모노드를 가리키는 인덱스의 위치에 따른 왼쪽 자식노드 자리가 비어있으면
            family_nodes[0][input1[i]] = input1[i+1]            # 부모노드를 가리키는 인덱스의 위치에 자식노드를 집어 넣음
        elif family_nodes[0][input1[i]] != 0:                   # 해당 부모노드의 왼쪽 자식노드 자리가 차 있으면
            family_nodes[1][input1[i]] = input1[i+1]            # 오른쪽 자식노드에다가 해당 값을 기입

    nodes_family_num = 1                                        # 해당 노드의 자신과 자식과 손자들의 수를 세아리는 변수

    A = find_child_num(N, family_nodes)                         # 함수 실행
    print(f'#{testcase} {A}')