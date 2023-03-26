import sys
sys.stdin = open('파이썬 sw문제해결 기본-string 5차시 3일차-글자수.txt', 'r')

# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
# 예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
# 파이썬의 경우 딕셔너리를 이용할 수 있다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# [문제풀이]
# 0. str1에 들어있는 글자들이 str2에 몇개 들어있는지 확인해는 것
# 0-1. 그리고 그 들어있는 숫자들 중 가장 많은 횟수를 출력
# 1. str1에서 겹치는 문자를 굳이 또 한 번 더 확인할 필요는 없으니까 set으로 중복제거 해주고
# 2. 반복문을 돌면서 str1의 인덱스 하나당 str2에 몇번 들어가는지 확인을 해보자.
# 3. 그리고 딕셔너리에 키밸류로 문자아 횟수를 입력받는 것이 가장 효율적인 것으로 보이니
# 3-1. 모든 반복이 끝난 후 키밸류값이 가장 큰 밸류를 출력하는 것으로 진행하자.

T= int(input())
for testcase in range(1,T+1):           # 테스트케이스 만큼 반복 실행
    string1 = input()                   # string2에 string1의 문자가 몇번 들어있는지 확인하기 위한 string1
    string2 = input()                   # string1의 문자가 string2에 몇번 들어있는지 확인하기 위한 string2

    string1_dp = set(string1)           # string1에 중복되어 있는 문자는 불필요하므로 중복제거
    string1_dp = list(string1_dp)       # 기존 string1을 중복제거하고 리스트화한 string1
    M = len(string2)                    # string2의 길이를 M으로 할당
    char_count = {}                     # string1의 문자가 string2에 들어있는 횟수를 세아리는 딕셔너리 생성

    # 각 문자당 string2에 들어있는 횟수 파악하기
    for string_1_v in string1_dp:       # 중복제거 string1의 문자마다 확인하기 위함
        for i in range(M):              # string2의 문자 하나하나를 확인하기 위함
            if string_1_v == string2[i]:# string1의 문자가 string2[]의 문자와 같다면
                try:                                # 우선 시도
                    char_count[string_1_v] += 1     # char_count 딕셔너리에 해당 값 +1
                except:                             # try 값이 안되면? 즉, 딕셔너리에 키가 없으면
                    char_count[string_1_v] = 1      # 생성해서 카운트 1로 만들어주기
    
    # 제일 많이 포함되어있는 횟수 찾기
    max_value = 0                                   # max_value 생성
    for string_1_v in string1_dp:                   # string1의 문자를 키 반복하면서 확인
        if char_count[string_1_v] > max_value:      # cahr_count[문자] 값이 max_value보다 크면
            max_value = char_count[string_1_v]      # max_value 변경
    print(f'#{testcase} {max_value}')