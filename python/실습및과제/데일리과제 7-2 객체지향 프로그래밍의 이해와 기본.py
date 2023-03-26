# [문제]
# 개의 속성과 행위를 정의하는 Doggy 클래스를 만들어라.

# 구성 요소
# 1. 초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
# 2. bark()메서드를 호출하면 개는 짖을 수 있다.
# 3. 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
# 3-1. 개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.
# 3-2. 개가 죽으면 num_of_dogs의 값이 1 감소한다.
# 4. get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다.

class Doggy:                            # Doggy 클래스를 생성
    num_of_dogs = 0                     # 클래스 변수 현재 있는 개의 숫자를 기록하는 변수로 구성
    birth_of_dogs = 0                   # 클래스 변수 태어난 개의 숫자를 기록하는 변수
    def __init__(self,name):            # 개가 태어나면?!
        self.name = name
        Doggy.num_of_dogs += 1          # 개 현재 수 +1
        Doggy.birth_of_dogs += 1        # 개 태어난 수 +1
        # print('hello')

    def __del__(self):                  # 개가 죽으면?!
        Doggy.num_of_dogs -= 1          # 개 현재 수에서 -1
        # print('bye')

    def bark(self):                     # bark()메서드 생성
        # print(f'{self.name} 월월으르릉월월컹컹')
        return f'{self.name} 월월으르릉월월컹컹'
    
    def get_status(self):               # birth_of_dogs와 num_of_dogs의 수를 출력하는 메서드
        # print(Doggy.birth_of_dogs, Doggy.num_of_dogs)
        return Doggy.birth_of_dogs, Doggy.num_of_dogs
    
    
# d = Doggy('해피')
# del d
# print(Doggy.birth_of_dogs)

dog1 = Doggy('춘삼이')
dog2 = Doggy('왕철이')
dog3 = Doggy('곽봉팔')
dog4 = Doggy('이춘배')
dog5 = Doggy('서룡복')
dog6 = Doggy('철금이')
dog7 = Doggy('왕옥개')
dog1.bark()
print(Doggy.num_of_dogs)
print(Doggy.birth_of_dogs)
del dog4
print(Doggy.num_of_dogs)
print(Doggy.birth_of_dogs)