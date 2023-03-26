import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T= int(input())
for _ in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    nums = input().split()
    # 문자열 SVN, FOR 등등 크기 비교가 안되니
    # dictionary 이용해서 크기 비교하기
    num_dic = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    # 정렬하기(버블, 선택정렬)
    # 이번에는 선택정렬
    for i in range(N-1):
        # i q번째 들어갈 요소 찾아주기
        # : i번부터 맨뒷 요소중 제일 작은애
        min_idx = i
        for j in range(i+1, N):
            # 그냥 비교가 안되니까.. dictionary value로 비교하자.
            if num_dic[nums[min_idx]] > num_dic[nums[j]]:
                min_idx = j
        # 원래 리스트를 정렬한다.
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    print(f'{tc}', *nums)