# 학기가 끝나고, 학생들의 점수로 학점을 계산중이다.
# 학점은 상대평가로 주어지는데, 총 10개의 평점이 있다.


# 학점은 학생들이 응시한 중간/기말고사 점수 결과 및 과제 점수가 반영한다.
# 각각 아래 비율로 반영된다


# 10 개의 평점을 총점이 높은 순서대로 부여하는데,

# 각각의 평점은 같은 비율로 부여할 수 있다.

# 예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.

# 입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,
# 학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
# K 번째 학생의 학점을 출력하는 프로그램을 작성하라.


# [제약사항]
# 1. N은 항상 10의 배수이며, 10이상 100이하의 정수이다. (10 ≤ N ≤ 100)
# 2. K는 1 이상 N 이하의 정수이다. (1 ≤ K ≤ N)
# 3. K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.
# 테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys
sys.stdin = open('1983 조교의 성적 매기기.txt','r')

# [문제풀이]
# 0. A+, A0 A- ,,,, C0 C- D0 의 10개의 평점이 있따.
# 0-1. 총점 = 중간고사(35%) + 기말고사 (45%) + 과제(20%)로 총점이 높은 순서대로 10개의 평점을 부여

# 버블정렬 함수
def sort_score(students_score):
    for i in range(len(students_score)-1):
        for j in range(len(students_score)-1):
            if students_score[j][1] < students_score[j+1][1]:
                students_score[j], students_score[j+1] = students_score[j+1], students_score[j]
    return students_score

# 학생번호와 점수를 학생 번호와 A+~D0로 바꾸는 함수
def grade_score(students):
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']    # A+ ~ D0 까지 10개의 성적
    multi_num = N/10                                                        # 20이면 20/10으로 multi_nun = 2
    for i in range(len(students)):                                          # 학생 수만큼 반복
        students[i][1] = grade[(int(i/multi_num))%10]                       # 학생의 점수를 각 인덱스 위치의 학생에 해당하는 점수를 주기
    return students                                                         # students를 반환

def k_print(K, students):                                                   # A+ A0,.,, 를 출력하기 위한 함수
    for i in range(len(students)):                                          # 학생 수 만큼 돌려서
        if students[i][0] == K-1:                                           # 학생 번호를 찾으면
            return students[i][1]                                           # 해당 학생의 점수를 반환
        
T= int(input())
for testcase in range(1,T+1):
    N, K = map(int, input().split())                                        # 학생의 수 N, 학점을 알고 싶은 학생의 번호 K
    students_score =[]                                                      # 빈 students_score 할당
    for i in range(N):                                                      # 점수를 계산하고 students_score에 입력받기 위함
        score = list(map(int, input().split()))                             # 점수를 입력받음
        total_score = score[0]*35 + score[1]*45 + score[2]*20               # 모두가 100으로 안나눈다면 변별력이 생기니 100으로 안나눔
        students_score.append([i, total_score])                             # students_score에 [학생번호-1, 점수]를 입력함
    students = sort_score(students_score)                                   # 점수대로 내림차순 정렬
    students_grade = grade_score(students)                                  # 점수를 학점으로 바꿈
    
    print(f'#{testcase} {k_print(K, students_grade)}')