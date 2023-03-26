# [문제]
# 김코딩이 일하고 있는 박물관에 도둑이 들었다. 박물관 입구와 출구에 센서가 있다.
# 센서는 지나가는 사람이 누구인지 인지하여 방문자를 기록한다.
# 입장 기록은 entry_record list에, 퇴장 기록은 exit_record list에 아래처럼 정리 되어 있다.
# 주어진 조건으로 분석하여 수상한 사람을 분별하라.
# 1. 많이 방문한 사람이 도둑일 가능성이 높다. 가장 많이 입장한 세 사람을 찾아 출력하라.
# 2. 입장 횟수와 퇴장 횟수의 차이가 0이어야 정상이다. 횟수의 차이가 있을 경우 정말 수상하다.
# 2-1. 입장 횟수와 퇴장 횟수가 같지 않은 사람을 분별하여 출력하라.
# 제약 조건: collection 모듈의 counter 객체를 활용해야한다.

#[문제풀이]
# 1. collections 모듈을 불러와 Counter함수를 이용
# 2. Counter함수를 이용하면 각 동일 데이터가 몇 번 들어있는지 {'데이터명:숫자','데이터명:숫자'''''}의 딕셔너리로 주어지므로 이를 잘 활용해보자.
# 3. Counter함수로 만들어진 것을 list(dict.items()) 함수를 이용해 튜플로 바꾸어서 횟수로 정렬해보자.

# 문제 출력 예시
# 입장 기록 많은 TOP3
# 안도둑 10회
# 임온실 9회
# 이싸피 8회

# 출입 기록이 수상한 사람
# 최이썬은 입장 기록이 1회 더 많아 수상합니다.
# 염자바은 퇴장 기록이 2회 더 많아 수상합니다.

from collections import *

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']


entry_record_lst = list(dict(Counter(entry_record)).items())    # Counter한 entry_record를 딕셔너리로 변환 후 리스트로 변환 입장 기록의 명부 리스트화
# print(entry_record_lst)
exit_record_lst = list(dict(Counter(exit_record)).items())      # Counter한 exit_record를 딕셔너리로 변환 후 리스트로 변환 퇴장 기록의 명부 리스트화
# print(exit_record_lst)

entry_record_lst.sort(key=lambda x : x[1])                      # entry_record_lst를 횟수를 기준 오름차순 정렬.
# print(entry_record_lst)
entry_record_dic = dict(entry_record_lst)
# print(entry_record_dic)

exit_record_lst.sort(key=lambda x : x[1])                       # exit_record_lst를 횟수를 기준 오름차순 정렬
# print(exit_record_lst)
exit_record_dic = dict(exit_record_lst)
# print(exit_record_dic)


print('입장 기록 많은 TOP3')
for top_entry_person in entry_record_lst[:4:-1]:                # 입장 기록 많은 TOP3를 entry_record_lst를 뒤에서부터 읽어내서 뒤에서 4번째 전까지만 반복
    print(f'{top_entry_person[0]} {top_entry_person[1]}회')     # 입장 기록 많은 TOP3를 이름 횟수로 나타낼 수 있도록 f스트링 이용

print('\n출입 기록이 수상한 사람')
for entry_person in entry_record_lst[::-1]:                     # entry_record_lst에서 entry_person튜플을 인자로 반복문 실행
                                                                # entry_record_lst[::-1]을 한 이유는 출력값을 동일하게 만들기 위해서.
    if entry_record_dic[entry_person[0]] > exit_record_dic[entry_person[0]]:                        # 입장횟수가 퇴장횟수보다 많다면?
        different_num1 = entry_record_dic[entry_person[0]] - exit_record_dic[entry_person[0]]       # 입장 - 퇴장
        print(f'{entry_person[0]}은 입장기록이 {different_num1}회 더 많아 수상합니다.')
    elif entry_record_dic[entry_person[0]] < exit_record_dic[entry_person[0]]:                      # 퇴장횟수가 입장횟수보다 많다면?
        different_num2 = exit_record_dic[entry_person[0]] - entry_record_dic[entry_person[0]]       # 퇴장 - 입장
        print(f'{entry_person[0]}은 퇴장기록이 {different_num2}회 더 많아 수상합니다.')