# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

# 단, 주어질 숫자는 10000을 넘지 않는다.


# [예제]

# 주어진 숫자가 10 일 경우 출력해야 할 정답은,

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
#  입력값 :10, 출력값 55

# for 문에서는 break 때문에 문제가 생겼음. while 문으로 시도해봐야지

# # for문
# num_sum = int(input('10,000미만의 정수를 넣어주세요:'))
# a_list = []

# i=1

# for i in range(1,num_sum+1):
#     if num_sum > 10000:
#         print(int(input('잘못 기입하셨습니다. 다시 실행해주세요.')))
#         break
#     else:
#         a_list.append(i)

# a_sum = sum(a_list)
# print(a_list)
# print(a_sum)
# ------------------------------------------------------------------------
#while 문
# num_sum = int(input('10,000미만의 정수를 입력해주세요:'))
# a_list = []
# i=1
# if num_sum >= 10000:
#     print("잘못된 값입니다.")   #여기서 다시 입력해주세요 하고 넘어가는게 안되네....쓰읍 왜지?
# else:
#     while num_sum < 10000:
#         a_list.append(i)
#         i +=1
#         if i == num_sum+1:
#             break
# # print(a_list)
# print(sum(a_list))

# 1~n값 더하기 공식이용 printf("%d", a*(a + 1) / 2);
num_sum = int(input())      # 계산에 입력될 값 작성
if num_sum <10000:
    print(int(num_sum*(num_sum+1)/2))
else:
    print("잘못된 값입니다.")