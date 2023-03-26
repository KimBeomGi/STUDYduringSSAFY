
# [문제]
# 이진 최소힙은 다음과 같은 특징을 가진다.
#     - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
#     - 부모 노드의 값<자식 노드의 값을 유지한다. 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
#     - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.
# 예를 들어 7, 2, 5, 3, 4, 6이 차례로 입력되면 다음과 같은 트리가 구성된다.
# 이때 마지막 노드인 6번의 조상은 3번과 1번 노드이다.
# 1000000이하인 N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고, 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성하시오.

# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 N이 주어지고, 다음 줄에 1000000이하인 서로 다른 N개의 자연수가 주어진다. 5<=N<=500

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다

import sys
sys.stdin = open('230223 8일차-이진 힙.txt','r')

# [문제풀이]
# 0. 최소힙을 이용한 문제이다.
# 0-1.따라서 주어지는 입력값을 힙이 되도록 해주며, 최소힙이므로 '부모노드의 값 < 자식 노드의 값'으로 해준다.
# 0-2.에서 7,2,5,3,4,6이 주어졌지만 만들어진 것은 1~6노드번호로 보일시 2,3,5,7,4,6 이다.
# 1.이때 마지막 노드는 6번이고, 이 6번의 조상은 1번 3번 노드이고 그 값은 2와 5이므로 합 7이 출력해야하는 값이다.
# 2. 전위 순회로 문제를 풀이 하면 가능할 것으로 보인다.

# heap에 값을 넣으면서 정렬하는 함수
def heap_push(A):
    global heapcount                            # global에서 heapcount를 들고
    heapcount += 1                              # heapcount에 +1
    tree[heapcount] = A                         # heap의 마지막 노드에 입력값을 추가
    # 마지막 노드 부터 위로 올라가며 비교
    parent = heapcount//2                       # 부모 노드는 자식노드//2의 번호이므로.(마지막값에서 확인)       
    current = heapcount                         # 현재 위치는 마지막 값인 heapcount이므로
    while tree[parent] > tree[current]:         # 최솟값 heap이므로 tree[parent] > tree[current]일 때만 변경되도록하잔
        tree[parent], tree[current] = tree[current], tree[parent]
        current = parent                        # 바꿔줬으면, 내 위에 부모랑도 확인 해줘야하는데 내가 원래 부모 자리로 옮겼으니까.
        parent = current//2                     # 변경된 내 위치에서 부모는 나 //2 의 위치에 있으니까

# 조상노드 값 합하기
def parents_sum(N):
    global sum_v                                # global에서 sum_v 가져오기
    if  N//2 == 0:                              # 노드 번호 N//2==0이면 root니까 돌아가.
        return
    sum_v += tree[N//2]                         # sum_v에 부모노드 값을 더해주자.
    parents_sum(N//2)                           # 재귀함수로 부모에 부모를 보자.
    
T = int(input())
for testcase in range(1, T+1):
    N = int(input())                            # 노드의 갯수 N을 입력받음
    tree = [0]*(N+1)                            # 리스트의 인덱스를 이용할 것이기 때문에 N+1로 해준다.
    in_value = list(map(int,input().split()))   # 우선 입력값을 리스트로 받아둠
    heapcount = 0                               # 입력값을 입력할때마다 증가되면서 현재 입력받은 마지막을 가리키는 heapcount
    for i in range(N):                          # heap하게 입력해주기 위한 반복문
        heap_push(in_value[i])                  # heap_push를 이용해 일반tree를 heap하게 만들어줌
    sum_v = 0                                   # 조상노드의 값을 합하기 위한 sum_v
    # print(tree)
    parents_sum(N)
    print(f'#{testcase} {sum_v}')