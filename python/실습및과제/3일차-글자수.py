# [문제]
# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
# 예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
# 파이썬의 경우 딕셔너리를 이용할 수 있다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# [문제풀이]
# 0. 길이가 N인 문자열 str1과 길이가 M인 str2가 주어지므로 각기 다른 길이의 문자열 2개가 주어진다.
# 0-1. str1에 포함된 글자한개 한개가 str2에 가장 많이 들어있는 것의 갯수를 출력하는 문제이다.
# 1. 파이썬의 경우 딕셔너리를 이용할 수 있다 하므로, 키로 str1의 문자들을 넣고, value로 str2에 몇 번 들어있는지를 확인하면 될듯하다.
# 2. 예로 주어진 str1 = “ABCA”, str2 = “ABABCA”의 경우 str1에서 중복되는 문자가 있기 때문에 굳이 중복해서 검사할 필요는 없다.
# 2-1. 따라서 set으로 중복 제거 후 재리스트화 하여 str2에서 검사하는 방법을 이용해보려 한다.

T = int(input())
for testcase in range(1, T+1):
    str1 = list(map(str, input()))                  # str1 입력 받음
    str2 = list(map(str, input()))                  # str2 입력 받음
    str1 = list(set(str1))                          # str1에 있는 문자가 str2에 얼마나 있는지 확인함에 있어 중복값은 필요없으므로 set으로 중복 제거후 list화
    alpha_in_str2_times_dic = {}
    for alphabet in str1:                           # str1에 있는 alphabet 인자를 이용하자
        for search_alpha in str2:                   # str2에 있는 인자가 alphabet과 동일한지 확인하려는 것임
            if alphabet == search_alpha:                                # 만약 str2의 문자와 str1의 문자가 일치하면
                try : alpha_in_str2_times_dic[alphabet] += 1            # alpha_in_str2_times 딕셔너리에 있는 alphabet 키의 값에 +1 하기
                except: alpha_in_str2_times_dic[alphabet] = 1           # alpha_in_str2_times 딕셔너리에 alphabet 키가 없으면 생성해서 값에 +1 하기
    alpha_in_str2_times_value = alpha_in_str2_times_dic.values()        # alpha_in_str2_times에 들어있는 값만을 골라내어주기.
    max_times = 0                                   # 최댓값을 구해야하지만 max()는 압수여서 쓰는 방법을 위한 변수
    for num in alpha_in_str2_times_value:           # alpha_in_str2_times의 키값들 중에서
        if max_times < num:                         # 현재 지정한 최댓값보다 더 크면
            max_times = num                         # 그 녀석이 최댓값의 자리에 오른다.
    print(f'#{testcase} {max_times}')               # 출력