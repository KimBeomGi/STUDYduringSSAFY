# 목표
# 학습주제파이썬 개발 환경에 대한 이해파이썬 예외처리 기본 방식에 대한 이해
# 학습목표모듈 동작 방식에 대해 이해한다.파이썬 자료 구조의 구조 및 동작 방식에 대해 이해한다.예외처리 방식 및 활용 방식에 대해 이해한다.
# 문제
# 김코딩은 타임머신을 개발했다. 적절한 날짜를 정하기 위해서 날짜를 분석하는 프로그램이 필요하다. 다음 조건을 만족하는 프로그램을 완성하라.

# 연도, 월, 일을 순서대로 입력받는다.
# 윤년으로 가면 타임머신에 에러가 생긴다. 윤년을 입력했을 경우 연도를 다시 입력받아야 한다.
# 윤년이 아닌 연도를 입력받을 경우, 날짜를 편하게 정할 수 있도록 해당 연도의 달력을 출력하라.
# 김코딩은 월요일을 싫어한다. 입력한 날짜가 월요일인 경우 경고 메시지를 출력하라.
# 입력이 완료되면 연, 월, 날짜, 그리고 요일을 dictionary에 정리하여 출력하라.
# HINT: calendar 모듈을 활용하라.	(공식문서 링크)
# import calendar
# print(calendar.calendar(2022))

# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

#[문제풀이]
# 1. 윤년 구하기(400의 배수. 그러나 4의 배수이면서 100의 배수는 아니게)
# 1-1. 윤년 이라면 print('윤년입니다. 연도를 다시 입력해주세요.')
# 2. 윤년이 아니라면 해당 연도 달력 출력
# 3. 월요일 입력시 경고 메시지를 출력
# 4. 연, 월, 일 순으로 받은 입력을 정리해 dictionayry에
# 4-1 {'년' : 2015, '월' : 8, '일' : 31, '요일' : '월요일'}로 출력

import calendar
import datetime
year = int(input('연도를 입력해주세요:'))   # 윤년인지 판단하기
while year : 
    if year % 400 == 0:
        print('윤년입니다. 연도를 다시 입력해주세요.')
        year = int(input('연도를 입력해주세요:'))       # 윤년이면 재입력받을 수 있도록 해줌
        continue
    elif year % 4 == 0 and year % 100 != 0:
        print('윤년입니다. 연도를 다시 입력해주세요.')
        year = int(input('연도를 입력해주세요:'))
        continue
    else:
        print(calendar.calendar(year))
        break

month = int(input('월을 입력해주세요:'))
day = int(input('날짜를 입력해주세요:'))

if calendar.weekday(year, month, day) == 0: # 요일을 출력하는 함수를 이용
    print('경고 월요일입니다!')

dayofweek = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
go_to_when = {}
go_to_when.setdefault('년', year)
go_to_when.setdefault('월', month)
go_to_when.setdefault('일', day)
go_to_when.setdefault('요일', dayofweek[calendar.weekday(year, month, day)])
print(go_to_when)