# [문제]
# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.
# 예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 ‘b’, ‘d’, ‘p’, ‘q’만으로 이루어진 하나의 문자열이 주어진다. 문자열의 길이는 1이상 1000이하이다.

# [출력]
# 각 테스트 케이스마다 주어진 문자열을 거울에 비춘 문자열로 출력한다.

# [문제풀이]
# 0. 비, 디, 피, 큐 로 이루어진 문자열이다. 이를 거울에 비췄을 때 어떤 문자가 나올지 출력하면된다.
# 1. 거울에 비췄을 때, b → d, d → b, p → q, q → b가 된다. 그리고 또한 역순이 되므로 그에 대해서도 고려해줘야한다.
# 2. 현재 구상으로는 먼저 숫자를 바꿔주고, 위치를 바꾸는 것을 구상하고 실행에 옮긴다.
# 2-1. 위치를 바꿀 때 중간 지점을 기점으로 리스트[i], 리스트[-(i+1)] = 리스트[-(i+1)], 리스트[i] 으로 시도해본다.

T = int(input())
for testcase in range(1, T+1):
    origin_word = input()                                            # 값 입력받기
    origin_word_list = list(map(str, origin_word))                   # 입력받은 값 리스트화(띄어쓰기가 없는 문자)

    # 이제 거울에 반사시킴
    # 1. 각 글자 반대 방향으로 바꾸기
    for origin_word_index1 in range(len(origin_word_list)):          # origin_word_list를 인덱스값으로 받는 반복문
        if origin_word_list[origin_word_index1] == 'b':              # 'b' → 'd'로 바꿈
            origin_word_list[origin_word_index1] = 'd'
        elif origin_word_list[origin_word_index1] == 'd':            # 'd' → 'b'로 바꿈
            origin_word_list[origin_word_index1] = 'b'
        elif origin_word_list[origin_word_index1] == 'p':            # 'p' → 'q'로 바꿈
            origin_word_list[origin_word_index1] = 'q'
        elif origin_word_list[origin_word_index1] == 'q':            # 'q' → 'p'로 바꿈
            origin_word_list[origin_word_index1] = 'p'
    
    # 2. 글자는 다 바꿨으니 이제 자리 바꿈 실시
    for origin_word_index2 in range(len(origin_word_list)//2):      # 리스트[i] ↔ 리스트[-(i+1)]을 하기 위해 중간을 기준으로 교체 실시
        origin_word_list[origin_word_index2], origin_word_list[-(origin_word_index2+1)] = origin_word_list[-(origin_word_index2+1)], origin_word_list[origin_word_index2]
        # 리스트[i] ↔ 리스트[-(i+1)]
    mirror_word = ''.join(origin_word_list)                         # 거울에 비춘 입력값의 형태
    print(f'#{testcase} {mirror_word}')