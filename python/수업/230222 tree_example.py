# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# 부모노드의 번호를 인덱스로 하는 (2*V+1)배열 만들어서
# 왼쪽과 오른쪽 자식 노드 번호를 저장.
V = int(input())
tree = [[0]*(V+1) for _ in range(2)]        # 각 노드의 관계를 넣을 리스트 tree[0]은 왼쪽 자식입력 tree[1]은 오른쪽 자식입력
data = list(map(int, input().split()))
for i in range(0,(V-1)*2,2):
    p,c = data[i], data[i+1]                # 부모, 자식을 읽어옴
    #p번의 자식이 처음 나왔으면 왼쪽에 넣어주기, 2번째 나왔으면 오른쪽 자식.
    if not tree[0][p]:                      # 왼쪽 자식이 아직 없으면.. 왼쪽 자식.
        tree[0][p] = c
    else:                                   # 왼쪽 자식이 있으면 오른쪽 자식.
        tree[1][p] = c

# 트리 저장 완료!

# for row in tree:
#     print(row)
# 트리를 순회해 봅시다!!!
# T: 현재 노드 번호
def preorder(T): #자식들보다 부모노드에서 먼저 일처리
    if T == 0:
        return

    print(T, end =' ')  # 일처리 완료
    # 왼쪽 자식
    preorder(tree[0][T])
    # 오른쪽 자식
    preorder(tree[1][T])


def inorder(T): # 왼쪽 자식 처리하고 부모노드에서 일처리, 오른쪽 자식 처리
    if T == 0:
        return

    # 왼쪽 자식
    inorder(tree[0][T])

    print(T, end =' ')  # 일처리 완료
    # 오른쪽 자식
    inorder(tree[1][T])

def postorder(T): # 왼쪽 오른쪽 처리 후 부모 노드 처리
    if T == 0:
        return

    # 왼쪽 자식
    postorder(tree[0][T])

    # 오른쪽 자식
    postorder(tree[1][T])

    print(T, end =' ')  # 일처리 완료

preorder(1)
print()
inorder(1)
print()
postorder(1)