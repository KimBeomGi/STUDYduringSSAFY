# [문제]
# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

# 입력
# 첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N, 다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
# 1<=T<=10, 10<=N<=1000

# 출력
# #과 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

# 입력 예
# 3
# 10
# 0011001110
# 10
# 0000100001
# 10
# 0111001111

# 출력 예
# #1 3
# #2 1
# #3 4

# [문제풀이]
# 1. 주어지는 숫자가 붙어있으므로 해당 숫자를 풀어서 각 떨어지도록 한다.
# 1-1. 리스트에 넣어주자.
# 1-3. 계산된 count를 넣어줄 count_list를 하나 만들어주자.
# 2. 미리 count = 0의 변수를 생성하고
# 2-1. for문을 돌려서 1이면 count += 1

T = int(input())
for testcase in range(1,T+1):
    N = int(input())                                    # 수열의 길이
    nums = list(map(int, input()))                      # 띄어쓰기 없는 형식의 수열
    count_list = []                                     # 연속된 1의 갯수를 세는 count를 담아놓을 리스트
    count = 0
    for num in range(len(nums)):                        # nums 리스트의 길이만큼 반복
        if nums[num] == 1:                              # nums의 인자가 1이면
            count += 1                                  # count에 + 1
            count_list.append(count)                    # cont_list에 count를 추가
        elif nums[num] == 0:                            # nums의 인자가 0이면
            count = 0                                   # count는 0

    max_count = 0                                       # 최대로 연속된 1의 갯수를 구해야 함
    for count_i in count_list:                          # count_list에서 반복문 실행
        if max_count < count_i:                         # max_count를 구하기 위한 if문
            max_count = count_i
    print(f'#{testcase} {max_count}')