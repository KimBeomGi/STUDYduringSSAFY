# [문제]
# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
# 예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
# ABC
# ZZZZZABCZZZZZ
# 두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
# ABC
# ZZZZAZBCZZZZZ
# 문자열이 일치하지 않으므로 0을 출력.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
# 다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# [문제풀이]
# 0. 길이와 내용이 각기 다른 2개의 문자열이 주어진다. 첫 문자열이 2번째 문자열에 존재하면 1, 존재하지 않으면 0을 출력하면된다.
# 1. 반복문을 이용한 비교를 진행하면 될 듯하다.
# 1-1. 근데 [ : ] 슬라이싱 압수당해서 다른방법으로 접근해야할 듯한데 반복문으로 접근해봐야겠다.
# 2. 현재 생각 둘다 리스트로 받아 놓고 for i in range(M-N+1)하고, 그안에서 첫 문자가 일치하면 다음 문자들도 비교하도록 하는 반복문 생성하기
# 3. 일치하는지 확인할 필요가 있으므로확인할수 있게 해주는 하나의 변수 생성하기 [0]*(M-N+1)을 생성해서 각 i별로 일치하면 0을 기입할 것임

T = int(input())
for testcase in range(1, T+1):                          # 테스트케이스만큼 반복
    str1 = list(map(str, input()))                      # str1 입력 받음
    str2 = list(map(str, input()))                      # str2 입력 받음

    N = len(str1)                                       # str1 리스트의 길이
    M = len(str2)                                       # str2 리스트의 길이
    
    # str1의 문자가 str2의 문자와 연이어 같은지 확인할 예정임
    is_in = [0]*(M-N+1)                                 # str1이 str2와 일치하는지 확인하기 위한 리스트
    for i in range(M-N+1):                              # 먼저 str2의 i번째 인덱스부터 비교 시작
        if str1[0] == str2[i] and len(str1) > 1:        # str1의 길이가 1보다 크고, str1의 첫 문자가 str2의 i번째 인덱스와 같다면
            for a in range(1, len(str1)):               # str1의 첫번째 문자이후도 str2의 i번째 이후와 같은지 확인
                if str1[0+a] == str2[i+a]:              # 만약 str1의 첫번재 문자 이후도 str2의 i번재 이후 문자와 같다면
                    is_in[i] += 1                       # is_in 리스트의 i번째 인덱스에 +1
                else:                                   # 불일치면?
                    is_in[i] = 0                        # is_in 리스트의 i번째 인덱스는 다시 0
                    break                               # 다르니까 해당 for문은 더 검사할 필요 없음.
        elif str1[0] == str2[i] and len(str1) == 1:     # str1의 길이가 1이고, str1의 첫 문자가 str2의 i번째 인덱스와 같다면
            is_in[i] += 1
            
    
    # 출력하는데 문제가 있어서 return 이용하려 함수화
    def is_in_def(is_in):                               # str1이 str2에 들어있는지 확인하는 함수
        for is_true in is_in:                           # is_in 리스트를 확인하면서
            if is_true > 0:                             # str1이 str2에 들어있음이 확인된다면
                return(f'#{testcase} {1}')              # 1의 출력값을 반환
        return(f'#{testcase} {0}')                      # str1이 str2에 들어있지가 않았다면 0의 출력값을 반환
    print(is_in_def(is_in))                             # 출력!



# 고지식한 패턴
'''
T = int(input())
for testcase in range(1, T+1):                          # 테스트케이스만큼 반복
    str1 = list(map(str, input()))                      # str1 입력 받음
    str2 = list(map(str, input()))                      # str2 입력 받음

    N = len(str1)                                       # str1 리스트의 길이
    M = len(str2)                                       # str2 리스트의 길이
    
    def BruteForce(str1, str2):                               # 고지식한 알고리즘 찾기이용
        j = 0                                           # str1 의 인덱스
        i = 0                                           # str2 의 인덱스
        while j < N and i < M:
            if str2[i] != str1[j]:
                i = i - j
                j = -1
            i = i+1
            j = j+1
        if j == N: 
            return '1'      # 검색 성공
        else: 
            return '0'      # 검색 실패
    print(f'#{testcase} {BruteForce(str1, str2)}')
'''