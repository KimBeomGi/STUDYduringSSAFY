# 목표
# 반복문(for, while)이 동작하는 핵심 원리에 대해 이해한다.
# 조건문(if)이 동작하는 핵심 원리에 대해 이해한다.
# 조건문을 이용하여 기본 자료형인 문자열을 슬라이싱할 수 있다.

# 문제
# 문자열을 전달받아 해당 문자열의 정중앙 문자를 출력하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 출력하라.

#[문제풀이]
# 문자열을 전달받아야 하므로 input()을 먼저 입력
# 그리고 문자열의 정중앙 문자를 출력해야하므로
# len(input())을 이용 그리고 그 중앙값을 구해서 중앙값을 출력
# 만약 짝수라면 중앙 2개를 출력

from math import *

Prt_srt=input()
mid_srt = floor(len(Prt_srt)/2)
if len(Prt_srt) % 2 == 1:
    print(Prt_srt[mid_srt])
else:
    print(Prt_srt[(mid_srt-1):(mid_srt+1)])