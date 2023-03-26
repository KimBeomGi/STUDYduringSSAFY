# [문제]
# 아스키 코드는 미국 ANSI에서 표준화한 정보교환용 7비트 부호체계이다.
# 아스키 코드는 총 128가지의 문자를 나타낼수 있으며, 각각의 문자를 나타내는 숫자값이 존재한다.
# 다음은 아스키코드표의 일부를 나타낸 것이다.
# python에서는 built-in함수인 ord()와 chr()을 사용하여, 각각 아스키코드 인코딩에 대응되는 숫자와 문자로 변환할 수 있따.

# 문자열 2개를 전달받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 합을 가진 문자열을 반환하는 코드를 작성하시오.


#[문제풀이]
# 1. ord()함수를 이용해서 문자열의 문자를 각 아스키코드의 수로 변환
# 1-1. 문자열을 우선 하나씩 갈라넣어준다. 그리고 ord()사용이 가능하도록 리스트로 변환
# 1-2. 리스트의 숫자합을 생성
# 2. word1과 word2에 대해서 1의 내용을 각각 만들어주고 if 문으로 비교 후 각 내용에 따라 출력


word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

w_solve_list1 = list(''.join(word1))
w_solve1 = []
for word in w_solve_list1:
    w_solve1.append(ord(word))
sw_solve1 = sum(w_solve1)
# print(sw_solve1)

w_solve_list2 = list(''.join(word2))
w_solve2 = []
for word in w_solve_list2:
    w_solve2.append(ord(word))
sw_solve2 = sum(w_solve2)
# print(sw_solve2)

if sw_solve1 > sw_solve2:
    print(word1)
elif sw_solve1 < sw_solve2:
    print(word2)