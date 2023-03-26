# 이건 powerset
# # 순열 중 K개인 경우만 구하면 걔가 조합

# arr = [1,2,3,4,5]

# N = len(arr)
# # idx번째 요소를 조합에 포함할지 안할지 결정
# selected = [0]*N

# def comb(idx):
#     if idx == N:                # 마지막 인덱스까지 모두 결정했으니
#         # 결과보기
#         print(selected)
#         for i in range(N):
#             if selected[i]:
#                 print(arr[i], end = '')
#         print()
#         return
#     #내가 할 수 있는 것 다 해보기
#     for i in range(2):
#         selected[idx] = i
#         comb(idx +1)

# comb(0)




# 순열 중 K개인 경우만 구하면 걔가 조합
arr = [1,2,3,4,5]

N = len(arr)
# idx번째 요소를 조합에 포함할지 안할지 결정
selected = [0]*N
# cnt = 여태까지 선택한 요소의 개수
def comb(idx, cnt):
    if cnt == K:        # K가 선택되었다면 끝, 마지막까지 갔는데 k개가 아니면 우리가 찾는게 아님
        print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i], end = ' ')
        print()
        return

    if idx == N:                # 마지막 인덱스까지 모두 결정했으나 K개를 선택하지 못함
        # 결과보기
        return
    #내가 할 수 있는 것 다 해보기
    for i in range(2):              # i가 0이면 해당 요소를 선택안한것, 1이면 선택한 요소니까
        selected[idx] = i
        # 요소를 선택하면 +1
        comb(idx +1, cnt +1*i)
        selected[idx] = 0

    # for i in range(1, -1, -1):              # i가 0이면 해당 요소를 선택안한것, 1이면 선택한 요소니까
    #     selected[idx] = i
    #     # 요소를 선택하면 +1
    #     comb(idx +1, cnt +1*i)
    #     # selected[idx] = 0

    
    # # 이것도 가능
    # selected[idx] = 1
    # # 요소를 선택하면 +1
    # comb(idx +1, cnt =+ 0)       
    # selected[idx] = 0
    # # 요소를 선택하면 +1
    # comb(idx +1, cnt)  

K = 3   # N개 중 K개를 선택
comb(0,0)