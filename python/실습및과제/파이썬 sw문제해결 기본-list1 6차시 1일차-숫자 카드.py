# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

import sys
sys.stdin = open('파이썬 sw문제해결 기본-list1 6차시 1일차-숫자 카드.txt', 'r')

# 가장 많은 카드의 숫자와 장수를 차례로 출력해야하므로 
# 카운팅 정렬을 이용해본다.

# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())            # 카드 장수 N
#     my_card = list(map(int, input()))       # 참고로 카드는 0~9까지의 숫자만을 포함한다.
#     count_list = [0]*(10)                  # 잠시 sorted를 담아놓을 그릇
#     sorted_my_card = [0]*10                  # 정렬된 카드를 담을 그릇

#     for i in range(10):                      # N만큼 반복하기
#         count_list[my_card[i]] += 1         # 각 숫자에 해당하는 인덱스에다 카운팅 하는중

#     # 구간합 구하기
#     for j in range(1, len(count_list)):    
#         count_list[i] += count_list[i-1]
        
#     for k in range(10):
#         count_list[my_card[i]] -= 1
#         sorted_my_card[count_list[my_card[i]]] = my_card[k]
    
#     # 0~9까지 정렬은 완료했으니,
#     count = [0]*10
#     for i in range(10):
#         count[sorted_my_card[i]] +=1
    

# 카운팅정렬과 유사하게 가는 식으로 진행하면 되겠다.

T = int(input())
for testcase in range(1, T+1):
    N = int(input())            # 카드 장수 N
    my_card = list(map(int, input()))       # 참고로 카드는 0~9까지의 숫자만을 포함한다.
    count_list = [0]*(10)                  # 각 [0]~[9]의 카드 장수를 담아놓을 그릇

    # 카드 장수 확인하기
    for i in range(N):                      # N만큼 반복하기
        count_list[my_card[i]] += 1         # 각 숫자에 해당하는 인덱스에다 카운팅 하는중
    # 제일 많은 카드 장수와 카드 번호 확인
    max_index = 0
    max_value = 0
    for i in range(10):
        if count_list[max_index] <= count_list[i]:
            max_index = i
            max_value = count_list[max_index]
    print(f'#{testcase} {max_index} {max_value}')