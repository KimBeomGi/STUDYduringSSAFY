# 문제
# 1.하나의 문장을 입력받아, 그 문장에 끝말잇기 규칙을 적용시켜보려한다.
# 2. 세 단어가 입력으로 주어졌을 때 그 끝말잇기가 옳으면 Pass, 옳지 않으면 Fail을 출력하시오.
# 3. 예를 들어 saFe eMotion Nail 인 경우, pass를 출력한다.


# [문제풀이]
#1. 띄어쓰기로 세 단어를 주어지므로 .split()을 이용해본다.
#2. 대문자와 소문자로 헷갈릴 수 있으므로 모두 대문자로 또는 소문자로 만들어본다.
#3. 즉, map(~, ~.split())을 리스트화 한후 리스트 각 인덱스의 인덱스를 이용한다.

str_lst = input('문자열을 입력하세요. : ')
lower_str_lst = str_lst.lower()
lineword_list = list(map(str, lower_str_lst.split()))  #받은 문자열을 리스트화

for word in range(len(lineword_list)):
    if word <= (len(lineword_list)-2):
        if lineword_list[word][-1] != lineword_list[word+1][0]:
            print('Fail')
            break
    else:
        print('Pass')