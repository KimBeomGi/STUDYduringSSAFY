class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2): # p1과 p2를 인자로 받아와서 각각 저장해준다.
        self.p1 = p1
        self.p2 = p2

    def get_area(self): # x값의 차이를 이용해 가로변의 길이를 구하고, y값의 차이를 이용해 세로변의 길이를 구한다.
        return abs(self.p1.x-self.p2.x) * abs(self.p1.y-self.p2.y)  # abs()는 절대값을 주는 함수

    def get_perimeter(self):    # 가로변 길이와 세로변 길이를 더한 뒤 곱하기 2
        return (abs(self.p1.x-self.p2.x) + abs(self.p1.y-self.p2.y)) * 2

    def is_square(self):    # 가로변과 세로변이 같으면 정사각형
        return abs(self.p1.x-self.p2.x) == abs(self.p1.y-self.p2.y)




# 입력 예시
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

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True