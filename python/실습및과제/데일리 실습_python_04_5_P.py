# [문제]
# 커닝하고 있는 사람은 시험장에서 퇴출
# 커닝하고 있는 사람의 리스트를 오름차순으로 출력
# 잠을 자고 있는 사람은 solving으로 바꾸어서 깨울것
# 이후 test_status 출력

# 출력값
# ['염자바', '임온실', '최이썬']
# test_status = {'김코딩': 'solving', '이싸피': 'solving', '오디비': 'solving', '조실습': 'solving', '박장고': 'solving'}

# [문제풀이]
#1. value값이 cheating 이면 test_status에서 제거하고, 새로운 리스트에 넣도록 한다.
#1-1. 그리고 오름차순이 될 수 있게 sorted()를 사용한다.
#2. value값이 sleeping 이면 solving으로 바꿔준다.


test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

cheating_students = []		# cheating 한 인원을 묶어둘 리스트
for student in test_status:					# cheating인원은 보내고, sleaping 인원은 깨우는 반복문
	if test_status[student] == 'cheating':
		cheating_students.append(student)
		
	elif test_status[student] == 'sleeping':
		test_status[student] = 'solving'

for cheat_student in cheating_students:		# cheating한 인원들을 test_status 딕셔너리에서 제거하는 for문
	del(test_status[cheat_student])

print(sorted(cheating_students))
print('test_status =', test_status)