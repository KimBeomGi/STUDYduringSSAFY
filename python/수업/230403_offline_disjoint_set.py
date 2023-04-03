# 서로소 집합: 서로소 집합들은 서로 중복된 원소를 포함하지 않음
# make_set, find_set, union 등의 연산이 가능.
# 원소의 개수는 10개라고 가정

def make_set():
    # 집합 10개 만들기
    return [x for x in range(11)]       # [0,1,2,3,4,5,5,6,7,8,9,10]

p = make_set()      # 인덱스에 해당하는 요소의 부모요소 번호를 가지는 배열

# 각 집합의 대표자를 반환하는 함수
# 대표자 : 부모의 번호와 자신의 번호가 일치하는 요소
def find_set(x):
    if x == p[x]:   # 내가 대표자면 반환
        return x
    else:       # 아니면... 부모가 대표자를 알고 있을것.
        return find_set(p[x])

# 두 개의 집합을 합침
def union(x,y):
    rx = find_set(x)
    ry = find_set(y)
    if rx != ry:
        # 합치는 방식은 많을 수 있는데...
        # 일단은 쉽게 y의 대표자의 부모를 x의 대표자로 만들기
        p[ry] =rx

p = make_set()
print(f'4: {find_set(4)}')
print(f'2: {find_set(2)}')
union(2, 4)
print(f'4: {find_set(4)}')
print(f'2: {find_set(2)}')
union(1, 5)
print(f'1: {find_set(1)}')
print(f'5: {find_set(5)}')
union(2,5)
print(f'1: {find_set(1)}')
print(f'2: {find_set(2)}')
print(f'4: {find_set(4)}')
print(f'5: {find_set(5)}')
union(2,8)
print(f'8: {find_set(8)}')