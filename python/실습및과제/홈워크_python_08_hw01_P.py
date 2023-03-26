# [문제]
# point 클래스와 rectangle클래스에 대한 명세 및 실행 예시를 참조하여 클래스를 구현하시오.

# 입력 예시
'''
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
'''
# 출력 예시
# 4
# 8
# True

# 9
# 12
# True

# [문제풀이]
# 1. 클래스 Point를 만들어준다.
# 1-1. 입력 받는 Point의 x,y값으로 생성자를 초기화하는 메서드 생성
# 1-1. p1 = Point(4,3)으로 표현할 수 있다고 했는데 저러면 p1이라는 변수를 Point()클래스를 이용해서 4,3을 집어넣어주는 것

# 2. 클래스 Rectangle을 만들어준다. 
# 2-1 Rectangle 클래스의 인스턴스 변수와 타입이 Point 클래스 인스턴스 이므로
# 2-2 Rectangle에서 point를 사용. 이 생각은 확실히 접고 point(부), Rectangle(자)의 형식으로 클래스를 작성해준다.
# 2-3-1.생성자 메서드는 1-1에서 완료
# 2-3-2. 좌표값인 p1,p2 초기화
# 2-3-3. get_area() 좌표값 이용 넓이 계산
# 2-3-4. get_perimeter() 좌표값이용 둘레 길이 계산
# 2-3-5. is_squre() 좌표값 이용 정사각형 여부 확인

class Point:                            # point 클래스 생성
    def __init__(self, x, y):           # 생성자 메서드 생성, 매개변수로 x, y값 초기화(생성한다)
        self.x = x
        self.y = y

class Rectangle:                        # Rectangle 클래스를  생성
    def __init__(self, p1, p2): # Point 클래스에서 x와 y를 받아옴.
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return int(abs(self.p1.x-self.p2.x) * abs(self.p1.y-self.p2.y))       # p1(x,y)와 p2(x,y)에서 각 x와 y의 차를 곱하면 그것이 사각형 넓이

    def get_perimeter(self):
        return int((abs(self.p1.x-self.p2.x) + abs(self.p1.y-self.p2.y))*2)   # p1(x,y)와 p2(x,y)에서 각 x와 y의 차를 더한 후 2를 곱해주면 그것이 사각형의 총 길이

    def is_square(self):
        # if abs(self.p1.x-self.p2.x) == abs(self.p1.y-self.p2.y):
        #     return True
        # else:
        #     return False
        return  abs(self.p1.x-self.p2.x) == abs(self.p1.y-self.p2.y)

        


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())