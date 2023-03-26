import sys
sys.stdin = open('1208_input.txt', "r")

for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    # 1. 덤프
    # 1-1 최고 높이 위치 찾기
    # 1-2 최저 높이 위치 찾기
    for _ in range(N):
        max_idx = 0
        min_idx = 0
        for i in range(100):
            if boxes[max_idx] < boxes[i]:
                max_idx = i
            elif boxes[min_idx] > boxes[i]:
                min_idx = i
        # 1-3 최고 높이에서 -1, 최저높이에서 +1
        boxes[max_idx] -= 1
        boxes[min_idx] =+ 1
        #2. 1을 N번 반복
        #3. 결과 출력(최고높이-최저높이)
    max_idx = 0
    min_idx = 0
    for i in range(100):
        if boxes[max_idx] < boxes[i]:
            max_idx = i
        elif boxes[min_idx] > boxes[i]:
            min_idx = i

    print(f'#{tc} {boxes[max_idx]-boxes[min_idx]}')