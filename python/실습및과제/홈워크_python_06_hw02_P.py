# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

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
print(list(sorted_words_dic.values()))
