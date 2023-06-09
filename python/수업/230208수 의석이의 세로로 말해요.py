# [문제]
# 아직 글을 모르는 의석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다.
# 이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 의석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.
# 다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 이런 식으로 다섯 개의 단어를 만든다. 아래에 의석이가 칠판에 붙여 만든 단어들의 예가 있다.
 
# A A B C D D
# a f z z
# 0 9 1 2 1
# a 8 E W g 6
# P 5 h 3 k x
 
# 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다.
# 심심해진 의석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.
# 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다.
# 이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다.
# 위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.
# 그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다.
# 위에서 의석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:

# Aa0aPAf985Bz1EhCz2W3D1gkD6x

# 칠판에 붙여진 단어들이 주어질 때, 의석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 총 다섯 줄로 이루어져 있다.
# 각 줄에는 길이가 1이상 15이하인 문자열이 주어진다. 각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’만으로 이루어져 있다.
 
# [출력]
# 각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 의석이가 세로로 읽은 순서대로 글자들을 출력한다.
'''
#[문제풀이]
#1. 'A~Z''a~z''0~9'가 나오며, 각기 다른 길이의 단어들이 배열되어있는 것을 각 자리수를 이어서 읽어내면된다.
#1-1. 행렬문제와 같다고 보면된다. 단 빈자리의 부분은 리스트로 할 시 out of range가 될 수 있으니 그 부분에 유의한다.
#2. 5개의 행으로주어지는 입력값을 리스트의 한 곳에 몰아 받고 이를 이용하자.
#2-1. 숫자도 있지만 문자와 섞여있으므로 문자로서 받도록 하자.

T= int(input())
for testcase in range(1, T+1):
    all_words = [list(map(str, input())) for _ in range(5)]             # 5개의 행으로 이루어지는 것을 한 리스트에 받아 행렬로 이용할 것임
    max_length = 0                                                      # 행에서 가장 긴 값을 구하기 위한 변수
    for words in all_words:                                             # 행에서 가장 긴 값을 구하기 위함
        if max_length < len(words):
            max_length = len(words)
    
    # 행은 5, 열은 max_length만큼 있다.
    print(f'#{testcase}', end=' ')
    for column in range(max_length):                                    # 최대 문자열의 길이 만큼 반복
        for row in range(5):                                            # 행은 5개이므로 5번 반복
            try:                                                        # 일단 진행해라
                print(f'{all_words[row][column]}', end='')              # 왼쪽부터 세로로 출력
            except IndexError:                                          # 근데 IndexError가 발생하면,(발생할 수 밖에 없는게 행마다 길이 값이 다름)
                continue                                                # 이번 턴은 넘어가라.
    print()
'''
#윤지씨 답
T = int(input())                        # 테스트케이스 입력받음
for testcase in range(1,T+1):           # 테스트케이스 반복
    words = []                          # 입력받을 리스트 그릇
    for _ in range(5):                  # 5번 반복하면서 입력받을 것임
        words.append(input())           # words리스트에 입력값 입력

    answer = ''                         # 출력할 답을 우선 초기화
    for i in range(15):                 # 각 줄에는 15가 최대의 길이이므로 그 횟수만큼 반복
        for word in words:              # words리스트 내의 각 문자열을 인자로하는 반복문
            if len(word) > i :          # 각 문자열의 길이가 i 보다 크다면
                answer += word[i]       # answer에 word[i]값을 추가해라.
 
    print(f'#{testcase} {answer}')


# [문제풀이]
#1. 한 행마다 최대 15개의 길이인 문자열이 주어지고 총 5개의 행이 주어진다.
#2. 이 각 행의 a[i], b[i], c[i], d[i], e[i], a[i+1] ---의 식으로 출력하게 하면된다.
T= int(input())
for testcase in range(1,T+1):
    words = [input() for _ in range(5)]     # 5개의 행이라 5번 입력받기 때문
    answer = ''                             # 답을 입력받을 answer변수
    
    # 각 문자열의 인덱스순으로 돌면서, 그 안에서 행별 해당하는 인덱스의 값을 answer에 입력할 것임
    for index_num in range(15):             # 최대 문자열의 길이가 15이므로
        for word in words:                  # words리스트 안의 각 단어 행을 반복
            if len(word) > index_num:       # 각 단어 행의 길이가 인덱스 숫자보다 크다면(길이가 7이면 a[6]이 마지막이기 때문)
                answer += word[index_num]   # 출력할 값인 answer에 word[index_num]즉 단어행의 index_num에 해당하는 문자를 입력
    
    print(f'#{testcase} {answer}')