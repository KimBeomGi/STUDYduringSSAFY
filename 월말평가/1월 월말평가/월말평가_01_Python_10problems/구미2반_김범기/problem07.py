# [문제]
# 당신은토이프로젝트로계산기를만들려고한다. 
# 이계산기는입력값에따라삼각형, 사각형그리고원의넓이를구할수있다.
# 또, 3개이상의입력값이있을때는모든수의합과평균을반환한다고한다.

# [문제풀이]
# 1. 각 계산기에 입력되는 갯수와 종류에 따라 달라지므로 if elif문을 적절히 이용
# 2. 주어질때 calculator(튜플) 형식으로 주어지므로 그에 맞게 적절히 이용
# 3. 입력되는 값은 항상 0보다 큰 양의 정숙값만 들어온다라고 되있으며
# 3-1. 구현하라는 것이 없기에 이것을 구현해야할 필요는 없는문제


# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    if len(numbers) == 1:                   # 1이면 원 넓이
        return (numbers[0]**2)*3.14
    elif len(numbers) == 2:                 # 2이면서 짝수이면 사각형 넓이
        if sum(numbers) % 2 == 0:
            return numbers[0]*numbers[1]
        else:                               # 2이면서 홀수이면 삼각형 넓이
            return (numbers[0]*numbers[1])/2
    elif len(numbers) >= 3:                 # 3개 이상이면 합, 평균
        return (sum(numbers), sum(numbers)/len(numbers))
    else:                                   # 0개 이면 0을 출력
        return 0




# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0