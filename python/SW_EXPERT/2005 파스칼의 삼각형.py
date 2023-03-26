# [문제]
# 크기가 N인 파스칼의 삼각형을 만들어야 한다.
# 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
# 1. 첫 번째 줄은 항상 숫자 1이다.
# 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
# N이 4일 경우,
 
# N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

# [제약 사항]
# 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.

# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.
# 삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 입력
# 1
# 4

# 출력
# #1
# 1
# 1 1
# 1 2 1
# 1 3 3 1

# [문제풀이]
# 1. 첫 [1]은 할당
# 2. for n in range(N):  반복문을 돌려서 n+1이 len(리스트)라면 새로 하나 생성
# 3. [1, 1]이 2번째부터 생길 것이므로 리스트[0]은 그대로 두고, 리스트[1]이 list[1].replace(list[0]+[list[1])이 되도록 하자
# 3. list[1] 이상이면 list[n].replace(list[n]+list[n-1])

T = int(input())

for t in range(1,T+1):                                  # testcase t를 인자로 1~T만큼 반복문 실행
    print(f'#{t}')                                      # 첫 번째에는 testcase가 #t의 형식으로 출력되야하므로 여기에서 출력
    N = int(input())
    pascal_list = [1]                                   # 첫 파스칼은 1 하나가 존재하므로 그 리스트를 할당
    # print(pascal_list)
    for n in range(N):                                  # N을 입력한 횟수만큼 반복문을 돌아야하므로 for문 이용
        if (n+1) == len(pascal_list):                   # n+1이 pascal_list의 길이와 같다면, 즉. 마지막 인덱스라면
            pascal_list.append(1)                       # 1을 추가해라
            print(pascal_list)                          # 마지막 리스트를 확인했으므로 pascal_list를 출력
            continue
        elif n == 0:
            pass
        elif n >= 1:                                     # 아니라면
            pascal_list[n].replace(pascal_list[n]+pascal_list[n-1])
            pascal_list[n]