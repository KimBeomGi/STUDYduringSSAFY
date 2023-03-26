import sys
sys.stdin = open('230213 파스칼의 삼각형.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    for i in range(1, N):   # 0행은 뭐 나 하나만 있으니까
        for j in range(N):
            if j == 0:      # 0열은 모두 1
                arr[i][j] = 1
            else:           # 윗 행의 j열과 j-1열을 더한 값이 현재 행의 j열 값.
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end =' ')
        print()