# 문제
# 김해피의 성적은 아래와 같다.

# [첨부파일 참조]
# 1. 신규 과목인 'algorithm'을 시험 보았더니 90점을 받았다. 성적 딕셔너리에 이를 추가하여라.
# 2. python 과목의 점수가 80점이 아닌 85점으로 정정되었다. 주어진 성적 딕셔너니를 수정하여라.
# 3. 김해피의 전체 과목 평균 점수를 출력하라.

score = {
    'python': 80,
    'django': 89,
    'web': 83
}
score.get('algorithm')
score['algorithm']=90
# print(score['algorithm']) # 'algorithm' 추가 여부 확인
score['python'] = 85    # python 80점에서 85점으로 정정

score_value = 0         # 점수 합을 위해 이용
for i in score:
    score_value = score_value + score[i]    #인덱스를 이용해 출력되는 각 밸류를 이용

sum = score_value/len(score)    # 평균은 총합/총개수 이므로.
print(sum)