# 목표
# 학습주제파이썬 개발 환경에 대한 이해파이썬 예외처리 기본 방식에 대한 이해
# 학습목표모듈 동작 방식에 대해 이해한다.파이썬 자료 구조의 구조 및 동작 방식에 대해 이해한다.예외처리 방식 및 활용 방식에 대해 이해한다.
# 문제
# 1. 문자열 배열을 받아 애너그램 단위로 그룹핑하는 함수 group_anagrams을 작성하여라.

# A.    입력 예시 
# eat,tea,tan,ate,nat,bat

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ]

# [문제풀이]
#1. 입력과 동시에 리스트로서 만들어준다.
#2. 각 리스트안의 내용의 단어들을 알파벳순서로 일치시켜준다.
#3. 만들어진 알파벳이 모두 들어가 있는 요소와 모두 일치한다면 

words = list(input().split(','))    # eat,tea,tan,ate,nat,bat 넣으면
print(words)        #['eat', 'tea', 'tan', 'ate', 'nat', 'bat']이 출력됨
# sorted_words = []
sorted_words_dic = {}
for word in words: 
    key = ''.join(sorted(word))             #''.join(리스트)를 이용해 리스트를 문자열로 바꿔준다.
    # print(key)                            # key가 제대로 작동하는지 확인하기 위함
    sorted_words_dic.setdefault(key,[])     #sorted_words_dic에 setdefault() 함수를 이용해서 '키' : '빈 값'을 넣어준다.
    sorted_words_dic[key].append(word)      # 키에 words리스트의 word에 해당하는 값을 넣어준다.
    print(sorted_words_dic)
print(list(sorted_words_dic.values()))      # sorted_words_dic 딕셔너리에서 value만 추출해서 그것을 리스트로 만들었음.



# words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# words_dict = {}
# for word in words:
#     key = ''.join(sorted(word)) # 키값 만들고. # join함수???    
#     words_dict.setdefault(key,[])      # 없으면 비어있는 것 하나 만들고 어펜드
#     words_dict[key].append(word)    #있으면 어펜드
# print(words_dict.values())




# arr1 = [5, 2, 8]
# arr2 = sorted(arr1)	# 원본은 유지하고 정렬한 새 리스트를 만듦.
 
# print('arr1: ', arr1)
# print('-----정렬 후-----')
# print('arr1: ', arr1)
# print('arr2: ', arr2)
 
# >>> arr1: [5, 2, 8]
# >>> arr1: [5, 2, 8]
# >>> arr2: [2, 5, 8]
