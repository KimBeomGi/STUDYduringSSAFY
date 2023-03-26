# 목표``
# 파이썬 기초 문법 (print, 이스케이프 문자열, 입력과 출력 등)에 대해 이해한다.파이썬 기본 자료형 (문자형, 수치형, 불린형)에 대해 이해한다.
# 파이썬 복합 자료형 (리스트, 딕셔너리, 튜플)에 대해 이해한다.set의 특징과 연산자를 이해한다.

# 문제
# 10 미만의 자연수에서 2과 7의 배수를 구하면 2,4,6,7,8이다. 이들의 총합은 27이다.1000미만의 자연수에서 2,7의 배수의 총합을 구하라.
# 요구사항
# 파이썬 버전에 대한 이해 파이썬 실행 환경에 대한 이해


# [문제 풀이]
# 2의 배수와 7의 배수를 구해야하므로 2*i 또는 7*i로 진행해주면 된다.
# 1000미만이므로 구해야하는 것은 <1000 으로 제약.
# 이제 총합을 구해야하므로 리스트를 활용해 리스트 sum을 이용해주면 될 듯하다.
# 폐기
# multiple_list=[]
# i=1
# while (2*i)<1000:
#     multiple_list.append[2*i]
#     i+1
# e=1
# while (7*e)<1000:
#     multiple_list.append[7*e]
#     e+1

# print(multiple_list)

multiple_list=[]
for i in range(1,1000):
    if i%2==0:
        multiple_list.append(i)
    elif i%7==0:
        multiple_list.append(i)
    else:
        pass
print(multiple_list)
print(sum(multiple_list))
