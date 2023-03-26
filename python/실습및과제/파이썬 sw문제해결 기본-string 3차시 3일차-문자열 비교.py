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
# import sys
# sys.stdin = open('파이썬 sw문제해결 기본-string 3차시 3일차-문자열 비교.txt', 'r')
# [문제풀이]

def search_in(string1, string2):
    N = len(string1)                    # 문자열1의 길이
    M = len(string2)                    # 문자열2의 길이
    for _ in range(M-N+1):              # 확인해야할 길이만 보면 M-N+1이지만 인덱스값이므로 M-N까지 확인하면되니까
        if string1 in string2:
            return f'#{testcase} 1'
    
    return f'#{testcase} 0'

T= int(input())
for testcase in range(1,T+1):
    string1 = input()                   # 문자열2에 들어있는지 확인할 짧은 문자열1
    string2 = input()                   # 문자열1이 들어있는지를 확인할 긴 문자열2

    print(search_in(string1, string2))
