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