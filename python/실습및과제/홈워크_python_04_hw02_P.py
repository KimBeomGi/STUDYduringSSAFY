# [문제]
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# [문제풀이]
# 1. 그룹핑을 어떻게 할 것이냐가 관건
# 2. words 인덱스에 각 sorted를 적용해서 그 값이 일치한다면 확인하고 묶는 방법을 모색.
# 3. try, except 문을 활용하는 것도 하나의 방법이지 않을까?

anagram_dict = {}
for word in words:
    key = ''.join(sorted(word))         # words리스트의 인덱스 word 인자를 오름차순정렬하고 문자열로 만들고 key에 대입한다.
    anagram_dict.setdefault(key,[])     # key를 anagram_dict에 넣고 이 키가 없다면 이 키의 값으로 리스트를 만들어라.
    anagram_dict[key].append(word)      # key의 value로 word인자를 추가해라.
print(anagram_dict.values())