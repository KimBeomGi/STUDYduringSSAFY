# 9
# 1 A 2 B 3 C 4 D 5 E 6 F 7 G 10 H 14 I

tree = ['']*2**4
N = int(input())
data = input().split()
for i in range(0, N*2, 2):
    tree[int(data[i])] = data[i+1]      # 노드 번호 입력받는 곳
print(tree)

def preorder(T):
    if T >= 2**4 or tree[T] == '':
        return
    
    print(tree[T], end= ' ')
    # 왼쪽자식
    preorder(T*2)
    # 오른쪽 자식
    preorder(T*2+1)

preorder(1)