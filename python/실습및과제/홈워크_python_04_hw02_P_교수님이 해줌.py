words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# 주어진 리스트에서 각 요소들을 sorted 해서 같은 애들끼리 모으면 됨
    # (eat, tea, ate), (tan, nat), (bat)으로 묶으려고한다.
    # 각 덩어리 데이터로 처리를 해야한다.
    # aet: (eat, tea, at), ant: (nat, tan), abt:(bat) 이런식
    # key값은 각 word들의 정렬된 형태
    # value key가 같은 애들이 모인 리스트
    # 키밸류 형태의 딕셔너리로 만들어도 된다.
# 1. words의 각 요소를 정렬
    # print(list(map(sorted,words)))# 덩어리 하나하나에 똑같은 함수를 적용시킬때는 map()이용
'''
sorted_words = map(sorted, words)
# 2. 정렬된 형태에서 중복을 제거(리스트는 set의 형태를 이용한 중복 제거X)
    # 중복제거를 위해서 set에 넣고 싶은데... 리스트는 set에 안들어감
    # 리스트를 튜플로 만들 것임.
    # print(set(map(tuple,sorted_words))) #각각의 sorted_words에 tuple을 먹일 것임
# 3. 중복이 제거된 값을 key로 하는 dictionary만들기, value는 비어있는 리스트
words_dict = {key: [] for key in set(map(tuple,sorted_words))}  # 우리가 생성한 튜플을 키로하는 딕셔너리를 생성
print(words_dict)
for word in words:  #words에서 word를 꺼낸다고 생각
    sorted_word = tuple(sorted(word))   #sorted(word)로 생성된 리스트를 tuple로 바궈줌
    # sorted_word 가 똑같은 애들 끼리 모아야한다.
    words_dict[sorted_word].append(word)

print(words_dict)
'''
# ================================

words_dict = {}
for word in words:
    key = ''.join(sorted(word))        # 키값 만들고.   # join함수???    
    words_dict.setdefault(key,[])      # 없으면 비어있는 것 하나 만들고 어펜드
    words_dict[key].append(word)       #있으면 어펜드
print(words_dict.values())