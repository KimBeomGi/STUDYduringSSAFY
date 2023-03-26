#[문제풀이]
# 1. 딕셔너리로 바꾸고{[이싸피:n], ===}형태로 변경
# 2. 몇 번을 왔는지 그리고 갔는지 비교 후 틀린 사람을 확인
# 3. collection 모듈의 counter 객체를 활용해야하므로 collection.py를 만들어주고 해당 
# 4. counter 함수로 하나 만들어두고 이때 받을 매개변수는 2개(entry_record, exit_record)로 받도록 만든다.
# 4-1. 그것이 각각 1번을 행하는 함수로 작동


# 문제 출력 예시
# 입장 기록 많은 TOP3
# 안도둑 10회
# 임온실 9회
# 이싸피 8회

# 출입 기록이 수상한 사람
# 최이썬은 입장 기록이 1회 더 많아 수상합니다.
# 염자바은 퇴장 기록이 2회 더 많아 수상합니다.

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']



# entry와 exit은 리스트로 들어올 것임
def counter(entry, exit):
    result = ''
    entry = sorted(entry)                                    # 차후 딕셔너리에서 출력 될 때 exit와 바로 비교할 수 있게 리스트에서 미리 정렬
    entry_num_times={}                                       # 입장 인원 명단을 정리하기 위한 딕셔너리
    for en_audience in entry:                                # 주어진 entry_record 리스트 내 인덱스를 for 반복문으로 돌리기
        try: entry_num_times[en_audience] += 1               # 주어진 entry_record 리스트 내 인덱스를 entry_num_times에 기입하고 그게 있다면 값에다가 +1을 해준다.
        except: entry_num_times[en_audience]=1               # 리스트 entry_record 내 인덱스를 entry_num_times에 기입하고 그게 없다면 값으로 1을 해준다.
    reverse_entry_numtimes= dict(map(reversed, entry_num_times.items()))            # 입장기록 많은 사람 출력하기 위함
    top_entry_audience = sorted(list(reverse_entry_numtimes), reverse= True)        # 내림차순으로 정렬해서 입장 기록 많은 3명확인 위함
    # print('입장 기록 많은 TOP3')
    result += '입장 기록 많은 TOP3\n'
    for top3_entry in top_entry_audience[0:3]:               # 입장 많은 3명에 대해서 확인 하기 위함
        # print(f'reverse_entry_numtimes.get(top3_entry) {top3_entry}회')
        result += f'{reverse_entry_numtimes.get(top3_entry)} {top3_entry}회\n'
    result += '\n'                                           # 입장기록top3와 퇴장기록top3를 구분하기 위한 한줄 띄기

    exit = sorted(exit)                                      # 차후 딕셔너리에서 출력 될 때 exit와 바로 비교할 수 있게 리스트   에서 미리 정렬
    exit_num_times={}                                        # 퇴장 인원 명단을 정리하기 위한 딕셔너리
    for ex_audience in exit:                                 # 주어진 exit_record 리스트 내 인덱스를 for 반복문으로 돌리기
        try: exit_num_times[ex_audience] += 1                # 주어진 exit_record 리스트 내 인덱스를 exit_num_times에 기입하고 그게 있다면 값에다가 +1을 해준다.
        except: exit_num_times[ex_audience]=1                # 리스트 exit_record 내 인덱스를 exit_num_times에 기입하고 그게 없다면 값으로 1을 해준다.
    reverse_exit_numtimes= dict(map(reversed, exit_num_times.items()))      # 퇴장 기록 많은 사람 출력하기 위함
    top_exit_audience = sorted(list(reverse_exit_numtimes), reverse= True)      # 내림차순으로 정렬해서 입장 기록 많은 3명확인 위함
    # print('퇴장 기록 많은 TOP3')
    result += '퇴장 기록 많은 TOP3\n'
    for top3_exit in top_exit_audience[0:3]:                 # 퇴장 많은 3명에 대해서 확인 하기 위함
        # print(f'reverse_exit_numtimes.get(top3_exit) {top3_entry}회')
        result += f'{reverse_exit_numtimes.get(top3_exit)} {top3_entry}회\n'
    result += '\n출입기록이 수상한 사람\n'                     # 퇴장기록top3와 출입기록이 수상한 사람을 구분하기 위한 한줄 띄기

    # 출입 내역 비교.
    entry_people_list = list(entry_num_times)                # 입장한 사람 명부 리스트로 entry_num_time와 exit_num_time 딕셔너리를 이용하기 위함.
    suspect_list = []
    for audience in entry_people_list:                       # 입장한 사람 명부를 반복문으로 돌리면서 entry_num_time와 exit_num_time 딕셔너리의 value를 비교하며, 일치여부를 확인하기 위함.
        if entry_num_times.get(audience) != exit_num_times.get(audience):                   # 입장과 퇴장 기록 수가 다르다면
            suspect_list.append(audience)                                                   # 용의자 리스트에 올려라
            if entry_num_times.get(audience) > exit_num_times.get(audience):                # 입장 기록이 퇴장기록 보다 많다면 입장-퇴장 수
                different1 = entry_num_times.get(audience) - exit_num_times.get(audience)
                # print(f'{audience} 은/는 입장 기록이 {different1}회 더 많아 수상합니다.')
                result += f'{audience}은/는 입장 기록이 {different1}회 더 많아 수상합니다.\n'
            elif entry_num_times.get(audience) < exit_num_times.get(audience):              # 입장 기록이 퇴장기록 보다 적다면 퇴장-입장 수
                different2 = exit_num_times.get(audience) - entry_num_times.get(audience)
                # print(f'{audience}은/는 입장 기록이 {different2}회 더 많아 수상합니다.')
                result += f'{audience}은/는 퇴장 기록이 {different2}회 더 많아 수상합니다.\n'

    # return (entry_num_times, exit_num_times)
    return result