# [문제]
# 페어 프로그래밍은 하나의 컴퓨터에서 두 사람의 프로그래머가 작업하는 방식을 의미한다.
# 진정한 프로그래머가 되기 위해 김해피는 페어를 매칭하기 위한 프로그램을 작성하려고 한다.
# 클래스를 활용해 작성하며 포함되는 메서드는 아래와 같다.
# [구성요소]
# 1. 초기화 메서드는 인자로 학생 이름으로 구성된 리스트를 받아서 인스턴스 변수에 할당한다.
# 2. pick(n) 메서드는 학생들 명단에서 인자 n명 만큼 랜덤으로 추출하여 return한다.
# 3. match_pair() 메서드는 학생들 명단을 랜덤으로 2명씩 매칭해준다.
# 3-1 이때, 학생들 명단의 수가 홀수명이면 단 한팀만 3명으로 구성한다.




import random

class ClassHelper:
    def __init__(self, name):                       # 초기화 메서드
        self.name = name

    def pick(self, n):
        return random.sample(self.name,  n)

    def match_pair(self):
        random.shuffle(self.name)
        result = []
        for i in range(0,len(self.name),2):
            if i == len(self.name)-3:
                result.append([self.name[i],self.name[i+1],self.name[i+2]])
                return result
            else:
                result.append([self.name[i],self.name[i+1]])



ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
