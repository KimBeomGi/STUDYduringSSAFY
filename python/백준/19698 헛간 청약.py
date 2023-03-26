# 소들의 수 
# $N$, 헛간의 크기 
# $W * H$를 나타내는 두 정수 
# $W$와 
# $H$, 그리고 소들에게 배정되는 공간의 크기 
# $L$이 
N, W, H, L = map(int, input().split())

if W >= L and H >= L:
    answer =  (W//L) * (H//L)
    if answer > N:
        print(N)
    else: print(answer)
else:
    print(0)