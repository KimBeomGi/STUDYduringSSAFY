# [문제]
# 1. 문자열 s_triangle로 각 변을 입력받았을 때, 어떤 삼각형인지 출력한다.
# 조건
# 1. 세 변의 길이가 같으면 정삼각형을 출력한다.
# 2. 두 변의 길이가 같으면 이등변 삼각형을 출력한다.
# 3. 피타고라스 정리 a^2+b^2 = c^2과 일치하면 직각삼각형을 출력한다.
# 4. 일반 삼각형인 경우 단순히 삼각형을 출력하고, 삼각형이 아닌 경우 삼각형 아님을 출력한다.
# 5. (짧은 두 변의 길이의 합이 가장 긴 변의 길이보다 크다면 삼각형이 될 수 있다.)

# [문제풀이]
# 문자열 s_triangle로 각 변을 입력받았을 때이므로 s_triangle은 우선 str로 작성
# 우선 조건을 보아 if, elif문을 잘 활용해보자.
# s_triangle로 각 변을 입력받았을 때와 삼각형이 아닌 경우를 보아 이 부분이 if 첫번째로 오도록 한다.

s_triangle = input()
s_triangle_list = list(map(int, s_triangle.split()))        # 문자열로 받은 s_trianlge을 int화 및 list화 해버리기
s_triangle_list = sorted(s_triangle_list, reverse=False)    # s_triangle_list를 오름차순화 하고 다시 s_triangle_list에 기입
# print(s_triangle_list)                                    # 제대로 s_triangle_list가 작동하는지 확인
if len(s_triangle_list) > 3 or (s_triangle_list[0] + s_triangle_list[1] <= s_triangle_list[2]):     # 조건 5에 부합하지 않음.
    print('변의 수를 잘 못 입력했거나, 삼각형이 될 수 없습니다.')                                             # 조건 4의 삼각형 아님을 출력.
elif s_triangle_list[0] == s_triangle_list[1] == s_triangle_list[2]:                                # 조건 1에 해당.
    print('정삼각형입니다.')
elif pow(s_triangle_list[0],2) + pow(s_triangle_list[1],2) == pow(s_triangle_list[2],2):            # 조건 3에 해당. 직각삼각형은 이등변 삼각형일 수도 있으므로 먼저 출력.
    print('직각삼각형입니다.')
elif s_triangle_list[0] == s_triangle_list[1] or s_triangle_list[0] == s_triangle_list[2] or s_triangle_list[1] == s_triangle_list[2]:  #조건 2에 해당.
    print('이등변 삼각형입니다.')
else:
    print('삼각형입니다.')