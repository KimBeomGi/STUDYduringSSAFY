# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# [입력]
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1   
 
# [출력]
# #1 200
# #2 208
# #3 121

#[문제풀이]
T=int(input())          #최초 테스트케이스 횟수 T 입력
for i in range(1,T+1):  #테스트 케이스를 1회부터 T회만큼 실행
    odd_save = list(map(int,input().split()))   # 10개의 값을 넣어서 리스트로 만들어줄 것
    odd_list = []   # 홀수만 모이게 될 리스트를 홀수만 모이게 만들기 전에 제작.
    for e in range (0, 10):     #총 10개의 수가 주어지므로 10번 돌림
        if odd_save[e]%2==1:    #홀수는 2로 나눴을 때 나머지가 1이므로 %2==1의 조건작성
            odd_list.append(odd_save[e])    # 조건이 충족하므로 odd_list에 append(odd_save[~])를 출력
        else:   #없으면 뭐 없이 그냥 넘어가야지.
            pass
    print('#'+str(i), sum(odd_list))    # 출력이 #1 200처럼 출력되야해서 돌리는 i 인자를 넣어주고 홀수의 합이므로 odd_list의 총합을 출력
