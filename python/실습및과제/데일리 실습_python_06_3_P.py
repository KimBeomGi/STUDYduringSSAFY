# [문제]
# 1. 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를 작성하시오.

# [문제풀이]
# 1. 우선 def count_vowels()로 함수를 하나 정의해주자.
# 2. 그리고 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환할 수 있도록 for e in '문자열':과 if문을 적절히 섞어서 return 해주자.
# 3. 영어에서 모음은 a,e,o,u,i 이다. 소문자 대문자 둘다 확인 할 수 있게 하자.
# 3-1. 소문자 대문자 구분없도록 문자열을 받으면 소문자로 만들어 두고 파악하는 것도 추가적인 방법 중 하나 일 수 있겠다.

# [소문자,대문자 상태에서 모음 확인]
# def count_vowels(string):
#     stringvowel = 0
#     for char in string:
#         if char in ['a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I']:
#             stringvowel += 1
#     return print(stringvowel)

# [소문자로 변환 후 모음 확인]
def count_vowels(string):
    stringvowel = 0                                 # 모음갯수를 확인하기 위한 변수
    string = string.lower()                         # 문자열을 소문자로 변환
    for char in string:                             # 문자열을 반복하면서 각 문자를 char 인자로 받아 반복
        if char in ['a', 'e', 'o', 'u', 'i']:       # 영어에서 모음 소문자인 a,e,o,u,i 가 있으면 모음갯수 확인 변수에 +1 함
            stringvowel += 1
    return print(stringvowel)                       # 문제에 나와있던 것이 count_vowels()로 print()가 없으므로 함수에 print()도 포함시켜주고 return

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3