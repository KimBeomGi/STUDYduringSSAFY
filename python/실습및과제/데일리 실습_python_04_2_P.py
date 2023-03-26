# [문제]
# 1. 주어진 리스트는 반장선거 투표 결과이다. 득표가 많은 순서대로 출력하시오.
# 단, 딕셔너리를 사용할 것이며, 외부 패키지는 사용하지 않든다.

# students = ['박해피', '이영희', '조민지', '조민지', 
#             '김철수', '이영희', '이영희', '김해킹',
#             '박해피', '김철수', '한케이', '강디티',
#             '조민지', '박해피', '김철수', '이영희',
#             '박해피', '김해킹', '박해피', '한케이','강디티']

#[문제풀이]
# 1. 리스트 형태이고 득표가 많은 순서대로 출력하시오. 라고 되어있다.
# 2. 우선 먼저 출력해보자

students = ['이영희', '박해피', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

who_leader_studnets ={}
for student in students:
    try: who_leader_studnets[student] += 1              # student인자가 who_leader_students 딕셔너리에 있다면 값에 +1
    except: who_leader_studnets[student] = 1            # student인자가 who_leader_students 딕셔너리에 없다면 값은 1
print(who_leader_studnets)                              # 문제에서 제시해준 대로는 이미 득표가 많은 순서대로 출력이 된다. 그러나 우린 그렇게도 되게 만들어야지.

print(dict(sorted(who_leader_studnets.items(), key=lambda item: item[1], reverse = True)))
# 키값을 이용해서 내림차순으로 출력해야 득표가 많은 순서대로 출력이 되므로 items()함수를 이용해주고
# sorted를 (a,b)형식으로 나오는 item의 값을 item[1] 즉, 키 값을 기준으로 sorted 할 것임을 선언.
# reverse = True로 내림차순으로 정렬할 것임을 선언.
# 마지막으로 dict를 사용 items()로 풀렸던 딕셔너리 who_leader_students를 다시 딕셔너리화 시킴.