T = int(input())    # 테스트 케이스
for testcase in range(T):
    scores = list(map(int, input().split()))    # 학생들 점수를 입력받음
    N = scores.pop(0)                           # 학생명수를 빼내서 N에 기입
    average = sum(scores)/N                     # 평균을 구하기
    count = 0                                   # count는 0
    for i in range(N):                          # 학생 점수를 확인할 것임
        if scores[i] > average:                 # 학생 점수가 평균보다 높다면
            count +=1                           # count +1
    percent = count/N*100                       # percent를 구하기

    print(f'{percent:.3f}%')                    # percent값이 소숫점 3자리가 나오게하기 위해 .3f를 작성