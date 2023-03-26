# 목표
# 패턴매칭, 조건표현식을 통해 변수 매칭 과정에 대해 이해한다.리스트/딕셔너리 순회에 대해 이해한다.예외 처리 (try...except)에 대해 이해한다.
# 문제
# 끝말잇기 단어의 리스트가 주어졌을 때, 몇 번째 사람이 탈락하는지 확인하는 코드를 작성하시오.
# 	조건
# 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우, 지게 됩니다.
# done을 입력할 때까지 끝말잇기를 시행합니다.

# 요구사항
# words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

# [문제풀이]
# 리스트 형식으로 주어진 문제이다. 문자를 계속 입력해주면서 사용하기에 input()을 사용해야하고, 마지막으로 Done을 입력하면 종료한다.
# 리스트 내에서 다시 인덱스를 이용해 마지막 글자를 words[][-1]로 뽑아낸다.
# 조건1. 다음 단어의 첫 글자가 위 글자와 일치하는지 여부 확인
# 맞으면 pass 틀리면 해당 인덱스값을 출력
# 조건2. 이전에 등장한 단어인지 여부 확인도 위 시행과 같이 실행. 이 때는 중복값이 있는지를 확인하여 위 처럼 실행

words_game=[]   #처음은 없는 리스트
word = input()  # input()을 반복문 이전에 시작할 첫 단어를 만들어줌
words_game.append(word)
while words_game:               # 끝말잇기 시작
    word_plus = input()         # 다시 input()을 이 input의 단어 조건이 끝말잇기의 조건을 만들기
    words_game.append(word_plus)
    if word_plus == 'Done':     # 끝말잇기 종료
        print('끝말잇기가 종료됩니다.')
        break    
    elif words_game[-1] in words_game[:-1]:       #조건2 일치여부
        print(len(words_game), '번째 사람이 탈락했습니다.')
        break
    elif words_game[-2][-1] == words_game[-1][0]:       #조건1 일치여부
        pass
    else:   # 조건 외 상황 발생 시
        print(len(words_game), '번째 사람이 탈락했습니다.')
        break