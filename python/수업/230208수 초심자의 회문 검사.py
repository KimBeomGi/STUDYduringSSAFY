# [문제 이동]
# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.

# [제약 사항]
# 각 단어의 길이는 3 이상 10 이하이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


# samsung
# asmsung
# amssung

# [문제풀이]
# 1. for i in range(len(입력값))
# 1-1. 글자가 7개면 첫 글자를 끝가지 보내는데는 6번의 자리바꿈을 수행
# 1-2. 첫글자를 바꾸고 나면 5번, 그다음은 4번, 3번,2번, 1번 끝.
# 2. 버블정렬을 활용하자.
'''
T = int(input())
for testcase in range(1, T+1):                          # 테스트케이스만큼 돌리기
    word = list(map(str, input()))                      # 주어진 단어를 하나씩 따로따로 떼어내고 이용하기 위해 리스트화
    word_copy = ''.join(word)
    for change in range(len(word)-1):                   # 총 몇 번 수행해야하는지
        for word_change in range(len(word)-change-1):   # 단어 글자당 바꾸기 위해 수행해야할 횟수
            word[word_change], word[word_change+1] = word[word_change+1], word[word_change]     # 리스트[i]를 리스트[i+1]로, 리스트[i+1]를 리스트[i]로 바꿈
    
    word = ''.join(word)                                # 리스트로 받은 world를 문자열로 정리
    if word_copy == word:                               # 처음받은 word의 값과 현재 뒤집은 word의 값과 같다면
        print(f'#{testcase} {1}')                       # 1출력 
    else:                                               # 아니면
        print(f'#{testcase} {0}')                       # 0출력
'''


# [문제풀이]
# 1. 입력받은 값을 뒤집음. 그리고 그 값이 입력받은 값과 같으면 회문이니까 1 출력 아니면 0 출력
# 1-1. 여기서 뒤집는 방법으로 리스트[i], 리스트[-(i+1)] = 리스트[-(i+1)], 리스트[i]를 이용
T = int(input())
for testcase in range(1, T+1):
    word = input()                                      # 단어 입력
    word_copy = list(map(str, word))                    # 입력된 단어를 이용하기 위해 리스트화
    # 리스트[i]와 리스트[-(i+1)]을 교체
    for word_index in range(len(word_copy)//2):         # 리스트의 중간값을 기준으로 첫값과 끝값을 교체하기 위함
        word_copy[word_index], word_copy[-(word_index+1)] = word_copy[-(word_index+1)], word_copy[word_index]
        # 리스트[i]와 리스트[-(i+1)]
    
    word_copy = ''.join(word_copy)                      # 전 후를 뒤집은 word_copy리스트를 문자열화
    if word_copy == word:                               # 처음받은 word의 값과 뒤집은 word_copy값이 같다면
        print(f'#{testcase} {1}')                       # 1출력 
    else:                                               # 아니면
        print(f'#{testcase} {0}')                       # 0출력