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
'''
T = int(input())

for t in range(T):
    N = int(input())
    print("#{}".format(t+1))
    answer = []                     # 정답을 담아야 함
    for i in range(N):
        temp = []                   # 파스칼의 한 줄
        for j in range(i+1):
            if j == 0 or j == i:    # 한 줄에서 첫번째 혹은 마지막은 무조건 1
                temp.append(1)      
            else:
                temp.append(answer[i-1][j] + answer[i-1][j-1])  # i-1, 즉 이전 줄의 두개를 합친게 이번 줄의 숫자가 됨
        answer.append(temp)
    for i in answer:
        print(*i)                   # asterisk를 사용하는 방법 중 하나로 리스트 안의 내용만 빼다 쓸 수 있다.
'''


'''
# 리스트 안에 리스트를 넣어두고 인덱스 리스트를 반복 출력 하면서 파스칼 삼각형을 만들어냄


T = int(input())

for t in range(1, T+1):                 # 1~T회 만큼 반복
    print(f'{t}')                       # 테스트케이스 작성
    N = int(input())                    # 구해야할 N에 대해 입력
    pascal_list = []                    # 구할 파스칼 삼각형의 값을 넣어둘 것.
    for law in range(N):                # 출력할 N행 만큼을 반복
        law_pascal = []                 # 파스칼 한 줄을 출력할 수 있도록 하는 것.    
                                        # 여기서부터 리스트 안에 리스트인 파스칼 행을 만들어내는 반복문
        for i in range(law+1):            # 파스칼 한 줄을 만들기 위한 반복문으로 0~(N-1)
            if i == 0 or i == law:        # 리스트[0]과 리스트[-1]에서
                law_pascal.append(1)    # 파스칼 한 줄의 리스트[0]과 리스트[-1]에는 1을 추가
                # print('ONE')
                # print(law_pascal)
                # print(pascal_list)
            else:                       # 리스트[0]과 리스트[-1]에 해당되지 않는다면                
                law_pascal.append(pascal_list[law-1][i] + pascal_list[law-1][i-1])      # law-1, 즉. 이전 행의 리스트[i]+리스트[i-1] 두개를 합친게 이번 줄의 숫자가 됨
                # print('TWO')
                # print(law_pascal)
                # print(pascal_list)
        pascal_list.append(law_pascal)  # 총 파스칼 리스트에서 파스칼 행을 넣음
        print(pascal_list)
    for pascal in pascal_list:
        # print('THREE')
        print(*pascal)                       # 파스칼 리스트에서 리스트로 들어있는 행 인덱스를 리스트를 벗겨내서 출력하도록 print(*i)를 이용했음
'''
T = int(input())

for t in range(1,T+1):      #testcase를 1~T만큼 반복
    print(f'{t}')
    N = int(input())
    pascal_list = []
    for law in range(N):
        law_pascal = []

        for i in range(law+1):          #0~N-1만큼
            if i == 0 or i == law:      # 리스트[0] 리스트[-1]이면
                law_pascal.append(1)    # 리스트[0] 리스트[-1]에 1을 추가
                print(law, i, law_pascal)
            else:
                print(law, i, law_pascal)
                law_pascal.append(pascal_list[law-1][i]+pascal_list[law-1][i-1])
                print(law, i, law_pascal)
        pascal_list.append(law_pascal)
    for pascal in pascal_list:
        print(*pascal)