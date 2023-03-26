# [문제]
# 한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.
# 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.
# 평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
# 평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 
# 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.

# 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의한다.
# 위의 예시에서 제1회 덤프를 수행한 이후 화면은 다음과 같다.
 
# A부분의 상자를 가장 낮은 B부분에 덤프하였으며, A대신 A’부분의 상자를 사용해도 무방하다.
# 다음은 제2회 덤프를 수행한 이후의 화면이다.
 
# A’부분의 상자를 옮겨서, C부분에 덤프하였다. 이때 C 대신 C’부분에 덤프해도 무방하다.
# 2회의 덤프 후, 최고점과 최저점의 차이는 8 – 2 = 6 이 되었다 (최초덤프 이전에는 9 – 1 = 8 이었다).
# 덤프 횟수가 2회로 제한된다면, 이 예시 문제의 정답은 6이 된다.

# [제약 사항]
# 가로 길이는 항상 100으로 주어진다.
# 모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.
# 덤프 횟수는 1이상 1000이하로 주어진다.
# 주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다
# (주어진 data에 따라 0 또는 1이 된다).

# [입력]
# 총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값이 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.



# [문제풀이]
# 1. 평탄화를 하는 것(가장 높은 곳에 있는 상자를 낮은 곳으로 옮기는 작업)을 덤프(dump)라고 한다.
# 1-1. 따라서 초기값은로 dump = 0의 변수가 필요하다.
# 1-2. 이때 덤프는 가장 높은 곳의 블럭은 가장 낮은 곳의 블럭으로 옮기는 것이므로
# 1-3. 리스트중 블럭의 숫자가 가장 많은 곳 중 1개를 블럭의 숫자가 가장 적은 곳에 주므로
# 1-4. 실행하면 가장 블럭의 숫자가 많은 곳 중 1곳은 -1개, 가장 적은 곳은 +1개가 된다.

# 2. 구해야하는 것은 최고점과 최저점의 차이이므로, 가장 많은 블럭의 숫자 - 가장 적은 블럭의 숫자가 되겠다.

# 3. 완벽한 평탄화는 (블럭의 갯수 / 1행의 블록 갯수)이므로 (블럭의 갯수 % 1행의 블록갯수) = 0 일때만 가능하다.
# 3-1. 고로(블럭의 갯수 % 1열의 블록갯수) != 0 이면 최고 높이와 최저 높이의 차가 -1이 되면 덤프를 멈추면 된다.

# 4. 덤프의 횟수가 처음에 주어지므로 각 덤프횟수 이내에 끝낸다면 바로 출력하도록 하고,
# 4-1. 끝내지 못한다면 주어진 덤프가 끝나는 대로 출력값을 출력한다.

# 5. 총 테스트 케이스는 10번이 주어지며, 가로 길이(1행의 블럭)는 100 고정이다.

for testcase in range(1, 11):                                                       # testcase가 10번이 주어지기때문에 1~10까지 반복
    D = int(input())                                                                # 처음 주어지는 덤프 값
    blocks_list = list(map(int, input().split()))                                   # 띄어쓰기로 숫자들이 주어지고, 리스트화해서 사용하기 위해 list(map(int, input().split())) 이용
    all_blocks_num = 0                                                              # blocks_list에 들어있는 모든 block의 갯수를 받기 위한 변수
    for column_block in blocks_list:                                                # blocks_list에 들어있는 모든 block의 갯수를 파악할 거임.
        all_blocks_num += column_block
    for dump_num in range(D):                                                       # 주어진 덤프횟수만큼 반복
        max_height = blocks_list[0]                                                 # 가장 높은 블럭의 높이
        max_column = 0                                                              # 가장 높은 블럭의 위치
        min_height = blocks_list[0]                                                 # 가장 낮은 블럭의 높이
        min_column = 0                                                              # 가장 낮은 블럭의 위치
        for blocks_num in range(len(blocks_list)):                                  # blocks_list의 각 블럭위치를 인자로 반복문 실행
            if blocks_list[blocks_num] >= max_height:                               # 가장 높은 블럭의 수와 위치를 구하기 위함
                max_height = blocks_list[blocks_num]
                max_column = blocks_num
            elif blocks_list[blocks_num] <= min_height:                             # 가장 낮은 블럭의 수와 위치를 구하기 위함
                min_height = blocks_list[blocks_num]
                min_column = blocks_num
        blocks_list[max_column] -= 1                                                # 가장 높은 열의 블럭에서 낮은 곳으로 옮기면서 1개 제거
        blocks_list[min_column] += 1                                                # 가장 낮은 열의 블럭에서 높은 곳으로 옮기면서 1개 추가
        if all_blocks_num % 100 == 0 and max_height == (all_blocks_num/100):                                                    # 주어진 덤프 전에 끝났을때(깔끔한 평탄화시)
            break
        elif all_blocks_num % 100 != 0 and max_height == ((all_blocks_num//100)+1) and min_height == (all_blocks_num//100):     # 주어진 덤프 전에 끝났을때(덜 깔끔한 평탄화시)
            break
    max_height = blocks_list[0]                         # 평탄화 후 최고 높이를 재기 위함
    min_height = blocks_list[0]                         # 평탄화 후 최저 높이를 재기 위함
    for blocks in blocks_list:                          # 평탄화 후 만들어진 블록리스트로 반복문 실행
        if blocks > max_height:                         # 평탄화 후 만들어진 블록리스트의 최고 높이 구하기
            max_height = blocks
        elif blocks < min_height:                       #평탄화 후 만들어진 블록리스트의 최저 높이 구하기
            min_height = blocks
    print(f'#{testcase} {max_height-min_height}')