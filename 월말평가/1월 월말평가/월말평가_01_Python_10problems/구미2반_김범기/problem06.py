# [문제]
# 해피기업은최근개발한자사제품에대한서포터를뽑기위해지원공고를게시했다. 
# 업계최고인해피기업의제품을체험하기위해많은사람들이제품서포터에지원하였다. 
# 지원자정보는아래표와같은dictionary 형태로list내부에저장되어있다.
# 그런데 담당자의실수로 서포터공고에서 나이제한에 대한 내용이 빠져있어 
# 현재지원자의분류가시급한상황이다.

# 지원자중24세를초과하는지원자의수를반환하는함수over_24를완성하시오.


# [문제풀이]
# 1. 리스트 안의 딕셔너리로 리스트[0:] 돌리면서
# 딕셔너리의 'age'의 값이 24 초과이면 숫자가 1씩 증가하는 반복문 생성

# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def over_24(people):
    i = 0
    for person in people:           # 24세 초과인 사람일 때마다 i에 +1진행 후 i출력
        if person['age'] > 24:
            i += 1
    return i

    


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    people = [
        {'name': '김싸피', 'age': 25},
        {'name': '이싸피', 'age': 28},
        {'name': '조싸피', 'age': 29},
        {'name': '아싸피', 'age': 23},
        {'name': '최싸피', 'age': 22},
        {'name': '고싸피', 'age': 21},
        {'name': '유싸피', 'age': 26},
        {'name': '후싸피', 'age': 20},
    ]

    print(over_24(people))  # 4