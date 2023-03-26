arr = [1,2,3,4,5]
N = len(arr)
selected = [0]*N

# idx에 해당하는 요소가 부분집합에 포함되는지 아닌지 결정
# 결정하고나서 다음 요소 포함여부 결정하러 ㄱㄱ
def subset(idx):
    if idx == N:
        # N-1번 요소까지 결정이 끝난 상황
        print(selected)     # 2^5개 만큼 출력 될 것임
        return
    # 완전탐색: 내가 할 수 있는거 다 해보면 됨ㅇㅇ
    selected[idx] = 1
    subset(idx+1)       # 재귀호출
    selected[idx] = 0
    subset(idx+1)       # 재귀호출

subset(0)