# [문제]
# 여러 개의 쇠막대기를 레이저로 절단하려고 한다.
# 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.
# 쇠막대기와 레이저의 배치는 다음 조건을 만족한다.

#  - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
#  - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
#  - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
#  - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

# 아래 그림은 위 조건을 만족하는 예를 보여준다.
# 수평으로 그려진 굵은 실선은 쇠막대기이고, 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향이다.

 

# 이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.
#     1. 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 “()” 으로 표현된다. 또한, 모든 “()”는 반드시 레이저를 표현한다.
#     2. 쇠막대기의 왼쪽 끝은 여는 괄호 ‘(’ 로, 오른쪽 끝은 닫힌 괄호 ‘)’ 로 표현된다.
# 위 예의 괄호 표현은 그림 위에 주어져 있다.
# 쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘려지고,
# 이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘려진다.
# 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.

# [출력]
# 각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 잘려진 조각의 총 개수를 출력한다.

# [입력]
# 2
# ()(((()())(())()))(())
# (((()(()()))(())()))(()())

'''
# [문제풀이]
# 0. 모든 입력값이 '(' 또는 ')' 인 괄호로 주어진다.
# 0-1. 여기서 (와 )는 각각 쇠막대기의 왼쪽 끝과 오른쪽 끝을 나타낸다.
# 0-2. 레이저는 ()에서 나오는데 ()사이의 공간에서 발사된다고 생각하자.
# 1. 보기편하게 '(' : 1,  ')' : 0으로 명명한다.
# 1-1. ()즉 10으로 붙어있다면 이는 레이저가 발사되는 위치임을 알 수 있게 A로 표현한다.
# 2. 가장 작은 길이의 막대기 먼저 레이저로 동강 낼 것이고, 동강낸 갯수는 막대기 안에 들어있는 레이저갯수+1개이다.
# 2-1. 참고로 모든 칸은 레이저 또는 막대의 끝과 끝으로만 이루어져있으므로 닫힌 괄호위치-열린 괄호위치를 해도 된다.

T= int(input())                                                     # 테스트케이스 입력받음
for testcase in range(1,T+1):                                       # 테스트케이스 반복실행
    ironbar_with_laser = input()                                    # 쇠막대기와 레이저 값 받음
    ironbar_with_laser_list = list(map(str,ironbar_with_laser))     # 입력값을 리스트로
    for bracket_i in range(len(ironbar_with_laser_list)):           # 괄호로 이루어진 쇠막대기 리스트에서 각 괄호를 인자로한 반복문
        if ironbar_with_laser_list[bracket_i] ==  '(':              # '('는 보기편하게 0으로 바꾸고
            ironbar_with_laser_list[bracket_i] = 0
        elif ironbar_with_laser_list[bracket_i] == ')':             # ')'는 보기편하게 1로 바꾼다.
            ironbar_with_laser_list[bracket_i] = 1
    
    #레이저와 쇠막대기 구분하기
    i = 0
    while i < len(ironbar_with_laser_list)-1:                       # 레이저를 다른 값으로 분리시키기 위한 while문
        if ironbar_with_laser_list[i] == 0 and ironbar_with_laser_list[i+1]:    # 레이저를 나타내는 ()이면
            ironbar_with_laser_list[i] = 'A'                                    # 레이저의 시작점을 A로 바꿔주고
            del ironbar_with_laser_list[i+1]                                    # 레이저의 끝은 지워서 레이저를 A로 표현
        i += 1
    
    laser_numbers = 0                                       # 레이저 A의 개수를 확인하기 위한 변수
    for is_laser in ironbar_with_laser_list:                # 레이저 A의 개수 파악
        if is_laser == 'A':                                 # 레이저가 맞다면, 즉 ()형태면
            laser_numbers += 1                              # 레이저의 갯수에 1을 더해라

    # 괄호가 닫히는 곳(1)을 만나면 가장 가까운 괄호가 열리는 곳(0)까지 돌아가서 A의 갯수를 헤아리고,
    # 세아린 A의 갯수+1개를 만들어진 쇠막대기 갯수에 추가, 그리고 해당 괄호 2개를 삭제함
    ironbar_numbers = 0                                     # 만들어진 쇠막대기 갯수
    i = 0                                                   # 쇠막대기가 만들어지는 갯수를 구하는 데 필요한 인자 i
    while laser_numbers < len(ironbar_with_laser_list):     # 레이저 갯수가 전체 리스트의 길이와 같아지면 더 실행할 필요가 없으므로, ironbar_with_laser_list의 길이가 길때만 실행
        if ironbar_with_laser_list[i] == 1:                 # 처음으로 닫힌 괄호(1)를 만나게 되면
            for j in range(i+1):                            # 0~i만큼의 j를 이용해 리스트[i-j]==0을 보게 하기 위함
                if ironbar_with_laser_list[i-j] == 0:       # 되돌아가면서 열린 괄호(0)를 만나고,
                    ironbar_numbers += j                    # 열린괄호~닫힌괄호사이에는 레이저로 채워져있으므로 j갯수만큼이 쇠막대기가 생성된다.
                                                            # 가장 작은 쇠막대기 기준임.
                    del ironbar_with_laser_list[i]          # 해당 부분은 필요없어졌으므로 제거
                    del ironbar_with_laser_list[i-j]        # 해당 부분은 필요없어졌으므로 제거
                    i = (i-j)                               # 삭제된 부분때문에 리스트가 조정되었으므로 i를 i-j의 위치로 이동 
                    break                                   # 해당 for문은 끝내고 다시 while 문으로 이동
        else:                                               # ironbar_with_laser_list[i]가 1이 아니면 1을 찾을 때까지 i를 이동
            i += 1                                          # 닫힌 괄호를 못찾았으니 다음 인덱스로 넘어가야지.
    print(f'#{testcase} {ironbar_numbers}')
'''


# [문제풀이]
# 0. 모든 입력값이 '(' 또는 ')' 인 괄호로 주어진다.
# 0-1. 여기서 (와 )는 각각 쇠막대기의 왼쪽 끝과 오른쪽 끝을 나타낸다.
# 0-2. 레이저는 ()에서 나오는데 ()사이의 공간에서 발사된다고 생각하자.
# 1. 보기편하게 '(' : 1,  ')' : 0으로 명명한다.
# 1-1. ()즉 10으로 붙어있다면 이는 레이저가 발사되는 위치임을 알 수 있게 A로 표현한다.
# 2. 가장 작은 길이의 막대기 먼저 레이저로 동강 낼 것이고, 동강낸 갯수는 막대기 안에 들어있는 레이저갯수+1개이다.
# 2-1. 참고로 모든 칸은 레이저 또는 막대의 끝과 끝으로만 이루어져있으므로 닫힌 괄호위치-열린 괄호위치를 해도 된다.
# 3. 방법 2.는 시간초과로 실패해서 2번째 방법시도중....
# 3-1. 실제로 작업대에 쇠막대기가 있고 레이저로 생각해보자.
# 3-2. 작업대에 쇠막대기를 올리는 것을 '('로 표현한다. 따라서 '('면 현재 작업중인 막대기 +1이다.(한 번에 하나씩만 올리니까)
# 3-3. 레이저로 자르는 것을 '()'로 표현된다. 작업중인 막대기는 그대로 있으나, 이전까지 작업하던 막대기가 동강나면서 그 수만큼의 막대기가 생성된다.
# 3-3-1. 따라서 '()'시에는 생성된 막대기 += 현재 작업중인 막대기이다.
# 3-4. 이제 작업대에서 막대기를 치우는 것을 ')'로 표현한다. 이때 이 막대기도 버리지 않고 생성된 막대기로 간주하므로 생성된 막대기에 치우는 수 만큼 생성한다.
# 3-4-1. 따라서 ')' 시에는 생성된 막대기 +1 과 동시에 현재 작업중인 막대기 -1을 한다.(한 번에 하나씩만 빼니까)

'''
T= int(input())                                                     # 테스트케이스 입력받음
for testcase in range(1,T+1):                                       # 테스트케이스 반복실행
    ironbar_with_laser = input()                                    # 쇠막대기와 레이저 값 받음
    ironbar_with_laser_list = list(map(str,ironbar_with_laser))     # 입력값을 리스트로
    for bracket_i in range(len(ironbar_with_laser_list)):           # 괄호로 이루어진 쇠막대기 리스트에서 각 괄호를 인자로한 반복문
        if ironbar_with_laser_list[bracket_i] ==  '(':              # '('는 보기편하게 0으로 바꾸고
            ironbar_with_laser_list[bracket_i] = 0
        elif ironbar_with_laser_list[bracket_i] == ')':             # ')'는 보기편하게 1로 바꾼다.
            ironbar_with_laser_list[bracket_i] = 1
    
    #레이저와 쇠막대기 구분하기
    i = 0
    while i < len(ironbar_with_laser_list)-1:                       # 레이저를 다른 값으로 분리시키기 위한 while문
        if ironbar_with_laser_list[i] == 0 and ironbar_with_laser_list[i+1]:    # 레이저를 나타내는 ()이면
            ironbar_with_laser_list[i] = 'A'                                    # 레이저의 시작점을 A로 바꿔주고
            del ironbar_with_laser_list[i+1]                                    # 레이저의 끝은 지워서 레이저를 A로 표현
        i += 1
    
    # 이제 레이저로 자르기 시작 작업테이블에 실제로 막대기 있다고 생각하면 아주아주 조금 편해짐
    worked_ironbar = 0                                              # 현재 판 위에 존재하는 쇠막대기
    made_ironbar = 0                                                # 레이저로 인해 갈라지며 생성된 쇠막대기
    for e in range(len(ironbar_with_laser_list)):                   # 0~ (len(ironbar_with_laser_list)-1) 만큼
        if ironbar_with_laser_list[e] == 0:                         # 열린괄호(0)를 만나게 된다면
            worked_ironbar += 1                                     # 작업중인 쇠막대기를 하나 증가시킨다.
        
        elif ironbar_with_laser_list[e] == 'A':                     # 레이저(A)를 만나게 되면 현재 작업중인 막대기 갯수는 그대로 있으므로
            made_ironbar += worked_ironbar                          # 현재까지 작업중인 막대기 갯수만큼 막대기를 생성한다.
        
        elif ironbar_with_laser_list[e] == 1:                       # 닫힌괄호(1)를 만나게 된다면
            worked_ironbar -= 1                                     # 이제 작업중인 막대기는 빼고
            made_ironbar += 1                                       # 작업중 막대기도 레이저로 생성된 막대기 중 하나가 된다.
    print(f'#{testcase} {made_ironbar}')                            # 출력값을 출력한다.
'''


# [문제풀이]
# 0. 모든 입력값이 '(' 또는 ')' 인 괄호로 주어진다.
# 0-1. 여기서 (와 )는 각각 쇠막대기의 왼쪽 끝과 오른쪽 끝을 나타낸다.
# 0-2. 레이저는 ()에서 나오는데 ()사이의 공간에서 발사된다고 생각하자.
# 1. 보기편하게 '(' : 1,  ')' : 0으로 명명한다.
# 1-1. ()즉 10으로 붙어있다면 이는 레이저가 발사되는 위치임을 알 수 있게 A로 표현한다.
# 2. 가장 작은 길이의 막대기 먼저 레이저로 동강 낼 것이고, 동강낸 갯수는 막대기 안에 들어있는 레이저갯수+1개이다.
# 2-1. 참고로 모든 칸은 레이저 또는 막대의 끝과 끝으로만 이루어져있으므로 닫힌 괄호위치-열린 괄호위치를 해도 된다.
# 3. 방법 2.는 시간초과로 실패해서 2번째 방법시도중....
# 3-1. 실제로 작업대에 쇠막대기가 있고 레이저로 생각해보자.
# 3-2. 작업대에 쇠막대기를 올리는 것을 '('로 표현한다. 따라서 '('면 현재 작업중인 막대기 +1이다.(한 번에 하나씩만 올리니까)
# 3-3. 레이저로 자르는 것을 '()'로 표현된다. 작업중인 막대기는 그대로 있으나, 이전까지 작업하던 막대기가 동강나면서 그 수만큼의 막대기가 생성된다.
# 3-3-1. 따라서 '()'시에는 생성된 막대기 += 현재 작업중인 막대기이다.
# 3-4. 이제 작업대에서 막대기를 치우는 것을 ')'로 표현한다. 이때 이 막대기도 버리지 않고 생성된 막대기로 간주하므로 생성된 막대기에 치우는 수 만큼 생성한다.
# 3-4-1. 따라서 ')' 시에는 생성된 막대기 +1 과 동시에 현재 작업중인 막대기 -1을 한다.(한 번에 하나씩만 빼니까)


T= int(input())                                                     # 테스트케이스 입력받음
for testcase in range(1,T+1):                                       # 테스트케이스 반복실행
    ironbar_with_laser = input()                                    # 쇠막대기와 레이저 값 받음
    ironbar_with_laser_list = list(map(str,ironbar_with_laser))     # 입력값을 리스트로
    # for bracket_i in range(len(ironbar_with_laser_list)):           # 괄호로 이루어진 쇠막대기 리스트에서 각 괄호를 인자로한 반복문
    #     if ironbar_with_laser_list[bracket_i] ==  '(':              # '('는 보기편하게 0으로 바꾸고
    #         ironbar_with_laser_list[bracket_i] = 0
    #     elif ironbar_with_laser_list[bracket_i] == ')':             # ')'는 보기편하게 1로 바꾼다.
    #         ironbar_with_laser_list[bracket_i] = 1
    
    # #레이저와 쇠막대기 구분하기
    # i = 0
    # while i < len(ironbar_with_laser_list)-1:                       # 레이저를 다른 값으로 분리시키기 위한 while문
    #     if ironbar_with_laser_list[i] == 0 and ironbar_with_laser_list[i+1]:    # 레이저를 나타내는 ()이면
    #         ironbar_with_laser_list[i] = 'A'                                    # 레이저의 시작점을 A로 바꿔주고
    #         del ironbar_with_laser_list[i+1]                                    # 레이저의 끝은 지워서 레이저를 A로 표현
    #     i += 1
    
    # 이제 레이저로 자르기 시작 작업테이블에 실제로 막대기 있다고 생각하면 아주아주 조금 편해짐
    worked_ironbar = 0                                              # 현재 판 위에 존재하는 쇠막대기
    made_ironbar = 0                                                # 레이저로 인해 갈라지며 생성된 쇠막대기
    e = 0
    # for e in range(len(ironbar_with_laser_list)):                 # 0~ (len(ironbar_with_laser_list)-1) 만큼
    while e < len(ironbar_with_laser_list):                         # 0~ (len(ironbar_with_laser_list)-1) 만큼
        # 순서중요! '(' ')' 레이저를 먼저 발견해야함.

        if ironbar_with_laser_list[e] == '(' and ironbar_with_laser_list[e+1] == ')': 
                                                                    # 레이저(A)를 만나게 되면 현재 작업중인 막대기 갯수는 그대로 있으므로
            made_ironbar += worked_ironbar                          # 현재까지 작업중인 막대기 갯수만큼 막대기를 생성한다.
            e += 2                                                  # e+2를 해줘야 레이저를 건너뛰니까

        elif ironbar_with_laser_list[e] == '(':                       # 열린괄호(0)를 만나게 된다면
            worked_ironbar += 1                                     # 작업중인 쇠막대기를 하나 증가시킨다.
            e += 1                                                  # 다음 리스트의 인덱스를 확인하러 가야지


        elif ironbar_with_laser_list[e] == ')':                     # 닫힌괄호(1)를 만나게 된다면
            worked_ironbar -= 1                                     # 이제 작업중인 막대기는 빼고
            made_ironbar += 1                                       # 작업중 막대기도 레이저로 생성된 막대기 중 하나가 된다.
            e += 1                                                  # 다음 리스트의 인덱스를 확인하러 가야지
    print(f'#{testcase} {made_ironbar}')                            # 출력값을 출력한다.