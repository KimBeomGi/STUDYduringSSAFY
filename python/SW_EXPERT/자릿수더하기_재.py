# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
# [제약 사항]
# 자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)

# [입력]
# 입력으로 자연수 N이 주어진다.

# [출력]
# 각 자릿수의 합을 출력한다.

# 입력
# 6789

# 출력
# 30

N = int(input())

a_list = []
if 1 <= N <= 9999 :
    for i in range(1,5):
        a_list.append(N%10) # N을 10으로 나눈 나머지가 결국 자릿값이 되기 때문에 이렇게 함
        N = N//10           # N을 10으로 나눈 몫을 남겨서 다시 자릿수 구하기 위함
        print(a_list)       # 잘 되고 있는지 확인용도
    print(sum(a_list))
else:
    print("범위를 확인하고 다시 실행해주세요")