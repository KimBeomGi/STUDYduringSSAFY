'''
class Person:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return f'안녕, {self.name}'
    
class Mom(Person):
    gene ='XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class SecondChild(Dad, Mom):
    def walk(self):
        return '둘째가 걷기'
    def cry(self):
        return '둘째가 응애'

baby2 = SecondChild('아가')
print(baby2.cry())
print(baby2.walk())
print(baby2.swim())
print(baby2.gene)
print(baby2.greeting())


class Person:
    def __init__(self, name, age):
        #print('생성될 때 자동으로 불려요')
        self.name = name
        self.age = age
    def __str__(self):
        return '이 클래스를 하나의 문자열로 표현하면 이겁니다.'

aiden = Person('aiden', 23)
print(aiden)


class Person:
    count = 0

    def __init__(self, name):
        self.naem = name
        Person.count += 1
    
    @classmethod
    def number_of_population(cls):
         print(f'인구수는{cls.count}입니다.')

person1 = Person('아이유')
person2 = Person('이찬혁')

Person.number_of_population()
person1.number_of_population()
# 인스턴스 입장에서 number_of_population() 메서드가 들어갔어도 클래스가 가진 변수를 들고 나온다.
person2.number_of_population()
'''